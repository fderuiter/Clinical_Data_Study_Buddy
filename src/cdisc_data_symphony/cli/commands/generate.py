import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
from cdisc_data_symphony.core import generation_service

load_dotenv()
console = Console()
generate_app = typer.Typer()


@generate_app.command()
def tfl_shell(
    spec: str = typer.Option(..., "--spec", help="TFL specification"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates a TFL shell document.
    """
    try:
        generation_service.generate_tfl_shell(spec, output_file)
        console.print(f"Successfully generated TFL shell in {output_file}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def sas_code(
    dataset: str = typer.Option(..., "--dataset", help="Source dataset (e.g., ADSL)"),
    output_type: str = typer.Option(..., "--output-type", help="Type of analysis output (e.g., Demographics)"),
    treatment_var: str = typer.Option(..., "--treatment-var", help="Treatment variable (e.g., TRT01A)"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates analysis code in SAS.
    """
    try:
        generation_service.generate_sas_code(dataset, output_type, treatment_var, output_file)
        console.print(f"Successfully generated SAS code in {output_file}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def edc_raw_dataset_package(
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects (10-200)"),
    therapeutic_area: str = typer.Option("Oncology", "--therapeutic-area", help="Therapeutic area for the study"),
    domains: List[str] = typer.Option(..., "--domains", help="List of domains to include (e.g., DM AE VS LB)"),
    study_story: str = typer.Option("none", "--study-story", help="Study story to simulate (none, high_dropout)"),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the generated package"),
    output_format: str = typer.Option("csv", "--output-format", help="Output format for datasets (csv, json, xpt)")
):
    """
    Generate an EDC Raw Dataset Package.
    """
    try:
        generation_service.generate_edc_raw_dataset_package(
            num_subjects, therapeutic_area, domains, study_story, output_dir, output_format
        )
        console.print(f"EDC Raw Dataset Package generated successfully in {output_dir}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def synthetic_data(
    standard: str = typer.Option(..., "--standard", help="The standard to generate data for (e.g., sdtmig)."),
    version: str = typer.Option(..., "--version", help="The version of the standard (e.g., 3-3)."),
    domain: str = typer.Option(..., "--domain", help="The domain to generate data for (e.g., DM)."),
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the file."),
):
    """
    Generate synthetic CDISC datasets.
    """
    try:
        file_path = generation_service.generate_synthetic_data(
            standard, version, domain, num_subjects, output_dir
        )
        console.print(f"✅  Saved dataset -> {file_path}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def analysis_code(
    language: str = typer.Option(..., "--language", help="Language for the generated code (sas or r)"),
    dataset: str = typer.Option(..., "--dataset", help="Source dataset (e.g., ADSL)"),
    output_type: str = typer.Option(..., "--output-type", help="Type of analysis output (e.g., Demographics)"),
    treatment_var: str = typer.Option(..., "--treatment-var", help="Treatment variable (e.g., TRT01A)"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates analysis code in SAS or R.
    """
    try:
        generation_service.generate_analysis_code(language, dataset, output_type, treatment_var, output_file)
        console.print(f"Successfully generated {language.upper()} code in {output_file}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def cdash_crf(
    ig_version: str = typer.Option(
        ..., "--ig-version", help="CDASHIG version (e.g., v2.3)"
    ),
    out_dir: pathlib.Path = typer.Option(
        "crfs", "--out", help="Directory for generated Word documents"
    ),
    domains: Optional[List[str]] = typer.Option(
        None, "--domains", help="Optional domain whitelist (e.g. AE CM VS)"
    ),
    config_path: pathlib.Path = typer.Option(
        "crf_config.yaml", "--config", help="Path to the configuration file."
    ),
    openfda_drug_name: Optional[str] = typer.Option(
        None, "--openfda-drug-name", help="Drug name to fetch adverse events from OpenFDA."
    ),
    openfda_max_results: int = typer.Option(
        20, "--openfda-max-results", help="Max adverse events to fetch from OpenFDA."
    ),
):
    """
    Generate Word CRF shells from CDISC Library API.
    """
    try:
        generation_service.generate_cdash_crf(
            ig_version, out_dir, domains, config_path, openfda_drug_name, openfda_max_results
        )
        console.print("CDASH CRF generated successfully.")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def study_protocols(
    therapeutic_area: str = typer.Option(..., "--therapeutic-area", help="The therapeutic area of the study."),
    treatment_arms: List[str] = typer.Option(..., "--treatment-arm", help="A treatment arm of the study. Can be specified multiple times."),
    duration_weeks: int = typer.Option(..., "--duration-weeks", help="The duration of the study in weeks."),
    phase: int = typer.Option(..., "--phase", help="The phase of the study."),
    output_dir: pathlib.Path = typer.Option("my_protocol", "--output-dir", help="The directory to save the generated protocol documents.")
):
    """
    Generates a study protocol.
    """
    try:
        generation_service.generate_study_protocols(
            therapeutic_area, treatment_arms, duration_weeks, phase, output_dir
        )
        console.print(f"Protocol documents generated in {output_dir}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@generate_app.command()
def specification_templates(
    product: str = typer.Option(..., "--product", help="The CDISC product (e.g., sdtmig, adamig)."),
    version: str = typer.Option(..., "--version", help="The version of the product (e.g., 3-3)."),
    domains: List[str] = typer.Option(..., "--domains", help="A list of domains to include in the specification (e.g., DM AE VS)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="The directory to save the generated Excel file.")
):
    """
    Generate Excel-based specification templates for CDISC datasets.
    """
    try:
        generation_service.generate_specification_templates(product, version, domains, output_dir)
        console.print("Specification templates generated successfully.")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
