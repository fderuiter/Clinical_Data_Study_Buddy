"""
Helpers to translate CDISC Library client DTOs -> crfgen.schema objects.
"""

from typing import Any

from crfgen.schema import Codelist, FieldDef, Form


def _get(obj: Any, key: str):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key)


def field_from_api(f: Any) -> FieldDef:
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
