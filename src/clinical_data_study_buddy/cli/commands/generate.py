"""
This module provides the 'generate' command for the Clinical Data Study Buddy CLI.

The generate command is a subcommand that groups together various generation
capabilities, such as creating TFL shells, synthetic data, analysis code,
and more.
"""
import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
from clinical_data_study_buddy.core import generation_service

load_dotenv()
console = Console()
generate_app = typer.Typer()


def validate_num_subjects(value: int):
    """
    A callback function for Typer to validate the number of subjects.

    This function ensures that the provided number of subjects is within the
    allowed range of 10 to 200.

    Args:
        value (int): The number of subjects to validate.

    Returns:
        int: The validated number of subjects.

    Raises:
        typer.BadParameter: If the number of subjects is outside the allowed range.
    """
    if value < 10 or value > 200:
        raise typer.BadParameter("Number of subjects must be between 10 and 200")
    return value


@generate_app.command()
def tfl_shell(
    spec: str = typer.Option(..., "--spec", help="TFL specification"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates a TFL (Tables, Figures, and Listings) shell document.

    This command calls the generation service to create a TFL shell document
    based on a given specification.

    Args:
        spec (str): The TFL specification.
        output_file (pathlib.Path): The path to the output file where the shell
                                    document will be saved.
    """
    try:
        generation_service.generate_tfl_shell(spec, output_file)
        console.print(f"Successfully generated TFL shell in {output_file}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


@generate_app.command()
def edc_raw_dataset_package(
    num_subjects: int = typer.Option(
        50, "--num-subjects", help="Number of subjects (10-200)", callback=validate_num_subjects
    ),
    therapeutic_area: str = typer.Option("Oncology", "--therapeutic-area", help="Therapeutic area for the study"),
    domains: List[str] = typer.Option(..., "--domains", help="List of domains to include (e.g., DM AE VS LB)"),
    study_story: str = typer.Option("none", "--study-story", help="Study story to simulate (none, high_dropout)"),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the generated package"),
    output_format: str = typer.Option("csv", "--output-format", help="Output format for datasets (csv, json, xpt)")
):
    """
    Generates an EDC (Electronic Data Capture) Raw Dataset Package.

    This command calls the generation service to create a complete package of
    synthetic datasets for a simulated study.

    Args:
        num_subjects (int): The number of subjects for the study.
        therapeutic_area (str): The therapeutic area for the study.
        domains (List[str]): A list of domains to include.
        study_story (str): The study story to simulate (e.g., "high_dropout").
        output_dir (pathlib.Path): The directory to save the generated package.
        output_format (str): The output format for the datasets (e.g., "csv").
    """
    try:
        generation_service.generate_edc_raw_dataset_package(
            num_subjects, therapeutic_area, domains, study_story, output_dir, output_format
        )
        console.print(f"EDC Raw Dataset Package generated successfully in {output_dir}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


@generate_app.command()
def synthetic_data(
    standard: str = typer.Option(..., "--standard", help="The standard to generate data for (e.g., sdtmig)."),
    version: str = typer.Option(..., "--version", help="The version of the standard (e.g., 3-3)."),
    domain: str = typer.Option(..., "--domain", help="The domain to generate data for (e.g., DM)."),
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the file."),
):
    """
    Generates synthetic CDISC datasets for a specific domain.

    This command calls the generation service to create a synthetic dataset
    based on a given CDISC standard, version, and domain.

    Args:
        standard (str): The standard to generate data for (e.g., "sdtmig").
        version (str): The version of the standard.
        domain (str): The domain to generate data for (e.g., "DM").
        num_subjects (int): The number of subjects.
        output_dir (pathlib.Path): The directory where the generated file will be saved.
    """
    try:
        file_path = generation_service.generate_synthetic_data(
            standard, version, domain, num_subjects, output_dir
        )
        console.print(f"✅  Saved dataset -> {file_path}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


@generate_app.command()
def analysis_code(
    language: str = typer.Option(..., "--language", help="Language for the generated code (sas or r)"),
    dataset: str = typer.Option(..., "--dataset", help="Source dataset (e.g., ADSL)"),
    output_type: str = typer.Option(..., "--output-type", help="Type of analysis output (e.g., Demographics)"),
    treatment_var: str = typer.Option(..., "--treatment-var", help="Treatment variable (e.g., TRT01A)"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates analysis code in SAS or R for a specific analysis.

    This command calls the generation service to create analysis code based on
    the specified language, dataset, and analysis type.

    Args:
        language (str): The language for the generated code ("sas" or "r").
        dataset (str): The source dataset (e.g., "ADSL").
        output_type (str): The type of analysis output (e.g., "Demographics").
        treatment_var (str): The treatment variable (e.g., "TRT01A").
        output_file (pathlib.Path): The path to the output file where the code
                                    will be saved.
    """
    try:
        generation_service.generate_analysis_code(language, dataset, output_type, treatment_var, output_file)
        console.print(f"Successfully generated {language.upper()} code in {output_file}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


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
    Generates Word CRF (Case Report Form) shells from the CDISC Library API.

    This command calls the generation service to create Word documents for
    CDASH-compliant CRFs, with an option to populate adverse event terms
    from OpenFDA.

    Args:
        ig_version (str): The CDASHIG version (e.g., "v2.3").
        out_dir (pathlib.Path): The directory for the generated Word documents.
        domains (Optional[List[str]]): An optional whitelist of domains.
        config_path (pathlib.Path): The path to the configuration file.
        openfda_drug_name (Optional[str]): Drug name to fetch AEs from OpenFDA.
        openfda_max_results (int): Max AEs to fetch from OpenFDA.
    """
    try:
        generation_service.generate_cdash_crf(
            ig_version, out_dir, domains, config_path, openfda_drug_name, openfda_max_results
        )
        console.print("CDASH CRF generated successfully.")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


@generate_app.command()
def study_protocols(
    therapeutic_area: str = typer.Option(..., "--therapeutic-area", help="The therapeutic area of the study."),
    treatment_arms: List[str] = typer.Option(..., "--treatment-arm", help="A treatment arm of the study. Can be specified multiple times."),
    duration_weeks: int = typer.Option(..., "--duration-weeks", help="The duration of the study in weeks."),
    phase: int = typer.Option(..., "--phase", help="The phase of the study."),
    output_dir: pathlib.Path = typer.Option("my_protocol", "--output-dir", help="The directory to save the generated protocol documents.")
):
    """
    Generates study protocol documents.

    This command calls the generation service to create study protocol
    documents based on the provided study parameters.

    Args:
        therapeutic_area (str): The therapeutic area of the study.
        treatment_arms (List[str]): A list of treatment arms for the study.
        duration_weeks (int): The duration of the study in weeks.
        phase (int): The phase of the study.
        output_dir (pathlib.Path): The directory to save the generated documents.
    """
    try:
        generation_service.generate_study_protocols(
            therapeutic_area, treatment_arms, duration_weeks, phase, output_dir
        )
        console.print(f"Protocol documents generated in {output_dir}")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)


@generate_app.command()
def specification_templates(
    product: str = typer.Option(..., "--product", help="The CDISC product (e.g., sdtmig, adamig)."),
    version: str = typer.Option(..., "--version", help="The version of the product (e.g., 3-3)."),
    domains: List[str] = typer.Option(..., "--domains", help="A list of domains to include in the specification (e.g., DM AE VS)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="The directory to save the generated Excel file.")
):
    """
    Generates Excel-based specification templates for CDISC datasets.

    This command calls the generation service to create Excel specification
    templates for a given CDISC product, version, and list of domains.

    Args:
        product (str): The CDISC product (e.g., "sdtmig", "adamig").
        version (str): The version of the product.
        domains (List[str]): A list of domains to include in the specification.
        output_dir (pathlib.Path): The directory to save the generated Excel file.
    """
    try:
        generation_service.generate_specification_templates(product, version, domains, output_dir)
        console.print("Specification templates generated successfully.")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
        raise typer.Exit(code=1)
