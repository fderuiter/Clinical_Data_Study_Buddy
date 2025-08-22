import unittest
import sys
import os

# Add src to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from analysisgen.generator import AnalysisGenerator

class TestAnalysisGenerator(unittest.TestCase):

    def test_generate_sas_code(self):
        """
        Test SAS code generation for demographics.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADSL',
            output_type='demographics',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn('proc freq data=ADSL;', code)
        self.assertIn('tables TRT01A*sex / nocol nopercent;', code)
        self.assertIn('class TRT01A;', code)
        self.assertIn('var age;', code)

    def test_generate_r_code(self):
        """
        Test R code generation for demographics.
        """
        generator = AnalysisGenerator(
            language='r',
            dataset='ADSL',
            output_type='demographics',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn("library(tidyverse)", code)
        self.assertIn("data <- read.csv(\"ADSL.csv\")", code)
        self.assertIn("group_by(TRT01A, SEX)", code)
        self.assertIn("group_by(TRT01A)", code)
        self.assertIn("summarise(", code)

    def test_unsupported_language(self):
        """
        Test that an unsupported language raises a ValueError.
        """
        with self.assertRaises(ValueError):
            generator = AnalysisGenerator(
                language='python',
                dataset='ADSL',
                output_type='demographics',
                treatment_var='TRT01A'
            )
            generator.generate_code()

if __name__ == '__main__':
    unittest.main()
