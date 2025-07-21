import pandas as pd
from pathlib import Path
from typing import List

from ..schema import Form
from .registry import register


@register("csv")
def render_csv(forms: List[Form], out_dir: Path) -> None:
    rows = []
    for f in forms:
        for fld in f.fields:
            rows.append({
                "form": f.title,
                "domain": f.domain,
                "scenario": f.scenario or "",
                "oid": fld.oid,
                "prompt": fld.prompt,
                "datatype": fld.datatype,
                "codelist": fld.codelist.nci_code if fld.codelist else "",
            })
    out_dir.mkdir(exist_ok=True, parents=True)
    pd.DataFrame(rows).to_csv(out_dir / "forms.csv", index=False)
