import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv

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


@app.command()
def generate_cdash_crf(
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
    from src.crfgen.cdash import build_domain_crf, load_ig
    from crfgen.populators import populate_ae_from_fda
    import yaml

    out_dir.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    else:
        console.print(f"Warning: Config file not found at {config_path}. Using default values.", style="yellow")

    fda_adverse_events = None
    if openfda_drug_name:
        console.print(f"Fetching adverse events for {openfda_drug_name} from OpenFDA...")
        fda_adverse_events = populate_ae_from_fda(
            openfda_drug_name, max_results=openfda_max_results
        )
        console.print(f"Found {len(fda_adverse_events)} suggested adverse event terms.")

    ig_df = load_ig(ig_version)

    target_domains = [d.upper() for d in (domains or ig_df["Domain"].unique())]
    for dom in target_domains:
        dom_df = ig_df[ig_df["Domain"] == dom]
        if dom_df.empty:
            console.print(f"Domain {dom} not found in IG – skipped", style="yellow")
            continue
        build_domain_crf(dom_df, dom, out_dir, config, fda_adverse_events=fda_adverse_events)


if __name__ == "__main__":
    app()
