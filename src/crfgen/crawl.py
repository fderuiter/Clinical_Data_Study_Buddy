from __future__ import annotations

import json
import pathlib
import time
from typing import List, Optional

from cdisc_library_client.client import AuthenticatedClient
from crfgen.converter import form_from_api
from crfgen.http import cached_get
from crfgen.schema import Form

BASE = "https://library.cdisc.org/api"
ACCEPT = "application/vnd.cdisc+json"
DELAY = 0.2  # seconds between calls (<= 60 req/min)


def _client(token: str) -> AuthenticatedClient:
    if isinstance(token, (bytes, bytearray)):
        token = token.decode()
    return AuthenticatedClient(base_url=BASE, token=str(token), timeout=30.0)


def _json(url: str, token: str):
    if isinstance(token, (bytes, bytearray)):
        token = token.decode()
    headers = {"Authorization": f"Bearer {token}", "Accept": ACCEPT}
    data = cached_get(url, headers)
    time.sleep(DELAY)
    return data


def harvest(token: str, ig_filter: Optional[str] = None) -> List[Form]:
    """Pull CDASH IG -> domains -> scenarios and convert to Form objects."""
    if isinstance(token, (bytes, bytearray)):
        token = token.decode()
    root = _json(f"{BASE}/mdr/cdashig", token)
    forms: list[Form] = []
    for ver in root["_links"]["versions"]:
        if ig_filter and ig_filter not in ver["title"]:
            continue
        ig = _json(ver["href"], token)
        for dom_link in ig["_links"]["domains"]:
            dom = _json(dom_link["href"], token)
            scenarios = dom["_links"].get("scenarios") or []
            payloads = [dom] + [_json(s["href"], token) for s in scenarios]
            for p in payloads:
                forms.append(form_from_api(p))
    return forms


# Convenience writer


def write_json(forms: List[Form], path: str = "crf.json") -> None:
    pathlib.Path(path).write_text(json.dumps([f.model_dump() for f in forms], indent=2))
