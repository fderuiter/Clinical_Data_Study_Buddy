import pandas as pd
from pathlib import Path
from typing import List
from ..schema import Form
from .registry import register


@register("xlsx")
def render_xlsx(forms: List[Form], out_dir: Path):
    out_dir.mkdir(exist_ok=True, parents=True)
    with pd.ExcelWriter(out_dir / "forms.xlsx") as xw:
        for f in forms:
            df = pd.DataFrame(
                [
                    {
                        "OID": fld.oid,
                        "Prompt": fld.prompt,
                        "Datatype": fld.datatype,
                        "Codelist": fld.codelist.nci_code if fld.codelist else "",
                    }
                    for fld in f.fields
                ]
            )
            sheet = f"{f.domain[:28]}{('-'+f.scenario) if f.scenario else ''}"[:31]
            df.to_excel(xw, sheet_name=sheet or f.domain, index=False)
