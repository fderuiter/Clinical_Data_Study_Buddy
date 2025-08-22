import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.generate_synthetic_data import main


class TestGenerateSyntheticData(unittest.TestCase):
    @patch("scripts.generate_synthetic_data.CDISCDataSetGeneratorClient")
    def test_main(self, mock_client):
        # Mock the client's methods
        mock_instance = mock_client.return_value
        mock_instance.generate_dataset.return_value = {
            "success": True,
            "filename": "sdtm_dm_20250821_101032.csv",
            "download_url": "/download/sdtm_dm_20250821_101032.csv",
            "domain": "DM",
            "num_subjects": 50,
            "therapeutic_area": "Oncology",
            "format": "csv",
        }
        mock_instance.download_file.return_value = None

        # Create a temporary output directory
        output_dir = "test_output"
        os.makedirs(output_dir, exist_ok=True)

        # Call the main function with test arguments
        test_args = [
            "scripts/generate_synthetic_data.py",
            "--dataset-type",
            "SDTM",
            "--domain",
            "DM",
            "--num-subjects",
            "50",
            "--therapeutic-area",
            "Oncology",
            "--format",
            "csv",
            "--output-dir",
            output_dir,
        ]
        with patch("sys.argv", test_args):
            main()

        # Assert that the client's methods were called with the correct arguments
        mock_instance.generate_dataset.assert_called_once_with(
            dataset_type="SDTM",
            domain="DM",
            num_subjects=50,
            therapeutic_area="Oncology",
            format="csv",
        )
        mock_instance.download_file.assert_called_once_with(
            "/download/sdtm_dm_20250821_101032.csv",
            os.path.join(output_dir, "sdtm_dm_20250821_101032.csv"),
        )

        # Create a dummy file to be "downloaded"
        downloaded_file_path = os.path.join(output_dir, "sdtm_dm_20250821_101032.csv")
        with open(downloaded_file_path, "w") as f:
            f.write("dummy content")

        # Clean up the temporary directory
        os.remove(downloaded_file_path)
        os.rmdir(output_dir)


if __name__ == "__main__":
    unittest.main()
