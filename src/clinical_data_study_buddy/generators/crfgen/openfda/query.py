"""
This module provides helper functions for constructing query strings and
parameters for the OpenFDA API. These functions simplify the process of
creating term, range, count, and paging queries.
"""
from typing import Optional

def term_query(field: str, term: str) -> str:
    """
    Creates a term query string for the OpenFDA API.

    Args:
        field (str): The field to search within.
        term (str): The term to search for.

    Returns:
        str: A formatted term query string.
    """
    return f'{field}:"{term}"'

def range_query(field: str, start: str, end: str) -> str:
    """
    Creates a range query string for the OpenFDA API.

    Args:
        field (str): The field to search within.
        start (str): The start of the range (e.g., "YYYY-MM-DD").
        end (str): The end of the range (e.g., "YYYY-MM-DD").

    Returns:
        str: A formatted range query string.
    """
    return f'{field}:[{start}+TO+{end}]'

def count_query(field: str) -> str:
    """
    Creates a count query string for the OpenFDA API.

    This function ensures that the field name ends with ".exact" to perform
    an exact count.

    Args:
        field (str): The field to count.

    Returns:
        str: A formatted count query string.
    """
    if not field.endswith(".exact"):
        return f"{field}.exact"
    return field

def paging_query(limit: Optional[int] = None, skip: Optional[int] = None) -> dict:
    """
    Creates a dictionary of paging parameters for the OpenFDA API.

    Args:
        limit (Optional[int]): The number of results to return. Cannot be
                               greater than 1000.
        skip (Optional[int]): The number of results to skip. Cannot be greater
                              than 25000 without using `search_after`.

    Returns:
        dict: A dictionary of paging parameters.

    Raises:
        ValueError: If `limit` or `skip` exceed their maximum allowed values.
    """
    params = {}
    if limit is not None:
        if limit > 1000:
            raise ValueError("Limit cannot be greater than 1000")
        params["limit"] = limit
    if skip is not None:
        if skip > 25000:
            raise ValueError("Skip cannot be greater than 25000 without search_after")
        params["skip"] = skip
    return params
