import typer
from rich.console import Console
import pathlib
from dotenv import load_dotenv
import sys
from cdisc_generators_api.core import download_service

load_dotenv()
console = Console()
download_app = typer.Typer()


@download_app.command()
def standard(
    standard: str = typer.Option(..., "--standard", "-s", help="The standard to download (e.g., sdtmig, adamig)."),
    version: str = typer.Option(..., "--version", "-v", help="The version of the standard (e.g., 3-3)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", "-o", help="The directory to save the downloaded files.")
):
    """
    Download a CDISC data standard from the CDISC Library.
    """
    console.print(f"Downloading {standard} version {version} to {output_dir}...")
    try:
        download_service.download_standard(standard, version, output_dir)
        console.print("✅  Download complete.")
    except Exception as e:
        console.print(f"ERROR: {e}", style="bold red")
        sys.exit(1)
