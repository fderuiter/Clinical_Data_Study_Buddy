"""
Authentication utilities.
"""

import os

DUMMY_VALUES = {"", "dummy-key", "***"}


def get_api_key() -> str:
    """Get CDISC Library API key from env and validate it."""
    token = os.getenv("CDISC_PRIMARY_KEY")
    if not token or token in DUMMY_VALUES:
        raise ValueError("CDISC_PRIMARY_KEY is not set correctly")
    return token
