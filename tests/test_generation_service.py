from unittest.mock import patch

import pandas as pd
import pytest

from clinical_data_study_buddy.core.generation_service import generate_cdash_crf


@patch("clinical_data_study_buddy.core.generation_service.load_ig")
@patch("clinical_data_study_buddy.core.generation_service.build_domain_crf")
def test_generate_cdash_crf_with_directory_as_config(
    mock_build_domain_crf, mock_load_ig, tmp_path
):
    """
    Test that generate_cdash_crf handles the case where config_path is a directory.
    It should not raise IsADirectoryError.
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
            openfda_max_results=0,
        )
    except IsADirectoryError:
        pytest.fail("generate_cdash_crf raised IsADirectoryError unexpectedly.")
