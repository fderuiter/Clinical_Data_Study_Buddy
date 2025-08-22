from __future__ import annotations

import json
import pathlib
import time
from typing import List, Optional

from cdisc_library_client.client import AuthenticatedClient
from crfgen.converter import form_from_api
from crfgen.http import cached_get
from crfgen.schema import Form

DELAY = 0.2  # seconds between calls (<= 60 req/min)


def _json(client: AuthenticatedClient, url: str):
    data = cached_get(client, url)
    time.sleep(DELAY)
    return data


def harvest(client: AuthenticatedClient, ig_filter: Optional[str] = None) -> List[Form]:
    """Pull CDASH IG -> domains -> scenarios and convert to Form objects."""
    base_url = str(client.get_httpx_client().base_url).rstrip("/")
    products = _json(client, f"{base_url}/mdr/products/DataCollection")
    cdashig_links = products["_links"]["cdashig"]
    forms: list[Form] = []
    for ver_link in cdashig_links:
        if ig_filter and ig_filter not in ver_link["title"]:
            continue
        ig = _json(client, ver_link["href"])
        for dom_link in ig["_links"]["domains"]:
            dom = _json(client, dom_link["href"])
            scenarios = dom["_links"].get("scenarios") or []
            payloads = [dom] + [_json(client, s["href"]) for s in scenarios]
            for p in payloads:
                forms.append(form_from_api(p))
    return forms


# Convenience writer


def write_json(forms: List[Form], path: str = "crf.json") -> None:
    pathlib.Path(path).write_text(json.dumps([f.model_dump() for f in forms], indent=2))
