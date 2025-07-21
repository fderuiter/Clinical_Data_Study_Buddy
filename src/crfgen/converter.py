"""
Helpers to translate CDISC Library client DTOs -> crfgen.schema objects.
"""

from typing import Any

from crfgen.schema import Form, FieldDef, Codelist


def field_from_api(f: Any) -> FieldDef:
    cl = (
        Codelist(nci_code=f.codelist.nci_code, href=f.codelist.href)
        if getattr(f, "codelist", None) else None
    )
    return FieldDef(
        oid=f.cdash_variable,
        prompt=f.prompt,
        datatype=f.datatype,
        cdash_var=f.cdash_variable,
        codelist=cl,
    )


def form_from_api(payload: Any) -> Form:
    return Form(
        title=payload.title,
        domain=payload.domain,
        scenario=getattr(payload, "scenario", None),
        fields=[field_from_api(f) for f in payload.fields],
    )
