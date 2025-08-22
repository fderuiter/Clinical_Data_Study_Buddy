import click
import yaml
from rich.console import Console
import os
from pydantic import ValidationError

from . import __version__
from .exporter.registry import get as get_exporter
from cdisc_library_client.harvest import harvest
from protogen.protocol import StudyProtocol, generate_protocol_markdown
from src.tfl.models import TFLSpec
from src.tfl.migration import migrate_spec, TFLSpecMigrationError


console = Console()


@click.group()
@click.version_option(__version__)
def app():
    ...

@app.command()
@click.option(
    "--api-key",
    envvar="CDISC_API_KEY",
    help="CDISC Library API key",
    required=True,
)
@click.option(
    "--ig-filter",
    help="Filter IG by name",
)
@click.option(
    "-c",
    "--cache",
    "cache_path",
    help="Cache path",
    type=click.Path(dir_okay=False, writable=True),
)
@click.option(
    "-s",
    "--style",
    "style_path",
    help="Style path",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.option(
    "-t",
    "--template",
    "template_path",
    help="Template path",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.option(
    "-l",
    "--log",
    "log_path",
    help="Log file path",
    type=click.Path(dir_okay=False, writable=True),
)
@click.argument("output_path", type=click.Path(dir_okay=False, writable=True))
@click.argument("standard")
@click.argument("version")
@click.argument("domains", nargs=-1)
def generate(
    api_key: str,
    ig_filter: str,
    cache_path: str,
    style_path: str,
    template_path: str,
    log_path: str,
    output_path: str,
    standard: str,
    version: str,
    domains: list[str],
):
    """
    Generate CRF from a CDISC standard
    """
    crf = harvest(api_key, ig_filter)
    exporter = get_exporter(output_path, style_path, template_path)
    if exporter:
        with console.status(f"Exporting to {output_path}..."):
            exporter.export(crf)
        console.log(f"Exported to {output_path}")
    else:
        console.log("No exporter found, skipping exporting.")

@app.command()
@click.option("--therapeutic-area", required=True, help="Therapeutic area of the study.")
@click.option("--treatment-arm", multiple=True, help="A treatment arm of the study. Can be specified multiple times.")
@click.option("--duration-weeks", required=True, type=int, help="Duration of the study in weeks.")
@click.option("--phase", required=True, type=int, help="Phase of the study.")
@click.option("--output-dir", default="output", help="Output directory for the protocol documents.")
def protocol(therapeutic_area: str, treatment_arm: list[str], duration_weeks: int, phase: int, output_dir: str):
    """
    Generate a study protocol document.
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


@app.command()
@click.argument("spec_path", type=click.Path(exists=True, dir_okay=False, readable=True))
def spec(spec_path: str):
    """
    Validate a TFL spec file.
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
        raise click.Abort()


def main():
    app()

if __name__ == "__main__":
    main()
