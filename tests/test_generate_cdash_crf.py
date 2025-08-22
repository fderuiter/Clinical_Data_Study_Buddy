import subprocess
import sys


def test_help():
    result = subprocess.run(
        [sys.executable, "scripts/generate_cdash_crf.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Generate Word CRF shells" in result.stdout


def test_generate(tmp_path):
    out_dir = tmp_path / "out"
    result = subprocess.run(
        [
            sys.executable,
            "scripts/generate_cdash_crf.py",
            "--model",
            "data_standards/1_collection/CDASH_Model_v1.3.xlsx",
            "--ig",
            "data_standards/1_collection/CDASHIG_v2.3.xlsx",
            "--out",
            str(out_dir),
            "--domains",
            "AE",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    doc_path = out_dir / "AE_Adverse_Events_CRF.docx"
    assert doc_path.exists()

    from docx import Document
    from zipfile import ZipFile

    doc = Document(doc_path)
    # The first table is the administrative section, the second is the main one.
    table = doc.tables[1]
    assert len(table.columns) == 6
