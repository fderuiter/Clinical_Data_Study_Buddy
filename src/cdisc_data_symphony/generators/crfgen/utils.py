"""
This module provides utility functions for the crfgen package, including
authentication helpers for accessing the CDISC Library API.
"""

import os

DUMMY_VALUES = {"", "dummy-key", "***"}


def get_api_key() -> str:
    """
    Gets and validates the CDISC Library API key from an environment variable.

    This function retrieves the API key from the `CDISC_PRIMARY_KEY` environment
    variable and checks that it is not a dummy or empty value.

    Returns:
        str: The validated CDISC Library API key.

    Raises:
        ValueError: If the `CDISC_PRIMARY_KEY` environment variable is not set
                    or contains a dummy value.
    """
    token = os.getenv("CDISC_PRIMARY_KEY")
    if not token or token in DUMMY_VALUES:
        raise ValueError("CDISC_PRIMARY_KEY is not set correctly")
    return token
