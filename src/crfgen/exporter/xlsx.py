from __future__ import annotations
from pathlib import Path
from typing import List
import pandas as pd

from ..schema import Form
from .registry import register


@register("xlsx")
def render_xlsx(forms: List[Form], out_dir: Path) -> None:
    """Write all forms to a single Excel workbook."""
    rows = []
    for form in forms:
        for fld in form.fields:
            rows.append(
                {
                    "form": form.title,
                    "domain": form.domain,
                    "scenario": form.scenario or "",
                    "oid": fld.oid,
                    "prompt": fld.prompt,
                    "datatype": fld.datatype,
                    "codelist": fld.codelist.nci_code if fld.codelist else "",
                }
            )
    out_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_excel(out_dir / "forms.xlsx", index=False)
