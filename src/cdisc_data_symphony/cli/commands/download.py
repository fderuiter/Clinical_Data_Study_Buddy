"""
This module provides the 'download' command for the CDISC Data Symphony CLI.

The download command is used to fetch and save various CDISC standards from the
CDISC Library.
"""
import typer
from rich.console import Console
import pathlib
from dotenv import load_dotenv
import sys
from cdisc_data_symphony.core import download_service

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
    Downloads a specified CDISC data standard from the CDISC Library.

    This command calls the download service to fetch the specified standard
    and version, saving it to the designated output directory.

    Args:
        standard (str): The name of the standard to download (e.g., "sdtmig").
        version (str): The version of the standard to download.
        output_dir (pathlib.Path): The directory where the downloaded standard
                                   will be saved.
    """
    console.print(f"Downloading {standard} version {version} to {output_dir}...")
    try:
        download_service.download_standard(standard, version, output_dir)
        console.print("✅  Download complete.")
    except Exception as e:
        console.print(f"ERROR: {e}", style="bold red")
        sys.exit(1)
