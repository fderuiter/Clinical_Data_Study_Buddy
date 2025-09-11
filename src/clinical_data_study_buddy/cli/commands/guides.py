"""
This module provides the 'adrg' and 'sdrg' commands for the CDISC Data
Symphony CLI. These commands are used to generate Analysis Data Reviewer's
Guides (ADRG) and Study Data Reviewer's Guides (SDRG) respectively.
"""
import typer
from rich.console import Console
import pathlib
from dotenv import load_dotenv
from clinical_data_study_buddy.generators.documents.adrg_generator import ADRGGenerator
from clinical_data_study_buddy.generators.documents.sdrg_generator import SDRGGenerator

load_dotenv()
console = Console()
adrg_app = typer.Typer()
sdrg_app = typer.Typer()


@adrg_app.command("generate")
def adrg_generate(
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates an Analysis Data Reviewer's Guide (ADRG) document.

    This command uses the ADRGGenerator to create a Word document based on a
    study-specific configuration file.

    Args:
        study_config_path (pathlib.Path): Path to the study-specific config file.
        output_path (pathlib.Path): Path to the output Word document.
    """
    generator = ADRGGenerator(study_config_path)
    generator.generate(output_path)
    console.print(f"ADRG document generated at: {output_path}")



@sdrg_app.command("generate")
def sdrg_generate(
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates a Study Data Reviewer's Guide (SDRG) document.

    This command uses the SDRGGenerator to create a Word document based on a
    study-specific configuration file.

    Args:
        study_config_path (pathlib.Path): Path to the study-specific config file.
        output_path (pathlib.Path): Path to the output Word document.
    """
    generator = SDRGGenerator(study_config_path)
    generator.generate(output_path)
    console.print(f"SDRG document generated at: {output_path}")
