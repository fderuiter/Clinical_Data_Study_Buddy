import subprocess
import sys
import pandas as pd
from unittest.mock import patch


def test_help():
    result = subprocess.run(
        [sys.executable, "scripts/generate_cdash_crf.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Generate Word CRF shells" in result.stdout


@patch("scripts.generate_cdash_crf.get_cdashig_variables_from_api")
def test_generate(mock_get_variables, tmp_path):
    out_dir = tmp_path / "out"
    mock_df = pd.DataFrame([
        {
            "Domain": "AE", "Variable": "AETERM", "Order": 1,
            "Display Label": "Adverse Event Term",
            "CRF Instructions": "Report the term for the adverse event.",
            "Type": "Char", "CT Values": None, "CT Codes": None,
            "Implementation Notes": "If the event is serious, this is a very long implementation note that is definitely longer than sixty characters to ensure that the footnotes section is created."
        },
        {
            "Domain": "AE", "Variable": "AESEV", "Order": 2,
            "Display Label": "Severity",
            "CRF Instructions": "Report the severity of the adverse event.",
            "Type": "Char", "CT Values": "MILD; MODERATE; SEVERE", "CT Codes": None,
            "Implementation Notes": None
        },
        {
            "Domain": "AE", "Variable": "AESTDTC", "Order": 3,
            "Display Label": "Start Date",
            "CRF Instructions": "Report the start date of the adverse event.",
            "Type": "Datetime", "CT Values": None, "CT Codes": None,
            "Implementation Notes": None
        }
    ])
    mock_get_variables.return_value = mock_df

    from scripts.generate_cdash_crf import main
    with patch.object(sys, "argv", ["scripts/generate_cdash_crf.py", "--ig-version", "v2.3", "--out", str(out_dir), "--domains", "AE"]):
        main()

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
