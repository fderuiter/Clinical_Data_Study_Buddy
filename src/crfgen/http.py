"""
Light wrapper around requests to add retry/back-off and
JSON disk-cache (protects Library quota & speeds tests).
"""

from __future__ import annotations

import json
import pathlib
import time
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

CACHE_DIR = pathlib.Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)


def _retry_session() -> requests.Session:
    r = Retry(total=5, backoff_factor=0.4, status_forcelist=[502, 503, 504, 429])
    s = requests.Session()
    s.mount("https://", HTTPAdapter(max_retries=r))
    return s


def cached_get(url: str, headers: dict[str, str], ttl_days: int = 30) -> Any:
    fname = CACHE_DIR / (url.replace("/", "_").replace(":", "") + ".json")
    if fname.exists() and (time.time() - fname.stat().st_mtime) < ttl_days * 86400:
        return json.loads(fname.read_text())

    sess = _retry_session()
    r = sess.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    fname.write_text(r.text)
    return r.json()
