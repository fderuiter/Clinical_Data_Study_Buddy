from pathlib import Path
from typing import List

from docx import Document

from ..schema import Form
from .registry import register


@register("docx")
def render_docx(forms: List[Form], out_dir: Path):
    """Render forms as simple DOCX files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in forms:
        doc = Document()
        title = f.title
        if f.scenario:
            title += f" ({f.scenario})"
        doc.add_heading(title, level=1)

        table = doc.add_table(rows=1, cols=4)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = "OID"
        hdr_cells[1].text = "Prompt"
        hdr_cells[2].text = "Datatype"
        hdr_cells[3].text = "Codelist"

        for fld in f.fields:
            row = table.add_row().cells
            row[0].text = fld.oid
            row[1].text = fld.prompt
            row[2].text = fld.datatype
            row[3].text = fld.codelist.nci_code if fld.codelist else ""

        doc.save(out_dir / f"{f.domain}.docx")
