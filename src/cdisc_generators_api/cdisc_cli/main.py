import typer
from rich.console import Console
from dotenv import load_dotenv

from cdisc_generators_api.cdisc_cli.commands.generate import generate_app
from cdisc_generators_api.cdisc_cli.commands.build import build_app
from cdisc_generators_api.cdisc_cli.commands.download import download_app
from cdisc_generators_api.cdisc_cli.commands.spec import spec_app
from cdisc_generators_api.cdisc_cli.commands.openfda import openfda_app
from cdisc_generators_api.cdisc_cli.commands.guides import adrg_app, sdrg_app


load_dotenv()

app = typer.Typer(
    name="cdisc",
    help="A new, unified CLI for the CDISC CRF Generator project.",
    add_completion=False,
)
console = Console()


@app.callback()
def main():
    """
    A new, unified CLI for the CDISC CRF Generator project.
    """
    # This callback will run before any command.
    # You can use it for common setup.
    pass

app.add_typer(generate_app, name="generate")
app.add_typer(build_app, name="build")
app.add_typer(download_app, name="download")
app.add_typer(spec_app, name="spec")
app.add_typer(openfda_app, name="openfda")
app.add_typer(adrg_app, name="adrg")
app.add_typer(sdrg_app, name="sdrg")


if __name__ == "__main__":
    app()
