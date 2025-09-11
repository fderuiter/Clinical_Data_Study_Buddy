"""
This module provides the 'build' command for the Clinical Data Study Buddy CLI.

The build command is used to fetch canonical CRF data from the CDISC Library
and to generate various CRF artifacts from a canonical JSON file.
"""
import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
import json
import sys
from cdisc_library_client.harvest import harvest
from clinical_data_study_buddy.generators.crfgen.utils import get_api_key
import clinical_data_study_buddy.generators.crfgen.exporter.csv  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.docx  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.latex  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.pdf  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.rtf  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.markdown  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.odm  # noqa
import clinical_data_study_buddy.generators.crfgen.exporter.xlsx  # noqa
from clinical_data_study_buddy.generators.crfgen.exporter import registry as reg
from clinical_data_study_buddy.core.models.schema import Form

load_dotenv()
console = Console()
build_app = typer.Typer()


@build_app.command()
def build_canonical(
    out: pathlib.Path = typer.Option("crf.json", "--out", "-o", help="Output file path"),
    version: Optional[str] = typer.Option(None, "--version", "-v", help="IG version substring (optional)")
):
    """
    Fetches canonical CRF data from the CDISC Library and saves it as a JSON file.

    This command connects to the CDISC Library API, harvests the CRF data for a
    specified Implementation Guide (IG) version, and then saves the data in a
    structured JSON format.

    Args:
        out (pathlib.Path): The path where the output JSON file will be saved.
        version (Optional[str]): An optional version string to filter the IG.
    """
    try:
        api_key = get_api_key()
    except ValueError as e:
        console.print(f"ERROR: {e}", style="bold red")
        sys.exit(1)

    console.print("Harvesting CRF data from CDISC Library...")
    forms = harvest(api_key, ig_filter=version)
    with open(out, "w") as f:
        json.dump([f.to_dict() for f in forms], f, indent=2)
    console.print(f"✅  Saved {len(forms)} forms -> {out}")


@build_app.command()
def build(
    source: pathlib.Path = typer.Option("crf.json", "--source", "-s", help="Path to the canonical JSON"),
    outdir: pathlib.Path = typer.Option("artefacts", "--outdir", "-o", help="Directory to emit artifacts"),
    formats: Optional[List[str]] = typer.Option(None, "--formats", "-f", help="Which formats to generate")
):
    """
    Generates various CRF artifacts from a canonical CRF JSON file.

    This command reads a canonical JSON file containing CRF data and then uses
    registered exporters to generate artifacts in various formats like DOCX,
    PDF, CSV, etc.

    Args:
        source (pathlib.Path): The path to the source canonical JSON file.
        outdir (pathlib.Path): The directory where the generated artifacts will be saved.
        formats (Optional[List[str]]): A list of specific formats to generate.
                                       If not provided, all registered formats
                                       will be generated.
    """
    if not source.exists():
        console.print(f"ERROR: source file not found: {source}", style="bold red")
        sys.exit(1)

    with source.open() as fp:
        data = json.load(fp)
    forms = [Form(**d) for d in data]

    outdir.mkdir(parents=True, exist_ok=True)

    if not formats:
        formats = reg.formats()

    for fmt in formats:
        fn = reg.get(fmt)
        console.print(f"[build] Rendering {fmt} → {outdir}")
        fn(forms, outdir)
