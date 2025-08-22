from __future__ import annotations

import os
from typing import List, Optional

import httpx
from cdisc_library_client.client import AuthenticatedClient
from cdisc_library_client.api.cdash_implementation_guide_cdashig import (
    get_mdr_cdashig_version,
    get_mdr_cdashig_version_domains,
    get_mdr_cdashig_version_scenarios,
)
from cdisc_library_client.api.default import get_mdr_products_data_collection

from crfgen.schema import Form


class CrfGen:
    def __init__(self, api_key: str, ig_filter: Optional[str] = None):
        self.api_key = api_key
        self.ig_filter = ig_filter
        self.client = self._get_client()

    def _get_client(self) -> AuthenticatedClient:
        """
        Get an authenticated client for the CDISC Library API.
        """
        transport = httpx.HTTPTransport(retries=5)
        client = AuthenticatedClient(
            base_url="https://library.cdisc.org/api",
            token=self.api_key,
            headers={"Accept": "application/json", "Cache-Control": "no-cache"},
            auth_header_name="api-key",
            prefix="",
            timeout=30.0,
            httpx_args={"transport": transport},
        )
        return client

    def harvest(self) -> List[Form]:
        """Pull CDASH IG -> domains -> scenarios and convert to Form objects."""
        products = get_mdr_products_data_collection.sync(client=self.client)
        cdashig_links = products.additional_properties["_links"]["cdashig"]
        forms: list[Form] = []
        for ver_link in cdashig_links:
            if self.ig_filter and self.ig_filter not in ver_link["title"]:
                continue
            ig = get_mdr_cdashig_version.sync(client=self.client, version=ver_link["title"])
            for dom_link in ig["_links"].get("domains", []):
                dom = get_mdr_cdashig_version_domains.sync(client=self.client, version=ver_link["title"], domain=dom_link["title"])
                scenarios = dom["_links"].get("scenarios") or []
                payloads = [dom] + [
                    get_mdr_cdashig_version_scenarios.sync(client=self.client, version=ver_link["title"], domain=dom_link["title"], scenario=s["title"])
                    for s in scenarios
                ]
                for p in payloads:
                    forms.append(self._form_from_api(p))
        return forms

    def _form_from_api(self, data: dict) -> Form:
        """Convert a CDISC Library API response into a Form object."""
        return Form(
            name=data.get("name"),
            ig_name=data.get("igName"),
            ig_version=data.get("igVersion"),
            domain=data.get("domain"),
            scenario=data.get("scenario"),
            fields=[
                {
                    "name": f.get("name"),
                    "label": f.get("label"),
                    "field_type": f.get("fieldType"),
                    "terminology": f.get("terminology"),
                    "instructions": f.get("instructions"),
                }
                for f in data.get("fields", [])
            ],
        )
