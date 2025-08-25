"""
Core module for the analysis generator.
"""
from . import r_templates, sas_templates


class AnalysisGenerator:
    """
    A class to generate analysis code in SAS and R.
    """
    def __init__(self, language, dataset, output_type, treatment_var):
        self.language = language
        self.dataset = dataset
        self.output_type = output_type
        self.treatment_var = treatment_var

    def generate_code(self):
        """
        Generates the analysis code.
        """
        if self.language.lower() == 'sas':
            return self._generate_sas_code()
        elif self.language.lower() == 'r':
            return self._generate_r_code()
        else:
            raise ValueError("Unsupported language. Please choose 'sas' or 'r'.")

    def _generate_sas_code(self):
        """
        Generates SAS code.
        """
        if self.output_type.lower() == 'demographics':
            return sas_templates.DEMO_TABLE_TEMPLATE.format(
                dataset=self.dataset,
                treatment_var=self.treatment_var
            )
        else:
            return "/* SAS code for this output type is not yet implemented. */"

    def _generate_r_code(self):
        """
        Generates R code.
        """
        if self.output_type.lower() == 'demographics':
            return r_templates.DEMO_TABLE_TEMPLATE.format(
                dataset=self.dataset,
                treatment_var=self.treatment_var
            )
        else:
            return "# R code for this output type is not yet implemented."
