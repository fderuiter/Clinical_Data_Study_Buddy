"""
This module provides a centralized service for interacting with the CDISC Library API.
"""

import httpx

from cdisc_library_client.client import AuthenticatedClient
from clinical_data_study_buddy.generators.crfgen.utils import get_api_key


def get_client() -> AuthenticatedClient:
    """
    Get an authenticated client for the CDISC Library API.

    This function retrieves the API key and creates an AuthenticatedClient
    instance with appropriate settings for connecting to the CDISC Library API,
    including automatic retries.

    Returns:
        AuthenticatedClient: An authenticated client for the CDISC Library API.
    """
    api_key = get_api_key()
    headers = {"api-key": api_key, "Accept": "application/json"}
    transport = httpx.HTTPTransport(retries=5)
    client = AuthenticatedClient(
        base_url="https://library.cdisc.org/api",
        token="dummy",
        headers=headers,
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
        httpx_args={"transport": transport},
    )
    return client
