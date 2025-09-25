"""
This module provides the functionality to export CRF (Case Report Form) data
to an RTF (Rich Text Format) file. It leverages the DOCX exporter and pandoc
for the conversion.
"""

import tempfile
from pathlib import Path
from typing import Sequence

import pypandoc

from clinical_data_study_buddy.core.models.schema import Form

from .docx import export_docx
from .registry import register


@register("rtf")
def export_rtf(forms: Sequence[Form], outdir: Path, style: dict = None) -> None:
    """
    Exports a sequence of Form objects to an RTF document.

    This function first generates a .docx file in a temporary location,
    and then converts it to RTF using pandoc.

    Args:
        forms (Sequence[Form]): A sequence of Form objects to be exported.
        outdir (Path): The output directory where the RTF file will be saved.
        style (dict, optional): A dictionary defining the styles to be applied
                                to the intermediate .docx document. Defaults to None.
    """
    with tempfile.NamedTemporaryFile(suffix=".docx") as tmp:
        docx_path = tmp.name
        export_docx(
            forms, Path(docx_path).parent, style, output_filename=Path(docx_path).name
        )
        rtf_path = outdir / f"{forms[0].id}.rtf"
        pypandoc.convert_file(str(docx_path), "rtf", outputfile=str(rtf_path))
