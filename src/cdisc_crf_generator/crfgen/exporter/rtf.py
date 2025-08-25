import tempfile
from pathlib import Path
from typing import Sequence

import pypandoc

from crfgen.schema import Form
from .docx import export_docx
from .registry import register


@register("rtf")
def export_rtf(forms: Sequence[Form], outdir: Path, style: dict = None) -> None:
    """
    Exports the given forms to an RTF document.

    This function first generates a DOCX file in a temporary location,
    and then converts it to RTF using pandoc.
    """
    with tempfile.NamedTemporaryFile(suffix=".docx") as tmp:
        docx_path = tmp.name
        export_docx(forms, Path(docx_path).parent, style, output_filename=Path(docx_path).name)
        rtf_path = outdir / f"{forms[0].id}.rtf"
        pypandoc.convert_file(str(docx_path), "rtf", outputfile=str(rtf_path))
