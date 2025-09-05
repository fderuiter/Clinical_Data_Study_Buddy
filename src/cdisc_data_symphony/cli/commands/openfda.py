import typer
from rich.console import Console
from dotenv import load_dotenv
from cdisc_data_symphony.generators.openfda import populate_crf

load_dotenv()
console = Console()
openfda_app = typer.Typer()


@openfda_app.command("populate-crf")
def openfda_populate_crf(
    drug_name: str = typer.Option(..., "--drug-name", help="The name of the drug to search for."),
    domain: str = typer.Option(..., "--domain", help="The domain to populate (AE or LABEL)."),
    max_results: int = typer.Option(10, "--max-results", help="The maximum number of records to return (for AE domain)."),
    start_date: str = typer.Option(None, "--start-date", help="Start date for filtering (YYYYMMDD)."),
    end_date: str = typer.Option(None, "--end-date", help="End date for filtering (YYYYMMDD)."),
    output_format: str = typer.Option("csv", "--output-format", help="The output format (csv or json).")
):
    """
    Populate CRF data from openFDA.
    """
    populate_crf(drug_name, domain, max_results, start_date, end_date, output_format)
