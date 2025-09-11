import pytest
import pandas as pd
from pathlib import Path
from unittest.mock import patch
from clinical_data_study_buddy.generators.dataset_helpers import apply_study_story

@pytest.fixture
def temp_dataset_dir(tmp_path):
    """
    Creates a temporary directory with dummy dataset files.
    """
    dm_data = {"USUBJID": [f"SUBJ-{i}" for i in range(10)]}
    ae_data = {"USUBJID": [f"SUBJ-{i}" for i in range(10)], "AETERM": [f"Event-{i}" for i in range(10)]}

    dm_df = pd.DataFrame(dm_data)
    ae_df = pd.DataFrame(ae_data)

    dm_file = tmp_path / "sdtm_dm.csv"
    ae_file = tmp_path / "sdtm_ae.csv"

    dm_df.to_csv(dm_file, index=False)
    ae_df.to_csv(ae_file, index=False)

    return tmp_path

def test_apply_study_story_high_dropout(temp_dataset_dir):
    """
    Test that the 'high_dropout' story correctly removes subjects from datasets.
    """
    num_subjects = 10
    domains = ["DM", "AE"]

    apply_study_story("high_dropout", temp_dataset_dir, num_subjects, domains, "csv")

    # Check that AE domain has fewer subjects
    ae_df = pd.read_csv(temp_dataset_dir / "sdtm_ae.csv")
    assert len(ae_df) < num_subjects

    # Check that DM domain is unchanged
    dm_df = pd.read_csv(temp_dataset_dir / "sdtm_dm.csv")
    assert len(dm_df) == num_subjects

@patch('clinical_data_study_buddy.generators.dataset_helpers.console.print')
def test_apply_study_story_no_dm_file(mock_print, tmp_path):
    """
    Test that a warning is printed when the DM domain file is not found.
    """
    apply_study_story("high_dropout", tmp_path, 10, ["AE"], "csv")
    mock_print.assert_called_with("Warning: DM domain not found. Cannot apply high dropout story.", style="yellow")

@patch('clinical_data_study_buddy.generators.dataset_helpers.console.print')
def test_apply_study_story_unsupported_format(mock_print, temp_dataset_dir):
    """
    Test that a warning is printed for unsupported file formats.
    """
    dm_df = pd.read_csv(temp_dataset_dir / "sdtm_dm.csv") # to ensure the function proceeds
    apply_study_story("high_dropout", temp_dataset_dir, 10, ["DM", "AE"], "sas7bdat")
    mock_print.assert_called_with("Warning: High dropout story not implemented for 'sas7bdat' format yet.", style="yellow")
