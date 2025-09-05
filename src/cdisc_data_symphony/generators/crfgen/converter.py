"""
This module provides helper functions to translate Data Transfer Objects (DTOs)
from the CDISC Library client into the schema objects used by the crfgen module.
"""

from typing import Any

from cdisc_data_symphony.generators.crfgen.schema import Codelist, FieldDef, Form


def _get(obj: Any, key: str):
    """
    Safely gets a value from an object, whether it's a dict or an object.

    Args:
        obj (Any): The object or dictionary to get the value from.
        key (str): The key or attribute name.

    Returns:
        The value associated with the key or attribute, or None if not found.
    """
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


def field_from_api(f: Any) -> FieldDef:
    """
    Converts a field object from the CDISC Library API to a FieldDef object.

    Args:
        f (Any): The field object from the API, can be a dict or an object.

    Returns:
        FieldDef: The converted FieldDef object.
    """
    codelist_obj = _get(f, "codelist")
    cl = (
        Codelist(
            nci_code=_get(codelist_obj, "nci_code"), href=_get(codelist_obj, "href")
        )
        if codelist_obj
        else None
    )
    return FieldDef(
        oid=_get(f, "cdash_variable"),
        prompt=_get(f, "prompt"),
        datatype=_get(f, "datatype"),
        cdash_var=_get(f, "cdash_variable"),
        codelist=cl,
    )
