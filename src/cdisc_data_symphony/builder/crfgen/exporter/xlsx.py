"""
This module provides the functionality to export CRF (Case Report Form) data
to a Microsoft Excel (.xlsx) file.
"""
from pathlib import Path
from typing import Sequence

import openpyxl

from cdisc_data_symphony.builder.crfgen.schema import Form

from .registry import register


@register("xlsx")
def export_xlsx(forms: Sequence[Form], outdir: Path) -> None:
    """
    Exports a sequence of Form objects to an .xlsx file.

    The resulting Excel file will contain a single sheet with the domain, OID,
    and prompt for each field in each form.

    Args:
        forms (Sequence[Form]): A sequence of Form objects to be exported.
        outdir (Path): The output directory where the .xlsx file will be saved.
    """
    path = outdir / "forms.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Forms"
    ws.append(["domain", "oid", "prompt"])
    for form in forms:
        for fld in form.fields:
            ws.append([form.domain, fld.oid, fld.prompt])
    wb.save(path)
