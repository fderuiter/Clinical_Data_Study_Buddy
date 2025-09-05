import typer
from rich.console import Console
import pathlib
from dotenv import load_dotenv
from cdisc_data_symphony.builder.spec import generate_dataset, validate

load_dotenv()
console = Console()
spec_app = typer.Typer()


@spec_app.command("generate-dataset")
def spec_generate_dataset(
    spec_file: pathlib.Path = typer.Option(..., "--spec-file", help="Path to the Excel specification file (e.g., sdtmig_3-3_spec.xlsx)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="The directory to save the generated dataset files.")
):
    """
    Generate a synthetic dataset from an Excel specification file.
    """
    generate_dataset(str(spec_file), str(output_dir))

@spec_app.command("validate")
def spec_validate(
    spec_file: pathlib.Path = typer.Option(..., "--spec-file", help="Path to the Excel specification file."),
    dataset_file: pathlib.Path = typer.Option(..., "--dataset-file", help="Path to the dataset file (e.g., a CSV).")
):
    """
    Validate a dataset against an Excel specification file.
    """
    validate(str(spec_file), str(dataset_file))
