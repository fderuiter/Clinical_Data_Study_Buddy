import os
import zipfile
from pathlib import Path
import pandas as pd
import httpx
from unittest.mock import patch, MagicMock
from clinical_data_study_buddy.generators.dataset_helpers import (
    package_datasets,
    apply_study_story,
    generate_define_xml,
)


def test_package_datasets(tmp_path):
    """
    Test that package_datasets correctly packages files into a zip archive
    and cleans up the temporary directory.
    """
    # 1. Create a temporary directory and some dummy files
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()
    (temp_dir / "file1.txt").write_text("hello")
    (temp_dir / "file2.csv").write_text("a,b,c")

    # 2. Create an output directory
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # 3. Call package_datasets
    package_datasets(temp_dir, output_dir)

    # 4. Assert that the zip file was created
    zip_filename = output_dir / "edc_raw_datasets.zip"
    assert zip_filename.exists()

    # 5. Assert that the zip file contains the correct files
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        assert set(zipf.namelist()) == {"file1.txt", "file2.csv"}

    # 6. Assert that the temporary directory was deleted
    assert not temp_dir.exists()


def test_apply_study_story_high_dropout(tmp_path):
    """
    Test that apply_study_story with 'high_dropout' correctly removes subjects
    from non-DM domains.
    """
    # 1. Create a temporary directory and dummy dataset files
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    # Create DM domain
    dm_df = pd.DataFrame({
        "USUBJID": [f"subj-{i}" for i in range(10)],
        "AGE": [i for i in range(10)]
    })
    dm_file = temp_dir / "sdtm_dm_test.csv"
    dm_df.to_csv(dm_file, index=False)

    # Create VS domain
    vs_df = pd.DataFrame({
        "USUBJID": [f"subj-{i}" for i in range(10)],
        "VSORRES": [i * 10 for i in range(10)]
    })
    vs_file = temp_dir / "sdtm_vs_test.csv"
    vs_df.to_csv(vs_file, index=False)

    # 2. Call apply_study_story
    apply_study_story(
        study_story="high_dropout",
        temp_dir=temp_dir,
        num_subjects=10,
        domains=["DM", "VS"],
        file_format="csv"
    )

    # 3. Assert that the VS domain file has been modified
    vs_df_after = pd.read_csv(vs_file)
    assert len(vs_df_after) < len(vs_df)
    # 30% dropout rate, so 3 subjects dropped
    assert len(vs_df_after) == 7

    # 4. Assert that the DM domain file has not been modified
    dm_df_after = pd.read_csv(dm_file)
    assert len(dm_df_after) == len(dm_df)


def test_generate_define_xml_no_api_key(tmp_path, monkeypatch):
    """
    Test that generate_define_xml creates an empty define.xml when
    CDISC_API_KEY is not set.
    """
    # Unset the environment variable
    monkeypatch.delenv("CDISC_API_KEY", raising=False)

    temp_dir = tmp_path
    domains = ["DM"]
    (temp_dir / "sdtm_dm_test.csv").write_text("USUBJID,AGE")

    generate_define_xml(temp_dir, domains)

    define_xml_path = temp_dir / "define.xml"
    assert define_xml_path.exists()
    with open(define_xml_path, "r") as f:
        assert f.read() == "<ODM></ODM>"


@patch("httpx.get")
def test_generate_define_xml_success(mock_get, tmp_path, monkeypatch):
    """
    Test that generate_define_xml successfully creates a define.xml file
    by fetching metadata from the CDISC Library.
    """
    # Set the environment variable
    monkeypatch.setenv("CDISC_API_KEY", "test-key")

    # Mock the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "label": "Subject Identifier for the Study",
        "datatype": "text",
        "length": 24
    }
    mock_get.return_value = mock_response

    temp_dir = tmp_path
    domains = ["DM"]
    dm_df = pd.DataFrame({"USUBJID": ["test-01"], "AGE": [42]})
    (temp_dir / "sdtm_dm_test.csv").write_text(dm_df.to_csv(index=False))

    generate_define_xml(temp_dir, domains)

    define_xml_path = temp_dir / "define.xml"
    assert define_xml_path.exists()

    # Check that the content is valid XML and contains expected elements
    with open(define_xml_path, "r") as f:
        content = f.read()
        assert "<ODM" in content
        assert 'OID="IG.DM"' in content
        assert 'OID="IT.DM.USUBJID"' in content
        assert 'OID="IT.DM.AGE"' in content


@patch("httpx.get")
def test_generate_define_xml_missing_domain_file(mock_get, tmp_path, monkeypatch):
    """
    Test that generate_define_xml skips domains for which no file exists.
    """
    monkeypatch.setenv("CDISC_API_KEY", "test-key")
    temp_dir = tmp_path
    domains = ["DM", "VS"] # VS file is missing
    (temp_dir / "sdtm_dm_test.csv").write_text("USUBJID,AGE")

    generate_define_xml(temp_dir, domains)

    define_xml_path = temp_dir / "define.xml"
    assert define_xml_path.exists()
    with open(define_xml_path, "r") as f:
        content = f.read()
        assert 'OID="IG.DM"' in content
        assert 'OID="IG.VS"' not in content # VS should not be in the output


@patch("httpx.get")
def test_generate_define_xml_api_error(mock_get, tmp_path, monkeypatch, capsys):
    """
    Test that generate_define_xml handles HTTP errors from the API gracefully.
    """
    monkeypatch.setenv("CDISC_API_KEY", "test-key")
    mock_get.side_effect = httpx.HTTPStatusError("Not Found", request=MagicMock(), response=MagicMock(status_code=404))

    temp_dir = tmp_path
    domains = ["DM"]
    dm_df = pd.DataFrame({"USUBJID": ["test-01"]})
    (temp_dir / "sdtm_dm_test.csv").write_text(dm_df.to_csv(index=False))

    generate_define_xml(temp_dir, domains)

    captured = capsys.readouterr()
    assert "Error fetching metadata for variable USUBJID in domain DM: 404" in captured.out
