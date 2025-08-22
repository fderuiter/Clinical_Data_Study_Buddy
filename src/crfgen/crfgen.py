import click
from rich.console import Console

from . import __version__
from .exporter.registry import get_exporter
from cdisc_library_client.harvest import harvest

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


def main():
    app()
