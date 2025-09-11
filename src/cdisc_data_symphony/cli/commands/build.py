import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
import json
import sys
from cdisc_library_client.harvest import harvest
from cdisc_data_symphony.generators.crfgen.utils import get_api_key
import cdisc_data_symphony.generators.crfgen.exporter.csv  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.docx  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.latex  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.pdf  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.rtf  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.markdown  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.odm  # noqa
import cdisc_data_symphony.generators.crfgen.exporter.xlsx  # noqa
from cdisc_data_symphony.generators.crfgen.exporter import registry as reg
from cdisc_data_symphony.core.models.schema import Form

load_dotenv()
console = Console()
build_app = typer.Typer()


@build_app.command()
def build_canonical(
    out: pathlib.Path = typer.Option("crf.json", "--out", "-o", help="Output file path"),
    version: Optional[str] = typer.Option(None, "--version", "-v", help="IG version substring (optional)")
):
    """
    Fetch the canonical CRF data from the CDISC Library and create a canonical crf.json file.
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
    Generate all CRF artifacts from a canonical crf.json file.
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
