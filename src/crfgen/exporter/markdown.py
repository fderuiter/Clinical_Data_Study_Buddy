from pathlib import Path
from typing import Sequence

from crfgen.schema import Form
from .registry import register


@register("md")
def export_markdown(forms: Sequence[Form], outdir: Path) -> None:
    for form in forms:
        path = outdir / f"{form.domain}.md"
        with path.open("w") as fh:
            fh.write(f"# {form.title}\n")
            for fld in form.fields:
                fh.write(f"- {fld.prompt} ({fld.oid})\n")

