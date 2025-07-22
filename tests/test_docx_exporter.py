import os
import subprocess
from pathlib import Path
from docx import Document

from crfgen.schema import load_forms
from crfgen.exporter import EXPORTERS
import crfgen.exporter.docx  # register docx exporter


def test_render_docx(tmp_path: Path):
    forms = load_forms("tests/.data/sample_crf.json")
    exporter = EXPORTERS["docx"]
    exporter(forms, tmp_path)
    files = list(tmp_path.glob("*.docx"))
    assert files
    doc = Document(files[0])
    texts = [cell.text for row in doc.tables[0].rows for cell in row.cells]
    assert "OID" in texts


def test_build_script(tmp_path: Path):
    cmd = [
        "python",
        "scripts/build.py",
        "--source",
        "tests/.data/sample_crf.json",
        "--outdir",
        str(tmp_path),
        "--formats",
        "docx",
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    subprocess.check_call(cmd, env=env)
    assert list(Path(tmp_path).glob("*.docx"))
