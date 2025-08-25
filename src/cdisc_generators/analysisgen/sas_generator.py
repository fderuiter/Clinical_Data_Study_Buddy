class SASGenerator:
    def __init__(self, dataset, output_type, treatment_var):
        self.dataset = dataset
        self.output_type = output_type
        self.treatment_var = treatment_var

    def generate(self):
        """
        Generates a simple SAS program.
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
