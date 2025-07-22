from pathlib import Path
from typing import Sequence

from crfgen.schema import Form
from .registry import register


@register("tex")
def export_latex(forms: Sequence[Form], outdir: Path) -> None:
    for form in forms:
        path = outdir / f"{form.domain}.tex"
        with path.open("w") as fh:
            fh.write(f"\\section{{{form.title}}}\n")
            for fld in form.fields:
                fh.write(f"\\item {fld.prompt} ({fld.oid})\n")

