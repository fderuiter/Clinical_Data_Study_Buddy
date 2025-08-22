"""
Light wrapper around httpx to add
JSON disk-cache (protects Library quota & speeds tests).
"""

from __future__ import annotations

import json
import pathlib
import time
from typing import Any

import httpx

from cdisc_library_client.client import AuthenticatedClient

CACHE_DIR = pathlib.Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)


def cached_get(client: AuthenticatedClient, url: str, ttl_days: int = 30) -> Any:
    """
    A cached GET request that uses the AuthenticatedClient.
    """
    fname = CACHE_DIR / (url.replace("/", "_").replace(":", "") + ".json")
    if fname.exists() and (time.time() - fname.stat().st_mtime) < ttl_days * 86400:
        return json.loads(fname.read_text())

    httpx_client = client.get_httpx_client()
    try:
        r = httpx_client.get(url)
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise RuntimeError(f"Resource not found: {url}") from e
        raise

    fname.write_text(r.text)
    return r.json()
