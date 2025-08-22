import unittest
from unittest.mock import patch, MagicMock
import os
import zipfile
from pathlib import Path
import pandas as pd
import sys

# Add the project root to the path to allow importing the script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.generate_raw_dataset_package import main as generate_main, apply_study_story, package_datasets

class TestGenerateRawDatasetPackage(unittest.TestCase):

    def setUp(self):
        self.output_dir = Path("test_output")
        self.temp_dir = self.output_dir / "temp_datasets"
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the created directories and files
        if os.path.exists(self.output_dir):
            import shutil
            shutil.rmtree(self.output_dir)

    @patch('scripts.generate_raw_dataset_package.CDISCDataSetGeneratorClient')
    def test_data_generation_process(self, mock_client):
        # Mock the client methods
        mock_instance = mock_client.return_value
        mock_instance.generate_dataset.return_value = {
            "download_url": "/download/sdtm_dm_123.csv",
            "filename": "sdtm_dm_123.csv"
        }

        # Run the script with mocked args
        with patch('sys.argv', ['script_name', '--num-subjects', '10', '--domains', 'DM', '--output-dir', str(self.output_dir)]):
            generate_main()

        # Assert that the client methods were called
        mock_instance.generate_dataset.assert_called_once_with(
            dataset_type="SDTM",
            domain="DM",
            num_subjects=10,
            therapeutic_area="Oncology",
            format="csv"
        )
        mock_instance.download_file.assert_called_once()

    def test_high_dropout_story(self):
        # Create some dummy data
        dm_data = {'USUBJID': [f'SUBJ-{i}' for i in range(1, 11)], 'DMVAR': range(10)}
        ae_data = {'USUBJID': [f'SUBJ-{i}' for i in range(1, 11)], 'AEVAR': range(10)}
        dm_df = pd.DataFrame(dm_data)
        ae_df = pd.DataFrame(ae_data)
        dm_df.to_csv(self.temp_dir / "sdtm_dm_test.csv", index=False)
        ae_df.to_csv(self.temp_dir / "sdtm_ae_test.csv", index=False)

        apply_study_story("high_dropout", self.temp_dir, 10, ["DM", "AE"], "csv")

        # Check that the AE file has been modified
        ae_modified_df = pd.read_csv(self.temp_dir / "sdtm_ae_test.csv")
        self.assertTrue(len(ae_modified_df) < 10)

    def test_zip_file_creation(self):
        # Create some dummy files
        (self.temp_dir / "file1.txt").touch()
        (self.temp_dir / "file2.txt").touch()

        package_datasets(self.temp_dir, self.output_dir)

        # Check that the zip file was created
        zip_file = self.output_dir / "edc_raw_datasets.zip"
        self.assertTrue(zip_file.exists())

        # Check the contents of the zip file
        with zipfile.ZipFile(zip_file, 'r') as zf:
            self.assertEqual(len(zf.namelist()), 2)
            self.assertIn("file1.txt", zf.namelist())
            self.assertIn("file2.txt", zf.namelist())

if __name__ == '__main__':
    unittest.main()
