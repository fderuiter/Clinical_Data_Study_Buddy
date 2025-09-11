"""
This module provides the 'openfda' command for the Clinical Data Study Buddy CLI.

The openfda command is used to interact with the OpenFDA API to populate
CRF data with information about adverse events and drug labels.
"""
import typer
from rich.console import Console
from dotenv import load_dotenv
from clinical_data_study_buddy.generators.openfda import populate_crf

load_dotenv()
console = Console()
openfda_app = typer.Typer()


@openfda_app.command("populate-crf")
def openfda_populate_crf(
    drug_name: str = typer.Option(..., "--drug-name", help="The name of the drug to search for."),
    domain: str = typer.Option(..., "--domain", help="The domain to populate (AE or LABEL)."),
    max_results: int = typer.Option(10, "--max-results", help="The maximum number of records to return (for AE domain)."),
    start_date: str = typer.Option(None, "--start-date", help="Start date for filtering (YYYY-MM-DD)."),
    end_date: str = typer.Option(None, "--end-date", help="End date for filtering (YYYY-MM-DD)."),
    output_format: str = typer.Option("csv", "--output-format", help="The output format (csv or json).")
):
    """
    Populates CRF data from OpenFDA for a given drug and domain.

    Args:
        drug_name (str): The name of the drug to search for.
        domain (str): The domain to populate (AE or LABEL).
        max_results (int): The maximum number of records to return (for AE domain).
        start_date (str): The start date for filtering (YYYY-MM-DD).
        end_date (str): The end date for filtering (YYYY-MM-DD).
        output_format (str): The output format (csv or json).
    """
    populate_crf(drug_name, domain, max_results, start_date, end_date, output_format)
