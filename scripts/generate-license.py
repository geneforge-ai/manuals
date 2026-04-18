#!/usr/bin/env python3
"""
GeneForge AI Labs — License Key Generator
Generates cryptographically signed license.key files bound to a System UUID.

Usage:
    python3 generate-license.py \
        --client acme-corp \
        --uuid 12345678-ABCD-EFGH-IJKL-901234567890 \
        --days 365 \
        --output license.key

Environment:
    GENEFORGE_LICENSE_SECRET  Shared secret for HMAC-SHA256 signing.
                              If unset, a random secret is generated and printed.
"""

import argparse
import hashlib
import hmac
import json
import os
import sys
from datetime import datetime, timedelta, timezone


def generate_secret() -> str:
    """Generate a random 64-char hex secret."""
    return os.urandom(32).hex()


def sign_license(client_id: str, uuid: str, expires_at: str, secret: str) -> str:
    """Create HMAC-SHA256 signature of license payload."""
    payload = f"{client_id}:{uuid}:{expires_at}"
    return hmac.new(
        secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def verify_license(license_data: dict, secret: str) -> bool:
    """Verify license signature and expiry."""
    try:
        expected = sign_license(
            license_data["client_id"],
            license_data["uuid"],
            license_data["expires_at"],
            secret,
        )
        if not hmac.compare_digest(expected, license_data["signature"]):
            return False
        # Check expiry
        expires = datetime.fromisoformat(license_data["expires_at"])
        if datetime.now(timezone.utc) > expires:
            return False
        return True
    except (KeyError, ValueError):
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate a GeneForge license.key file bound to a System UUID."
    )
    parser.add_argument("--client", default="", help="Client ID (e.g. acme-corp)")
    parser.add_argument(
        "--uuid", default="", help="System UUID from collect-uuid.sh"
    )
    parser.add_argument(
        "--days", type=int, default=365, help="License validity in days (default: 365)"
    )
    parser.add_argument(
        "--output", default="license.key", help="Output file path (default: license.key)"
    )
    parser.add_argument(
        "--secret",
        default=os.environ.get("GENEFORGE_LICENSE_SECRET"),
        help="Shared HMAC secret (or set GENEFORGE_LICENSE_SECRET env var)",
    )
    parser.add_argument(
        "--verify",
        help="Verify an existing license.key file instead of generating",
    )
    args = parser.parse_args()

    # Enforce required args only when not verifying
    if not args.verify:
        if not args.client or not args.uuid:
            parser.error("--client and --uuid are required when generating a license")

    # Handle verification mode
    if args.verify:
        if not args.secret:
            print("❌ ERROR: --verify requires --secret or GENEFORGE_LICENSE_SECRET", file=sys.stderr)
            sys.exit(1)
        with open(args.verify, "r") as f:
            data = json.load(f)
        if verify_license(data, args.secret):
            print("✅ License is VALID")
            print(f"   Client: {data['client_id']}")
            print(f"   UUID:   {data['uuid']}")
            print(f"   Expires: {data['expires_at']}")
            sys.exit(0)
        else:
            print("❌ License is INVALID or EXPIRED")
            sys.exit(1)

    # Generation mode
    secret = args.secret
    if not secret:
        secret = generate_secret()
        print("⚠️  No secret provided. Generated random secret (save this!):", file=sys.stderr)
        print(f"   GENEFORGE_LICENSE_SECRET={secret}", file=sys.stderr)
        print(file=sys.stderr)

    issued_at = datetime.now(timezone.utc)
    expires_at = issued_at + timedelta(days=args.days)

    license_data = {
        "client_id": args.client,
        "uuid": args.uuid,
        "issued_at": issued_at.isoformat(),
        "expires_at": expires_at.isoformat(),
        "signature": sign_license(args.client, args.uuid, expires_at.isoformat(), secret),
    }

    with open(args.output, "w") as f:
        json.dump(license_data, f, indent=2)

    print(f"✅ License generated: {args.output}")
    print(f"   Client:    {args.client}")
    print(f"   UUID:      {args.uuid}")
    print(f"   Valid for: {args.days} days")
    print(f"   Expires:   {expires_at.isoformat()}")
    print(f"   Secret:    {'<provided>' if args.secret else '<random — see stderr>'}")


if __name__ == "__main__":
    main()
