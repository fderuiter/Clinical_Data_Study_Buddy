import subprocess
import sys
import pandas as pd
from unittest.mock import patch
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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


@patch("scripts.generate_cdash_crf.populate_ae_from_fda")
@patch("scripts.generate_cdash_crf.get_cdashig_variables_from_api")
def test_generate_with_openfda(mock_get_variables, mock_populate_ae, tmp_path):
    out_dir = tmp_path / "out"
    # Mock for get_cdashig_variables_from_api
    mock_df = pd.DataFrame([
        {"Domain": "AE", "Variable": "AETERM", "Order": 1, "Display Label": "Adverse Event Term", "CRF Instructions": "", "Type": "Char", "CT Values": None, "CT Codes": None, "Implementation Notes": None},
    ])
    mock_get_variables.return_value = mock_df

    # Mock for populate_ae_from_fda
    mock_populate_ae.return_value = [{"reaction_term": "Headache"}, {"reaction_term": "Nausea"}]

    from scripts.generate_cdash_crf import main
    with patch.object(sys, "argv", ["scripts/generate_cdash_crf.py", "--ig-version", "v2.3", "--out", str(out_dir), "--domains", "AE", "--openfda-drug-name", "TestDrug"]):
        main()

    doc_path = out_dir / "AE_Adverse_Events_CRF.docx"
    assert doc_path.exists()

    from docx import Document
    doc = Document(doc_path)

    # Check for the new section heading
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    assert "Suggested Adverse Event Terms from OpenFDA" in headings

    # Check the content of the new table
    # There should be 3 tables now: admin, variables, fda
    assert len(doc.tables) == 3
    fda_table = doc.tables[2]
    assert fda_table.cell(0, 0).text == "Reaction Term"
    assert fda_table.cell(1, 0).text == "Headache"
    assert fda_table.cell(2, 0).text == "Nausea"
