"""Paid Italian legal databases connector registry.

Provides a unified interface for accessing Italian paid legal databases.
Currently implements ItalgiureWeb (via Cassa Forense credentials) with
automated scraping and fallback to external search links for all databases.

Supported databases:
- italgiureweb: Cassazione/Consiglio di Stato/TAR/Corte Costituzionale via Cassa Forense
- dejure: Giuffrè legal database (placeholder, requires API partnership)
- onelegale: Wolters Kluwer Italia / Leggi d'Italia (placeholder)
- dike: Dike Giuridica (placeholder)
- eurex: Eurex legal database (placeholder)
- jurisdata: Juris Data (placeholder)
"""
from __future__ import annotations

from typing import Dict, List, Optional
from urllib.parse import quote


# Registry of supported paid databases
PAID_DATABASES: Dict[str, Dict] = {
    "italgiureweb": {
        "name": "ItalgiureWeb",
        "description": "Banca dati del Centro Elettronico di Documentazione della Cassazione (via Cassa Forense)",
        "url": "https://www.italgiure.giustizia.it/sncass/",
        "login_url": "https://www.cassaforense.it/",
        "requires": ["username", "password"],
        "automated": True,
    },
    "dejure": {
        "name": "De Jure",
        "description": "Banca dati Giuffrè Francis Lefebvre — giurisprudenza, dottrina, normativa",
        "url": "https://www.dejure.it/",
        "search_url": "https://www.dejure.it/ricerca?query={query}",
        "requires": ["api_key"],
        "automated": False,
    },
    "onelegale": {
        "name": "One Legale",
        "description": "Wolters Kluwer Italia — giurisprudenza, dottrina, normativa (ex Pluris / Leggi d'Italia)",
        "url": "https://www.wki.it/one-legale",
        "search_url": "https://www.wki.it/ricerca?q={query}",
        "requires": ["api_key"],
        "automated": False,
    },
    "dike": {
        "name": "Dike Giuridica",
        "description": "Banca dati Dike Giuridica — giurisprudenza e normativa",
        "url": "https://www.dikegiuridica.it/",
        "search_url": "https://www.dikegiuridica.it/ricerca/{query}",
        "requires": ["api_key"],
        "automated": False,
    },
    "eurex": {
        "name": "Eurex",
        "description": "Banca dati Eurex — giurisprudenza italiana",
        "url": "https://www.eurex.it/",
        "search_url": "https://www.eurex.it/ricerca?q={query}",
        "requires": ["api_key"],
        "automated": False,
    },
    "jurisdata": {
        "name": "Juris Data",
        "description": "Banca dati Juris Data — giurisprudenza e normativa",
        "url": "https://www.jurisdata.it/",
        "search_url": "https://www.jurisdata.it/ricerca/{query}",
        "requires": ["api_key"],
        "automated": False,
    },
}


def get_paid_database_status(settings: Optional[Dict] = None) -> Dict[str, Dict]:
    """Return configuration status for all paid databases.

    Args:
        settings: The 'paid_databases' section from settings_store.

    Returns:
        Dict mapping database key to {name, configured, enabled, automated, description}.
    """
    settings = settings or {}
    status = {}
    for key, meta in PAID_DATABASES.items():
        cfg = settings.get(key, {})
        required = meta.get("requires", [])
        configured = bool(cfg.get("enabled")) and all(cfg.get(f) for f in required)
        status[key] = {
            "name": meta["name"],
            "configured": configured,
            "enabled": bool(cfg.get("enabled", False)),
            "automated": meta.get("automated", False),
            "description": meta["description"],
            "url": meta["url"],
        }
    return status


def build_external_search_url(db_name: str, query: str) -> str:
    """Build an external search URL for a paid database (fallback).

    Args:
        db_name: Key of the database in PAID_DATABASES.
        query: Search query string.

    Returns:
        URL string or empty string if database unknown.
    """
    meta = PAID_DATABASES.get(db_name)
    if not meta:
        return ""
    encoded = quote(query)
    search_template = meta.get("search_url") or meta.get("url")
    if "{query}" in search_template:
        return search_template.replace("{query}", encoded)
    # Fallback: append query parameter if no template
    if "?" in search_template:
        return f"{search_template}&q={encoded}"
    return f"{search_template}?q={encoded}"


def search_paid_database(
    name: str,
    query: str,
    settings: Optional[Dict] = None,
    max_results: int = 5,
) -> Dict:
    """Search a paid Italian legal database.

    For automated databases (italgiureweb) attempts live scraping.
    For all others, returns a fallback link to the external search page.

    Args:
        name: Database key (e.g. 'italgiureweb').
        query: Search query.
        settings: paid_databases settings dict.
        max_results: Max number of results to return.

    Returns:
        Dict with keys:
            - success: bool
            - source: str (human readable name)
            - results: list of result dicts
            - fallback_url: optional external search URL
            - message: optional user-facing message
    """
    settings = settings or {}
    meta = PAID_DATABASES.get(name)
    if not meta:
        return {
            "success": False,
            "source": name,
            "results": [],
            "message": f"Banca dati '{name}' non supportata.",
        }

    cfg = settings.get(name, {})
    required = meta.get("requires", [])
    configured = bool(cfg.get("enabled")) and all(cfg.get(f) for f in required)

    if not configured:
        fallback = build_external_search_url(name, query)
        return {
            "success": False,
            "source": meta["name"],
            "results": [],
            "fallback_url": fallback,
            "message": (
                f"{meta['name']} non configurata. "
                "Configura le credenziali in Impostazioni oppure apri la ricerca esterna."
            ),
        }

    if not meta.get("automated", False):
        fallback = build_external_search_url(name, query)
        return {
            "success": False,
            "source": meta["name"],
            "results": [],
            "fallback_url": fallback,
            "message": (
                f"{meta['name']} è disponibile solo come ricerca esterna. "
                "L'integrazione automatica richiede una partnership con l'editore."
            ),
        }

    # Automated path: currently only ItalgiureWeb
    if name == "italgiureweb":
        try:
            from .italgiure import search_italgiure
            results = search_italgiure(
                query=query,
                max_results=max_results,
                credentials={
                    "username": cfg.get("username", ""),
                    "password": cfg.get("password", ""),
                },
            )
            if results:
                return {
                    "success": True,
                    "source": meta["name"],
                    "results": results,
                }
        except Exception as exc:
            fallback = build_external_search_url(name, query)
            return {
                "success": False,
                "source": meta["name"],
                "results": [],
                "fallback_url": fallback,
                "message": f"Errore connessione {meta['name']}: {exc}. Apri la ricerca esterna.",
            }

    fallback = build_external_search_url(name, query)
    return {
        "success": False,
        "source": meta["name"],
        "results": [],
        "fallback_url": fallback,
        "message": f"Nessun risultato su {meta['name']}. Prova la ricerca esterna.",
    }


def list_paid_database_links(query: str) -> List[Dict]:
    """Return quick-search fallback links for all supported paid databases.

    Useful when the user has not configured credentials or automation fails.
    """
    links = []
    for key, meta in PAID_DATABASES.items():
        links.append({
            "key": key,
            "name": meta["name"],
            "description": meta["description"],
            "url": build_external_search_url(key, query),
            "automated": meta.get("automated", False),
        })
    return links
