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

from clinical_data_study_buddy.core.models.schema import Form, FieldDef


class CrfGen:
    """
    A class for harvesting CRF data from the CDISC Library API.

    This class provides methods to connect to the CDISC Library API, fetch data
    for CDASH Implementation Guides, and convert the data into a list of
    Form objects.
    """

    def __init__(self, api_key: str, ig_filter: Optional[str] = None):
        """
        Initializes the CrfGen class.

        Args:
            api_key (str): The API key for the CDISC Library.
            ig_filter (Optional[str]): A string to filter the CDASH IG versions.
                                       Only versions containing this string will
                                       be processed. Defaults to None.
        """
        self.api_key = api_key
        self.ig_filter = ig_filter
        self.client = self._get_client()

    def _get_client(self) -> AuthenticatedClient:
        """
        Get an authenticated client for the CDISC Library API.

        This method sets up an httpx client with appropriate headers, timeouts,
        and retries to ensure reliable communication with the API.

        Returns:
            AuthenticatedClient: An authenticated client for the CDISC Library API.
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

        Returns:
            List[Form]: A list of Form objects representing the harvested CRF data.
        """
        products = get_mdr_products_data_collection.sync(client=self.client)
        cdashig_links = products.additional_properties.get("_links", {}).get("cdashig", [])
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

        Args:
            data (dict): The API response data for a domain or scenario.

        Returns:
            Form: A Form object representing the domain or scenario.
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

    This function is a convenient wrapper around the CrfGen class that simplifies
    the process of harvesting CRF data from the CDISC Library.

    Args:
        api_key (str): The API key for the CDISC Library.
        ig_filter (Optional[str]): A string to filter the CDASH IG versions.
                                   Only versions containing this string will
                                   be processed. Defaults to None.

    Returns:
        List[Form]: A list of Form objects representing the harvested CRF data.
    """
    crfgen = CrfGen(api_key, ig_filter)
    return crfgen.harvest()
