import os
import zipfile
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import MagicMock, patch
from clinical_data_study_buddy.generators.dataset_helpers import (
    generate_define_xml,
    package_datasets,
    apply_study_story,
)

@pytest.fixture
def temp_dir(tmp_path):
    d = tmp_path / "temp"
    d.mkdir()
    return d

@pytest.fixture
def output_dir(tmp_path):
    d = tmp_path / "output"
    d.mkdir()
    return d

def test_generate_define_xml_no_api_key(temp_dir, monkeypatch):
    """
    Tests that generate_define_xml handles the case where CDISC_API_KEY is not set.
    """
    monkeypatch.delenv("CDISC_API_KEY", raising=False)
    generate_define_xml(temp_dir, ["DM"])
    define_xml_path = temp_dir / "define.xml"
    assert define_xml_path.exists()
    with open(define_xml_path, "r") as f:
        assert f.read() == "<ODM></ODM>"

@patch("httpx.get")
def test_generate_define_xml_success(mock_get, temp_dir, monkeypatch):
    """
    Tests that generate_define_xml successfully creates a define.xml file.
    """
    monkeypatch.setenv("CDISC_API_KEY", "test_key")
    # Create a dummy domain file
    dm_df = pd.DataFrame({"USUBJID": ["1", "2"], "BRTHDTC": ["1990-01-01", "1991-01-01"]})
    dm_file = temp_dir / "sdtm_dm.csv"
    dm_df.to_csv(dm_file, index=False)

    # Mock the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"label": "Subject ID", "datatype": "text", "length": 12}
    mock_get.return_value = mock_response

    generate_define_xml(temp_dir, ["DM"])
    define_xml_path = temp_dir / "define.xml"
    assert define_xml_path.exists()
    # A more thorough check would be to parse the XML and verify its contents
    assert define_xml_path.stat().st_size > 100

def test_package_datasets(temp_dir, output_dir):
    """
    Tests that package_datasets creates a zip file and cleans up the temp directory.
    """
    # Create some dummy files
    (temp_dir / "file1.txt").touch()
    (temp_dir / "file2.txt").touch()

    package_datasets(temp_dir, output_dir)

    zip_path = output_dir / "edc_raw_datasets.zip"
    assert zip_path.exists()
    assert not temp_dir.exists()

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        assert set(zipf.namelist()) == {"file1.txt", "file2.txt"}

def test_apply_study_story_high_dropout(temp_dir):
    """
    Tests the 'high_dropout' study story.
    """
    # Create dummy domain files
    dm_df = pd.DataFrame({"USUBJID": [f"SUBJ-{i}" for i in range(10)]})
    dm_file = temp_dir / "sdtm_dm.csv"
    dm_df.to_csv(dm_file, index=False)

    vs_df = pd.DataFrame({"USUBJID": [f"SUBJ-{i}" for i in range(10)], "VSORRES": [70 + i for i in range(10)]})
    vs_file = temp_dir / "sdtm_vs.csv"
    vs_df.to_csv(vs_file, index=False)

    apply_study_story("high_dropout", temp_dir, 10, ["DM", "VS"], "csv")

    # DM should be unchanged
    dm_df_after = pd.read_csv(dm_file)
    assert len(dm_df_after) == 10

    # VS should have fewer subjects
    vs_df_after = pd.read_csv(vs_file)
    assert len(vs_df_after) < 10
