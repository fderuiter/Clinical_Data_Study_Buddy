import pytest
from pathlib import Path
import os
import pandas as pd
import zipfile
import shutil
from unittest.mock import patch, MagicMock

from clinical_data_study_buddy.generators.dataset_helpers import (
    generate_define_xml,
    package_datasets,
    apply_study_story,
)


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for test files."""
    return tmp_path


@pytest.fixture
def setup_test_data(temp_dir):
    """Set up test data for the dataset helper functions."""
    input_dir = temp_dir / "input"
    input_dir.mkdir()

    # Create dummy data files
    dm_data = {
        "USUBJID": [f"SUBJECT-{i}" for i in range(1, 6)],
        "AGE": [25, 30, 35, 40, 45],
    }
    dm_df = pd.DataFrame(dm_data)
    dm_df.to_csv(input_dir / "sdtm_dm_test.csv", index=False)

    ae_data = {
        "USUBJID": [f"SUBJECT-{i}" for i in range(1, 6)],
        "AETERM": ["HEADACHE", "NAUSEA", "FEVER", "DIZZINESS", "FATIGUE"],
    }
    ae_df = pd.DataFrame(ae_data)
    ae_df.to_csv(input_dir / "sdtm_ae_test.csv", index=False)

    return input_dir


def test_package_datasets_creates_zip(setup_test_data, temp_dir):
    """Test that package_datasets creates a zip file."""
    output_dir = temp_dir / "output"
    output_dir.mkdir()
    package_datasets(setup_test_data, output_dir)
    zip_file = output_dir / "edc_raw_datasets.zip"
    assert zip_file.exists()


def test_package_datasets_zip_contents(setup_test_data, temp_dir):
    """Test that the zip file contains the correct files."""
    output_dir = temp_dir / "output"
    output_dir.mkdir()
    package_datasets(setup_test_data, output_dir)
    zip_file = output_dir / "edc_raw_datasets.zip"
    with zipfile.ZipFile(zip_file, "r") as zf:
        zip_contents = zf.namelist()
        assert "sdtm_dm_test.csv" in zip_contents
        assert "sdtm_ae_test.csv" in zip_contents


def test_package_datasets_cleans_temp_dir(setup_test_data, temp_dir):
    """Test that the temporary directory is removed after packaging."""
    output_dir = temp_dir / "output"
    output_dir.mkdir()
    # Create a copy of the temp_dir to check for its existence later
    temp_dir_path_str = str(setup_test_data)
    package_datasets(setup_test_data, output_dir)
    assert not os.path.exists(temp_dir_path_str)


def test_apply_study_story_high_dropout(setup_test_data):
    """Test the 'high_dropout' study story."""
    num_subjects = 5
    domains = ["DM", "AE"]
    apply_study_story("high_dropout", setup_test_data, num_subjects, domains, "csv")

    # DM should be unchanged
    dm_df = pd.read_csv(setup_test_data / "sdtm_dm_test.csv")
    assert len(dm_df) == 5

    # AE should have fewer subjects
    ae_df = pd.read_csv(setup_test_data / "sdtm_ae_test.csv")
    assert len(ae_df) < 5


def test_apply_study_story_high_dropout_dm_not_found(setup_test_data):
    """Test high_dropout story when DM domain is not found."""
    os.remove(setup_test_data / "sdtm_dm_test.csv")
    num_subjects = 5
    domains = ["DM", "AE"]
    apply_study_story("high_dropout", setup_test_data, num_subjects, domains, "csv")

    # AE should be unchanged
    ae_df = pd.read_csv(setup_test_data / "sdtm_ae_test.csv")
    assert len(ae_df) == 5


def test_apply_study_story_high_dropout_unsupported_format(setup_test_data):
    """Test high_dropout story with an unsupported file format."""
    num_subjects = 5
    domains = ["DM", "AE"]
    apply_study_story("high_dropout", setup_test_data, num_subjects, domains, "json")

    # AE should be unchanged
    ae_df = pd.read_csv(setup_test_data / "sdtm_ae_test.csv")
    assert len(ae_df) == 5


def test_apply_study_story_invalid_story(setup_test_data):
    """Test that nothing happens when an invalid story name is passed."""
    num_subjects = 5
    domains = ["DM", "AE"]
    apply_study_story("invalid_story", setup_test_data, num_subjects, domains, "csv")

    # Both files should be unchanged
    dm_df = pd.read_csv(setup_test_data / "sdtm_dm_test.csv")
    assert len(dm_df) == 5
    ae_df = pd.read_csv(setup_test_data / "sdtm_ae_test.csv")
    assert len(ae_df) == 5


@patch("httpx.get")
def test_generate_define_xml_creates_file(mock_get, setup_test_data):
    """Test that generate_define_xml creates a define.xml file."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"label": "Subject ID", "datatype": "text", "length": 10}
    mock_get.return_value = mock_response
    os.environ["CDISC_API_KEY"] = "test-key"

    domains = ["DM"]
    generate_define_xml(setup_test_data, domains)
    define_xml_path = setup_test_data / "define.xml"
    assert define_xml_path.exists()


def test_generate_define_xml_no_api_key(setup_test_data):
    """Test define.xml generation when CDISC_API_KEY is not set."""
    if "CDISC_API_KEY" in os.environ:
        del os.environ["CDISC_API_KEY"]

    domains = ["DM"]
    generate_define_xml(setup_test_data, domains)
    define_xml_path = setup_test_data / "define.xml"
    assert define_xml_path.exists()
    # Should contain an empty ODM tag
    with open(define_xml_path, "r") as f:
        content = f.read()
        assert "<ODM></ODM>" in content


@patch("httpx.get")
def test_generate_define_xml_with_mocked_api(mock_get, setup_test_data):
    """Test define.xml generation with a mocked CDISC Library API."""
    mock_responses = {
        "https://library.cdisc.org/products/sdtmig/3-3/datasets/DM/variables/USUBJID": {
            "label": "Unique Subject Identifier", "datatype": "text", "length": 20
        },
        "https://library.cdisc.org/products/sdtmig/3-3/datasets/DM/variables/AGE": {
            "label": "Age", "datatype": "integer", "length": 3
        },
    }

    def mock_get_side_effect(url, headers, timeout, follow_redirects):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_responses.get(url, {})
        return mock_response

    mock_get.side_effect = mock_get_side_effect
    os.environ["CDISC_API_KEY"] = "test-key"

    domains = ["DM"]
    generate_define_xml(setup_test_data, domains)
    define_xml_path = setup_test_data / "define.xml"
    assert define_xml_path.exists()

    with open(define_xml_path, "r") as f:
        content = f.read()
        assert 'OID="IG.DM"' in content
        assert 'OID="IT.DM.USUBJID"' in content
        assert 'OID="IT.DM.AGE"' in content
        assert "<TranslatedText xml:lang=\"en\">Unique Subject Identifier</TranslatedText>" in content
        assert "<TranslatedText xml:lang=\"en\">Age</TranslatedText>" in content
