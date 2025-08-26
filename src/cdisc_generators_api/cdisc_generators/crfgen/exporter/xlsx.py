from pathlib import Path
from typing import Sequence

import openpyxl

from cdisc_generators_api.cdisc_generators.crfgen.schema import Form

from .registry import register


@register("xlsx")
def export_xlsx(forms: Sequence[Form], outdir: Path) -> None:
    path = outdir / "forms.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["domain", "oid", "prompt"])
    for form in forms:
        for fld in form.fields:
            ws.append([form.domain, fld.oid, fld.prompt])
    wb.save(path)
