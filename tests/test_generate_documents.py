import os
import sys
import json
import unittest

from cdisc_generators.adrg import generate_adrg
from cdisc_generators.sdrg import generate_sdrg

class TestGenerateDocuments(unittest.TestCase):
    def setUp(self):
        # Create dummy input files
        self.crf_data = {
            "sdtm": {
                "datasets": [
                    {"name": "DM", "label": "Demographics"},
                    {"name": "AE", "label": "Adverse Events"}
                ]
            },
            "adam": {
                "datasets": [
                    {"name": "ADSL", "label": "Subject-Level Analysis Dataset"},
                    {"name": "ADAE", "label": "Adverse Event Analysis Dataset"}
                ]
            }
        }
        self.study_config = {
            "study_id": "ABC-123",
            "protocol_id": "XYZ-001",
            "protocol_title": "A Study to Evaluate the Efficacy and Safety of a New Drug"
        }

        with open("test_crf.json", "w") as f:
            json.dump(self.crf_data, f)
        with open("test_study_config.json", "w") as f:
            json.dump(self.study_config, f)

    def tearDown(self):
        # Clean up dummy files
        if os.path.exists("test_crf.json"):
            os.remove("test_crf.json")
        if os.path.exists("test_study_config.json"):
            os.remove("test_study_config.json")
        if os.path.exists("test_adrg.docx"):
            os.remove("test_adrg.docx")
        if os.path.exists("test_sdrg.docx"):
            os.remove("test_sdrg.docx")

    def test_generate_adrg(self):
        """
        Test that the generate_adrg function creates a docx file.
        """
        output_path = "test_adrg.docx"
        generate_adrg("test_crf.json", "test_study_config.json", output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_generate_sdrg(self):
        """
        Test that the generate_sdrg function creates a docx file.
        """
        output_path = "test_sdrg.docx"
        generate_sdrg("test_crf.json", "test_study_config.json", output_path)
        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()
