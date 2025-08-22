"""
Authentication utilities.
"""

import os

import httpx
from cdisc_library_client.client import AuthenticatedClient

DUMMY_VALUES = {"", "dummy-key", "***"}
BASE = "https://library.cdisc.org/api"
ACCEPT = "application/vnd.cdisc+json"


def get_api_key() -> str:
    """Get CDISC Library API key from env and validate it."""
    token = os.getenv("CDISC_PRIMARY_KEY")
    if not token or token in DUMMY_VALUES:
        raise ValueError("CDISC_PRIMARY_KEY is not set correctly")
    return token


def get_client() -> AuthenticatedClient:
    """
    Get an authenticated client for the CDISC Library API.
    """
    token = get_api_key()
    transport = httpx.HTTPTransport(retries=5)
    client = AuthenticatedClient(
        base_url=BASE,
        token=token,
        headers={"Accept": ACCEPT},
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
        httpx_args={"transport": transport},
    )
    return client
