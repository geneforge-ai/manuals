"""Tests for paid Italian legal database connectors."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "web-ui"))

from core.connectors.paid_databases import (
    PAID_DATABASES,
    build_external_search_url,
    get_paid_database_status,
    list_paid_database_links,
    search_paid_database,
)
from core.connectors.italgiure import search_italgiure


def test_paid_databases_registry_complete():
    """All expected databases are registered."""
    keys = set(PAID_DATABASES.keys())
    expected = {"italgiureweb", "dejure", "onelegale", "dike", "eurex", "jurisdata"}
    assert expected.issubset(keys)
    for meta in PAID_DATABASES.values():
        assert "name" in meta
        assert "url" in meta
        assert "requires" in meta


def test_build_external_search_url_known_databases():
    """External search URLs are generated for all registered databases."""
    query = "art. 2043 c.c. risarcimento"
    for key in PAID_DATABASES:
        url = build_external_search_url(key, query)
        assert url.startswith("http")
        assert "art" in url or "2043" in url or "risarcimento" in url or "q=" in url


def test_get_paid_database_status_empty():
    """Status with no settings reports no database configured."""
    status = get_paid_database_status({})
    for key, info in status.items():
        assert info["configured"] is False
        assert info["enabled"] is False


def test_get_paid_database_status_italgiure_configured():
    """ItalgiureWeb is reported configured when credentials and enabled flag are present."""
    settings = {
        "italgiureweb": {
            "enabled": True,
            "username": "ABC123",
            "password": "secret",
        },
        "dejure": {"api_key": ""},
    }
    status = get_paid_database_status(settings)
    assert status["italgiureweb"]["configured"] is True
    assert status["italgiureweb"]["enabled"] is True
    assert status["dejure"]["configured"] is False


def test_search_paid_database_unsupported():
    """Unsupported database returns a clean error."""
    result = search_paid_database("unknown_db", "query", {})
    assert result["success"] is False
    assert "non supportata" in result["message"]


def test_search_paid_database_italgiure_not_configured():
    """Unconfigured ItalgiureWeb returns fallback link."""
    result = search_paid_database("italgiureweb", "prova", {})
    assert result["success"] is False
    assert result["fallback_url"]
    assert "italgiure" in result["fallback_url"]


def test_search_paid_database_placeholder_returns_external_link():
    """Placeholder databases return external search link."""
    settings = {"dejure": {"enabled": True, "api_key": "fake-key"}}
    result = search_paid_database("dejure", "art. 1218 c.c.", settings)
    assert result["success"] is False
    assert result["fallback_url"]
    assert "dejure" in result["fallback_url"].lower() or "q=" in result["fallback_url"]


def test_list_paid_database_links():
    """Quick links include all databases and an external URL."""
    links = list_paid_database_links("diritto europeo")
    keys = {link["key"] for link in links}
    assert "italgiureweb" in keys
    assert "dejure" in keys
    for link in links:
        assert link["url"].startswith("http")
        assert "diritto+europeo" in link["url"] or "diritto%20europeo" in link["url"] or "q=" in link["url"]


def test_italgiure_connector_returns_fallback_without_credentials():
    """ItalgiureWeb connector gracefully falls back when credentials are missing."""
    results = search_italgiure("art. 2043 c.c.", max_results=5, credentials={})
    assert isinstance(results, list)
    assert len(results) >= 1
    assert results[0].get("fallback") is True
    assert "ItalgiureWeb" in results[0]["source"]


def test_italgiure_connector_returns_fallback_with_invalid_credentials():
    """ItalgiureWeb connector falls back on invalid/bad credentials."""
    results = search_italgiure(
        "prova",
        max_results=5,
        credentials={"username": "bad", "password": "bad"},
    )
    assert isinstance(results, list)
    assert len(results) >= 1
    # Either fallback results or empty list are acceptable; fallback is expected
    assert all(r.get("fallback") is True for r in results) or len(results) == 0
