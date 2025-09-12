import unittest
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
import pandas as pd
from clinical_data_study_buddy.core.generation_service import generate_cdash_crf

class TestGenerateCdashCrf(unittest.TestCase):
    @patch("clinical_data_study_buddy.core.generation_service.build_domain_crf")
    @patch("clinical_data_study_buddy.core.generation_service.load_ig")
    @patch("clinical_data_study_buddy.core.generation_service.populate_ae_from_fda")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.mkdir")
    def test_generate_cdash_crf_basic(
        self, mock_mkdir, mock_safe_load, mock_populate, mock_load_ig, mock_build_crf
    ):
        # Arrange
        ig_version = "v2.3"
        out_dir = Path("test_crf_output")
        domains = ["AE", "VS"]
        config_path = Path("crf_config.yaml")
        openfda_drug_name = None
        openfda_max_results = 20

        mock_ig_df = pd.DataFrame({
            "Domain": ["AE", "VS", "DM"],
            "Question": ["Adverse Event", "Vital Signs", "Demographics"],
        })
        mock_load_ig.return_value = mock_ig_df

        # Act
        with patch("builtins.open", mock_open(read_data="key: value")) as mock_file:
            with patch("pathlib.Path.is_file", return_value=True):
                 generate_cdash_crf(
                    ig_version, out_dir, domains, config_path, openfda_drug_name, openfda_max_results
                )

        # Assert
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_safe_load.assert_called_once()
        mock_populate.assert_not_called()
        self.assertEqual(mock_build_crf.call_count, 2)

    @patch("clinical_data_study_buddy.core.generation_service.build_domain_crf")
    @patch("clinical_data_study_buddy.core.generation_service.load_ig")
    @patch("clinical_data_study_buddy.core.generation_service.populate_ae_from_fda")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.mkdir")
    def test_generate_cdash_crf_with_openfda(
        self, mock_mkdir, mock_safe_load, mock_populate, mock_load_ig, mock_build_crf
    ):
        # Arrange
        ig_version = "v2.3"
        out_dir = Path("test_crf_output")
        domains = ["AE"]
        config_path = Path("crf_config.yaml")
        openfda_drug_name = "Aspirin"
        openfda_max_results = 10

        mock_ig_df = pd.DataFrame({
            "Domain": ["AE", "VS", "DM"],
            "Question": ["Adverse Event", "Vital Signs", "Demographics"],
        })
        mock_load_ig.return_value = mock_ig_df
        mock_populate.return_value = ["Headache", "Nausea"]

        # Act
        with patch("builtins.open", mock_open(read_data="key: value")) as mock_file:
             with patch("pathlib.Path.is_file", return_value=True):
                generate_cdash_crf(
                    ig_version, out_dir, domains, config_path, openfda_drug_name, openfda_max_results
                )

        # Assert
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_safe_load.assert_called_once()
        mock_populate.assert_called_once_with(openfda_drug_name, max_results=openfda_max_results)
        mock_build_crf.assert_called_once()

if __name__ == "__main__":
    unittest.main()
