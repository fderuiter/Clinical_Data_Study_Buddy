import csv
from pathlib import Path
from typing import Sequence

from cdisc_generators.crfgen.schema import Form

from .registry import register


@register("csv")
def export_csv(forms: Sequence[Form], outdir: Path) -> None:
    path = outdir / "forms.csv"
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["domain", "oid", "prompt"])
        for form in forms:
            for fld in form.fields:
                writer.writerow([form.domain, fld.oid, fld.prompt])
