import tempfile
from pathlib import Path
from typing import Sequence

import pypandoc

from cdisc_data_symphony.generators.crfgen.schema import Form
from .docx import export_docx
from .registry import register


@register("pdf")
def export_pdf(forms: Sequence[Form], outdir: Path, style: dict = None) -> None:
    """
    Exports the given forms to a PDF document.

    This function first generates a DOCX file in a temporary location,
    and then converts it to PDF using pandoc.
    """
    with tempfile.NamedTemporaryFile(suffix=".docx") as tmp:
        docx_path = tmp.name
        export_docx(forms, Path(docx_path).parent, style, output_filename=Path(docx_path).name)
        pdf_path = outdir / f"{forms[0].id}.pdf"
        pypandoc.convert_file(str(docx_path), "pdf", outputfile=str(pdf_path))
