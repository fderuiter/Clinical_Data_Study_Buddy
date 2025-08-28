import unittest
from cdisc_generators_api.cdisc_generators.analysisgen.generator import AnalysisGenerator

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

    def test_generate_sas_code_disposition(self):
        """
        Test SAS code generation for disposition.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADSL',
            output_type='disposition',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn('proc freq data=ADSL;', code)
        self.assertIn('tables TRT01A*dcreason / nocol nopercent;', code)

    def test_generate_sas_code_exposure(self):
        """
        Test SAS code generation for exposure.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADEX',
            output_type='exposure',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn('proc means data=ADEX', code)
        self.assertIn('var CUMDOSE TRTDUR RELDOS;', code)

    def test_generate_sas_code_teae_summary(self):
        """
        Test SAS code generation for TEAE summary.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADAE',
            output_type='teae_summary',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn("where TEAEFL = 'Y';", code)
        self.assertIn("where SAEFL = 'Y';", code)
        self.assertIn("where AERELFL = 'Y';", code)
        self.assertIn("where AESEV = 'SEVERE';", code)
        self.assertIn("where AEOUT = 'FATAL';", code)

    def test_generate_sas_code_teae_by_soc_pt(self):
        """
        Test SAS code generation for TEAE by SOC and PT.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADAE',
            output_type='teae_by_soc_pt',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn("tables AEBODSYS*AEDECOD*TRT01A / nocol nopercent;", code)

    def test_generate_sas_code_lab_shift(self):
        """
        Test SAS code generation for lab shift table.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADLB',
            output_type='lab_shift',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn("tables BNTOXGR*WNTOXGR / nocol nopercent;", code)
        self.assertIn("by TRT01A PARAMCD;", code)

    def test_generate_sas_code_vs_change(self):
        """
        Test SAS code generation for vital signs change table.
        """
        generator = AnalysisGenerator(
            language='sas',
            dataset='ADVS',
            output_type='vs_change',
            treatment_var='TRT01A'
        )
        code = generator.generate_code()
        self.assertIn("class TRT01A AVISIT;", code)
        self.assertIn("var CHG;", code)
        self.assertIn("by PARAMCD;", code)

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
