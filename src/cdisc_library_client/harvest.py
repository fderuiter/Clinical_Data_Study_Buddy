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

from cdisc_data_symphony.builder.crfgen.schema import Form, FieldDef


class CrfGen:
    """A class for harvesting CRF data from the CDISC Library API."""

    def __init__(self, api_key: str, ig_filter: Optional[str] = None):
        self.api_key = api_key
        self.ig_filter = ig_filter
        self.client = self._get_client()

    def _get_client(self) -> AuthenticatedClient:
        """
        Get an authenticated client for the CDISC Library API.

        This method sets up an httpx client with appropriate headers, timeouts, and retries.
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
        """
        Pull CDASH IG -> domains -> scenarios and convert to Form objects.

        This method iterates through the CDASH Implementation Guides, their domains,
        and scenarios, fetching the data for each and converting them into Form objects.
        """
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
        """
        Convert a CDISC Library API response for a domain or scenario into a Form object.

        This method maps the fields from the API response to the attributes of the
        Form and FieldDef pydantic models.
        """
        fields = []
        for f in data.get("fields", []):
            field_def = FieldDef(
                oid=f.get("name"),
                prompt=f.get("label"),
                datatype=f.get("fieldType"),
                cdash_var=f.get("name"),
                range_check=f.get("rangeCheck"),
            )
            fields.append(field_def)

        return Form(
            title=data.get("name"),
            domain=data.get("domain"),
            scenario=data.get("scenario"),
            fields=fields,
        )


def harvest(api_key: str, ig_filter: str | None = None) -> List[Form]:
    """
    A high-level function to pull CDASH IG -> domains -> scenarios and convert to Form objects.

    This function is a convenient wrapper around the CrfGen class.
    """
    crfgen = CrfGen(api_key, ig_filter)
    return crfgen.harvest()
