"""ItalgiureWeb connector — Cassa Forense / CED Cassazione legal database.

This module attempts to automate access to ItalgiureWeb using Cassa Forense
credentials. Because the official portal uses complex authentication flows
(SPID, redirects, anti-CSRF tokens), the connector is designed to gracefully
degrade to a manual external search link when automation is not possible.

The primary goal is to give users a unified entry point for Italian paid
databases while keeping credentials local and under studio control.
"""
from __future__ import annotations

import logging
import re
import urllib.parse
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

BASE_URL = "https://www.italgiure.giustizia.it"
SNCASS_URL = f"{BASE_URL}/sncass/"
CASSAFORENSE_LOGIN_URL = "https://www.cassaforense.it/"
SENTENZEWEB_URL = "https://www.cortedicassazione.it/cassazione-resources/resources/css/SentenzeWeb"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9",
}


def _build_fallback_result(query: str, reason: str) -> List[Dict]:
    """Return a single synthetic result pointing to external search pages."""
    encoded = urllib.parse.quote(query)
    return [
        {
            "title": f"🔍 Cerca '{query}' su ItalgiureWeb",
            "url": SNCASS_URL,
            "source": "ItalgiureWeb",
            "date": "",
            "court": "",
            "snippet": (
                f"{reason} Clicca per aprire ItalgiureWeb e inserire manualmente la ricerca. "
                "Le credenziali Cassa Forense restano nel browser."
            ),
            "fallback": True,
        },
        {
            "title": f"🔍 Cerca '{query}' su SentenzeWeb (ultimi 5 anni Cassazione)",
            "url": (
                "https://www.cortedicassazione.it/cassazione-resources/resources/css/SentenzeWeb"
                f"?testoRicerca={encoded}"
            ),
            "source": "SentenzeWeb",
            "date": "",
            "court": "Corte di Cassazione",
            "snippet": "Ricerca libera sulle sentenze civili e penali della Cassazione degli ultimi 5 anni.",
            "fallback": True,
        },
    ]


def _extract_form_fields(soup: BeautifulSoup) -> Dict[str, str]:
    """Extract hidden input fields from a login form."""
    fields: Dict[str, str] = {}
    for form in soup.find_all("form"):
        for inp in form.find_all("input"):
            name = inp.get("name")
            value = inp.get("value", "")
            if name and inp.get("type") in (None, "hidden", "text", "password"):
                fields[name] = value
    return fields


def _parse_search_results(html: str, max_results: int) -> List[Dict]:
    """Parse ItalgiureWeb search result HTML.

    This is a best-effort parser: the exact DOM may vary. It looks for
    result rows, links and snippets generically.
    """
    soup = BeautifulSoup(html, "html.parser")
    results: List[Dict] = []

    # Strategy 1: rows with class containing "risultato"
    for row in soup.find_all(["tr", "div", "li"], class_=re.compile("risultato", re.I)):
        link = row.find("a", href=True)
        if not link:
            continue
        title = link.get_text(strip=True)
        href = link["href"]
        detail_url = href if href.startswith("http") else urllib.parse.urljoin(BASE_URL, href)
        snippet = ""
        for p in row.find_all(["p", "span", "div"]):
            text = p.get_text(strip=True)
            if text and text != title and len(text) > 20:
                snippet = text
                break
        results.append({
            "title": title,
            "url": detail_url,
            "source": "ItalgiureWeb",
            "date": "",
            "court": "",
            "snippet": snippet,
        })
        if len(results) >= max_results:
            break

    # Strategy 2: any link that looks like a document detail
    if not results:
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if not any(k in href.lower() for k in ("documento", "sentenza", "atto", "dettaglio", "provvedimento")):
                continue
            title = a.get_text(strip=True)
            if not title or len(title) < 5:
                continue
            detail_url = href if href.startswith("http") else urllib.parse.urljoin(BASE_URL, href)
            results.append({
                "title": title,
                "url": detail_url,
                "source": "ItalgiureWeb",
                "date": "",
                "court": "",
                "snippet": "",
            })
            if len(results) >= max_results:
                break

    return results


def search_italgiure(
    query: str,
    max_results: int = 5,
    credentials: Optional[Dict[str, str]] = None,
) -> List[Dict]:
    """Search ItalgiureWeb with optional Cassa Forense credentials.

    Args:
        query: Search string.
        max_results: Maximum number of results to return.
        credentials: Dict with 'username' and 'password'.

    Returns:
        List of result dicts. If automation fails, returns fallback results
        pointing to ItalgiureWeb and SentenzeWeb manual search pages.
    """
    credentials = credentials or {}
    username = credentials.get("username", "").strip()
    password = credentials.get("password", "").strip()

    if not username or not password:
        logger.info("ItalgiureWeb credentials not configured; returning fallback links.")
        return _build_fallback_result(query, "Credenziali Cassa Forense non configurate.")

    session = requests.Session()
    session.headers.update(HEADERS)

    try:
        # Step 1: fetch the ItalgiureWeb search page to detect redirects / auth requirements
        logger.debug("Fetching ItalgiureWeb search page...")
        resp = session.get(SNCASS_URL, timeout=20, allow_redirects=True)
        resp.raise_for_status()

        # If we are already on a result/search page and it does not redirect to login,
        # attempt a search directly (public/SentenzeWeb-like behaviour).
        if "login" not in resp.url.lower() and "cassaforense" not in resp.url.lower():
            logger.debug("ItalgiureWeb accessible without login; performing direct search.")
            search_params = {"testoRicerca": query}
            search_resp = session.get(
                SNCASS_URL,
                params=search_params,
                timeout=20,
                allow_redirects=True,
            )
            results = _parse_search_results(search_resp.text, max_results)
            if results:
                return results

        # Step 2: attempt Cassa Forense login (best-effort)
        logger.debug("Attempting Cassa Forense login...")
        login_resp = session.get(CASSAFORENSE_LOGIN_URL, timeout=20)
        login_resp.raise_for_status()
        login_soup = BeautifulSoup(login_resp.text, "html.parser")

        # Heuristic: find the login form and its action
        login_form = None
        action = None
        for form in login_soup.find_all("form"):
            inputs = {inp.get("name", "").lower(): inp for inp in form.find_all("input")}
            if any("user" in k or "codice" in k or "pin" in k for k in inputs):
                login_form = form
                action = form.get("action") or CASSAFORENSE_LOGIN_URL
                break

        if not login_form:
            logger.warning("Could not locate Cassa Forense login form; returning fallback.")
            return _build_fallback_result(query, "Impossibile individuare il form di login Cassa Forense.")

        # Build payload using discovered fields + credentials
        payload = _extract_form_fields(login_soup)
        # Try common field names
        for candidate in ("username", "user", "codice", "codiceMeccanografico", "login"):
            if candidate in payload:
                payload[candidate] = username
                break
        else:
            # If no candidate matched, add a generic username field
            payload["username"] = username

        for candidate in ("password", "pass", "pin", "pwd"):
            if candidate in payload:
                payload[candidate] = password
                break
        else:
            payload["password"] = password

        action_url = action if action.startswith("http") else urllib.parse.urljoin(CASSAFORENSE_LOGIN_URL, action)
        post_resp = session.post(action_url, data=payload, timeout=30, allow_redirects=True)
        post_resp.raise_for_status()

        # Heuristic: check whether we are still on a login page
        if "login" in post_resp.url.lower() or "errore" in post_resp.text.lower():
            logger.warning("Cassa Forense login appears to have failed; returning fallback.")
            return _build_fallback_result(query, "Login Cassa Forense non riuscito.")

        # Step 3: go back to ItalgiureWeb and perform search
        logger.debug("Login likely succeeded; searching ItalgiureWeb...")
        search_resp = session.get(
            SNCASS_URL,
            params={"testoRicerca": query},
            timeout=20,
            allow_redirects=True,
        )
        results = _parse_search_results(search_resp.text, max_results)
        if results:
            return results

        return _build_fallback_result(query, "Nessun risultato trovato su ItalgiureWeb.")

    except requests.exceptions.Timeout:
        logger.warning("ItalgiureWeb request timed out; returning fallback.")
        return _build_fallback_result(query, "Timeout nella connessione a ItalgiureWeb.")
    except requests.exceptions.RequestException as exc:
        logger.warning("ItalgiureWeb request error: %s; returning fallback.", exc)
        return _build_fallback_result(query, f"Errore di connessione: {exc}.")
    except Exception as exc:
        logger.exception("Unexpected error in ItalgiureWeb connector")
        return _build_fallback_result(query, f"Errore imprevisto: {exc}.")
