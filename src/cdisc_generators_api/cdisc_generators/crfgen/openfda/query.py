from typing import Optional

def term_query(field: str, term: str) -> str:
    """
    Creates a term query for the openFDA API.

    Args:
        field: The field to search.
        term: The term to search for.

    Returns:
        A formatted term query string.
    """
    return f'{field}:"{term}"'

def range_query(field: str, start: str, end: str) -> str:
    """
    Creates a range query for the openFDA API.

    Args:
        field: The field to search.
        start: The start of the range (e.g., "YYYY-MM-DD").
        end: The end of the range (e.g., "YYYY-MM-DD").

    Returns:
        A formatted range query string.
    """
    return f'{field}:[{start}+TO+{end}]'

def count_query(field: str) -> str:
    """
    Creates a count query for the openFDA API.

    Args:
        field: The field to count.

    Returns:
        A formatted count query string.
    """
    if not field.endswith(".exact"):
        return f"{field}.exact"
    return field

def paging_query(limit: Optional[int] = None, skip: Optional[int] = None) -> dict:
    """
    Creates a dictionary of paging parameters for the openFDA API.

    Args:
        limit: The number of results to return.
        skip: The number of results to skip.

    Returns:
        A dictionary of paging parameters.
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
