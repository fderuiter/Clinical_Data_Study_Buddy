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

    doc = Document(doc_path)
    # The first table is the administrative section (2 cols)
    # The second table is the variables section (6 cols)
    table = doc.tables[1]
    assert len(table.columns) == 6

    texts = "\n".join(p.text for p in doc.paragraphs)
    assert "Footnotes" in texts
    assert "[1]" in texts

    admin = doc.tables[0].cell(0, 0).text.replace("\xa0", " ")
    assert admin == "SECTION A  ADMINISTRATIVE"
    from zipfile import ZipFile

    with ZipFile(doc_path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8")
        assert "w14:checkbox" in xml or "w14:date" in xml
        assert "Validate dependencies" in xml
        assert xml.count("<w:bottom") > 0

    # There are two tables in the document, one for admin and one for variables
    assert len(doc.tables) == 2
    # The variables table is the second one
    table = doc.tables[1]
    assert len(table.columns) == 6
