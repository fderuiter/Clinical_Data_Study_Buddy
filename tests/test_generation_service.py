import pytest
import pathlib
from unittest.mock import patch, MagicMock
import pandas as pd
from clinical_data_study_buddy.core.generation_service import generate_cdash_crf, generate_synthetic_data

@patch('clinical_data_study_buddy.core.generation_service.load_ig')
@patch('clinical_data_study_buddy.core.generation_service.build_domain_crf')
def test_generate_cdash_crf_with_directory_as_config(mock_build_domain_crf, mock_load_ig, tmp_path, capsys):
    """
    Test that generate_cdash_crf handles the case where config_path is a directory.
    It should not raise IsADirectoryError and should print a warning.
    """
    mock_load_ig.return_value = pd.DataFrame({"Domain": ["AE"]})
    config_dir = tmp_path / "config_dir"
    config_dir.mkdir()

    try:
        generate_cdash_crf(
            ig_version="v2.3",
            out_dir=tmp_path,
            domains=["AE"],
            config_path=config_dir,
            openfda_drug_name=None,
            openfda_max_results=0
        )
    except IsADirectoryError:
        pytest.fail("generate_cdash_crf raised IsADirectoryError unexpectedly.")

    captured = capsys.readouterr()
    assert f"Warning: Config path {config_dir} is a directory, not a file. Using default values." in captured.out


@patch('clinical_data_study_buddy.core.generation_service.load_ig')
@patch('clinical_data_study_buddy.core.generation_service.build_domain_crf')
def test_generate_cdash_crf_with_non_existent_config(mock_build_domain_crf, mock_load_ig, tmp_path, capsys):
    """
    Test that generate_cdash_crf handles a non-existent config_path.
    It should print a warning message.
    """
    mock_load_ig.return_value = pd.DataFrame({"Domain": ["AE"]})
    non_existent_config = tmp_path / "non_existent.yaml"

    generate_cdash_crf(
        ig_version="v2.3",
        out_dir=tmp_path,
        domains=["AE"],
        config_path=non_existent_config,
        openfda_drug_name=None,
        openfda_max_results=0
    )

    captured = capsys.readouterr()
    assert f"Warning: Config file not found at {non_existent_config}. Using default values." in captured.out


@patch('clinical_data_study_buddy.core.generation_service.get_api_key')
@patch('clinical_data_study_buddy.core.generation_service.harvest')
def test_generate_synthetic_data_domain_not_found(mock_harvest, mock_get_api_key, tmp_path):
    """
    Test that generate_synthetic_data raises ValueError when the domain is not found.
    """
    mock_get_api_key.return_value = "test_key"
    mock_harvest.return_value = []  # No forms returned

    with pytest.raises(ValueError, match="Domain NONEXISTENT not found in sdtmig 3-3"):
        generate_synthetic_data(
            standard="sdtmig",
            version="3-3",
            domain="NONEXISTENT",
            num_subjects=10,
            output_dir=tmp_path
        )
