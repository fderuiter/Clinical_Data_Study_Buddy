import typer
from rich.console import Console
import pathlib
from dotenv import load_dotenv
from cdisc_data_symphony.generators.adrg import generate_adrg
from cdisc_data_symphony.generators.sdrg import generate_sdrg

load_dotenv()
console = Console()
adrg_app = typer.Typer()
sdrg_app = typer.Typer()


@adrg_app.command("generate")
def adrg_generate(
    crf_json_path: pathlib.Path = typer.Option(..., "--crf", help="Path to the canonical crf.json file."),
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates an Analysis Data Reviewer's Guide (ADRG) document.
    """
    generate_adrg(crf_json_path, study_config_path, output_path)
    console.print(f"ADRG document generated at: {output_path}")



@sdrg_app.command("generate")
def sdrg_generate(
    crf_json_path: pathlib.Path = typer.Option(..., "--crf", help="Path to the canonical crf.json file."),
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates a Study Data Reviewer's Guide (SDRG) document.
    """
    generate_sdrg(crf_json_path, study_config_path, output_path)
    console.print(f"SDRG document generated at: {output_path}")
