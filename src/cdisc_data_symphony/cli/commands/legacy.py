"""
This module defines a command-line interface (CLI) for generating various
clinical study artifacts, including CRFs, study protocols, and for validating
TFL specification files.
"""
import typer
import yaml
from rich.console import Console
import os
from pydantic import ValidationError
import pathlib
from typing import List, Optional

from cdisc_data_symphony.builder.crfgen.exporter.registry import get as get_exporter
from cdisc_data_symphony.builder.protogen.protocol import StudyProtocol, generate_protocol_markdown
from cdisc_data_symphony.builder.tfl.models import TFLSpec
from cdisc_data_symphony.builder.tfl.migration import migrate_spec, TFLSpecMigrationError


console = Console()
legacy_app = typer.Typer()


@legacy_app.command()
def generate(
    api_key: str = typer.Option(..., envvar="CDISC_API_KEY", help="CDISC Library API key"),
    ig_filter: Optional[str] = typer.Option(None, "--ig-filter", help="Filter IG by name"),
    cache_path: Optional[pathlib.Path] = typer.Option(None, "-c", "--cache", help="Cache path"),
    style_path: Optional[pathlib.Path] = typer.Option(None, "-s", "--style", help="Style path"),
    template_path: Optional[pathlib.Path] = typer.Option(None, "-t", "--template", help="Template path"),
    log_path: Optional[pathlib.Path] = typer.Option(None, "-l", "--log", help="Log file path"),
    output_path: pathlib.Path = typer.Argument(..., help="Output path"),
    standard: str = typer.Argument(..., help="CDISC standard"),
    version: str = typer.Argument(..., help="Version of the standard"),
    domains: List[str] = typer.Argument(..., help="Domains to include"),
):
    """
    Generates a CRF from a specified CDISC standard.
    """
    crf = harvest(api_key, ig_filter)
    exporter = get_exporter(str(output_path), str(style_path) if style_path else None, str(template_path) if template_path else None)
    if exporter:
        with console.status(f"Exporting to {output_path}..."):
            exporter.export(crf)
        console.log(f"Exported to {output_path}")
    else:
        console.log("No exporter found, skipping exporting.")

@legacy_app.command()
def protocol(
    therapeutic_area: str = typer.Option(..., "--therapeutic-area", help="Therapeutic area of the study."),
    treatment_arm: List[str] = typer.Option(..., "--treatment-arm", help="A treatment arm of the study. Can be specified multiple times."),
    duration_weeks: int = typer.Option(..., "--duration-weeks", help="Duration of the study in weeks."),
    phase: int = typer.Option(..., "--phase", help="Phase of the study."),
    output_dir: str = typer.Option("output", "--output-dir", help="Output directory for the protocol documents.")
):
    """
    Generates a study protocol document.
    """
    console.log(f"Generating study protocol in {output_dir}...")
    os.makedirs(output_dir, exist_ok=True)

    protocol_data = {
        "therapeutic_area": therapeutic_area,
        "treatment_arms": treatment_arm,
        "duration_weeks": duration_weeks,
        "phase": phase,
    }

    study_protocol = StudyProtocol(**protocol_data)

    output_path = generate_protocol_markdown(study_protocol, output_dir)

    console.log(f"Protocol document generated at {output_path}")


@legacy_app.command()
def spec(
    spec_path: pathlib.Path = typer.Argument(..., help="Path to the TFL specification file to validate.")
):
    """
    Validates a TFL (Tables, Figures, and Listings) specification file.
    """
    console.log(f"Validating spec file: {spec_path}")
    try:
        with open(spec_path, "r") as f:
            spec_data = yaml.safe_load(f)

        spec_data = migrate_spec(spec_data)
        TFLSpec(**spec_data)
        console.log("[green]Spec file is valid.[/green]")
    except (yaml.YAMLError, TFLSpecMigrationError, ValidationError) as e:
        console.log(f"[red]Spec file is invalid:[/red]")
        console.log(e)
        raise typer.Abort()
