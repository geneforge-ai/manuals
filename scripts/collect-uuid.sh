#!/usr/bin/env bash
# =============================================================================
# GeneForge AI Labs — System UUID Collector
# Client-side script to collect the machine UUID for license activation.
# No sensitive data is transmitted. Only the DMI System UUID is read.
# =============================================================================

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"

print_usage() {
    cat <<EOF
Usage: ${SCRIPT_NAME} [OPTIONS]

Collect the System UUID from this machine for GeneForge license activation.

Options:
  -o, --output FILE    Write UUID to FILE instead of stdout
  -h, --help           Show this help message

Examples:
  ${SCRIPT_NAME}
  ${SCRIPT_NAME} --output /tmp/my-uuid.txt
EOF
}

# --- Parse arguments ---
OUTPUT_FILE=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        -o|--output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            print_usage >&2
            exit 1
            ;;
    esac
done

# --- Collect UUID ---
UUID=""
METHOD=""

# Method 1: sysfs (no sudo required on most systems)
if [[ -r /sys/class/dmi/id/product_uuid ]]; then
    UUID="$(cat /sys/class/dmi/id/product_uuid | tr -d '[:space:]')"
    METHOD="sysfs"
fi

# Method 2: dmidecode (requires sudo on most systems)
if [[ -z "${UUID}" ]] && command -v dmidecode &>/dev/null; then
    UUID="$(sudo dmidecode -s system-uuid 2>/dev/null | tr -d '[:space:]' || true)"
    if [[ -n "${UUID}" ]]; then
        METHOD="dmidecode"
    fi
fi

# Method 3: systemd machine-id (fallback, not DMI but stable per install)
if [[ -z "${UUID}" ]] && [[ -r /etc/machine-id ]]; then
    UUID="$(cat /etc/machine-id | tr -d '[:space:]')"
    METHOD="machine-id"
    echo "⚠️  Warning: DMI UUID not available. Using machine-id fallback." >&2
    echo "   Please contact GeneForge support if activation fails." >&2
fi

# Validate UUID format (basic check)
if [[ -z "${UUID}" ]]; then
    echo "❌ ERROR: Unable to determine System UUID." >&2
    echo "   Tried: /sys/class/dmi/id/product_uuid, dmidecode, /etc/machine-id" >&2
    echo "   Please run with sudo or contact GeneForge support." >&2
    exit 1
fi

# --- Output ---
RESULT="{""\"uuid\""": ""\"${UUID}\""", ""\"method\""": ""\"${METHOD}\""", ""\"timestamp\""": ""\"$(date -Iseconds)\"""}"

if [[ -n "${OUTPUT_FILE}" ]]; then
    echo "${RESULT}" > "${OUTPUT_FILE}"
    echo "✅ UUID written to: ${OUTPUT_FILE}" >&2
    echo "   Method used: ${METHOD}" >&2
else
    echo "${RESULT}"
fi
