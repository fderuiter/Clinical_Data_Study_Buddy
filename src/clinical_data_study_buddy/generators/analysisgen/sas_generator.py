"""
This module contains the SASGenerator class, which is responsible for
generating SAS programs for analysis.
"""


class SASGenerator:
    """
    A class for generating simple SAS programs.

    This class creates a SAS program that imports a CSV file into a SAS dataset
    and then prints the contents of that dataset.
    """

    def __init__(self, dataset, output_type, treatment_var):
        """
        Initializes the SASGenerator.

        Args:
            dataset (str): The name of the dataset to be imported (without the .csv extension).
            output_type (str): The type of analysis output (currently not used).
            treatment_var (str): The name of the treatment variable (currently not used).
        """
        self.dataset = dataset
        self.output_type = output_type
        self.treatment_var = treatment_var

    def generate(self):
        """
        Generates a simple SAS program.

        The generated program imports a CSV file into a SAS dataset and then
        prints the dataset.

        Returns:
            str: The generated SAS program as a string.
        """
        return f"""\
PROC IMPORT DATAFILE="{self.dataset}.csv"
    OUT=work.{self.dataset}
    DBMS=CSV
    REPLACE;
RUN;

PROC PRINT DATA=work.{self.dataset};
RUN;
"""
