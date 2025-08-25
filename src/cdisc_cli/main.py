import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
import json
import sys
import yaml
from cdisc_library_client.harvest import harvest
from cdisc_generators.crfgen.utils import get_api_key
from cdisc_generators.standard_downloader import download_standard as download_standard_func
from cdisc_generators.crfgen.cdash import build_domain_crf, load_ig
from cdisc_generators.crfgen.populators import populate_ae_from_fda
import cdisc_generators.crfgen.exporter.csv  # noqa
import cdisc_generators.crfgen.exporter.docx  # noqa
import cdisc_generators.crfgen.exporter.latex  # noqa
import cdisc_generators.crfgen.exporter.pdf  # noqa
import cdisc_generators.crfgen.exporter.rtf  # noqa
import cdisc_generators.crfgen.exporter.markdown  # noqa
import cdisc_generators.crfgen.exporter.odm  # noqa
import cdisc_generators.crfgen.exporter.xlsx  # noqa
from cdisc_generators.crfgen.exporter import registry as reg
from cdisc_generators.crfgen.schema import Form
from cdisc_generators.analysisgen.generator import AnalysisGenerator
from cdisc_generators.analysisgen.sas_generator import SASGenerator
from cdisc_generators.data_generator import DataGenerator
from cdisc_generators.tfl.tfl_shell_generator import TFLShellGenerator
from cdisc_generators.dataset_helpers import generate_define_xml, package_datasets, apply_study_story
import pandas as pd
from pathlib import Path
import os


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
def generate_tfl_shell(
    spec: str = typer.Option(..., "--spec", help="TFL specification"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates a TFL shell document.
    """
    generator = TFLShellGenerator(spec)
    shell = generator.generate()

    try:
        with open(output_file, 'w') as f:
            f.write(shell)
        console.print(f"Successfully generated TFL shell in {output_file}")
    except IOError as e:
        console.print(f"Error writing to file: {e}", style="bold red")


@app.command()
def generate_sas_code(
    dataset: str = typer.Option(..., "--dataset", help="Source dataset (e.g., ADSL)"),
    output_type: str = typer.Option(..., "--output-type", help="Type of analysis output (e.g., Demographics)"),
    treatment_var: str = typer.Option(..., "--treatment-var", help="Treatment variable (e.g., TRT01A)"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates analysis code in SAS.
    """
    generator = SASGenerator(dataset, output_type, treatment_var)
    code = generator.generate()

    try:
        with open(output_file, 'w') as f:
            f.write(code)
        console.print(f"Successfully generated SAS code in {output_file}")
    except IOError as e:
        console.print(f"Error writing to file: {e}", style="bold red")


@app.command()
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


@app.command()
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


@app.command()
def download_standard(
    standard: str = typer.Option(..., "--standard", "-s", help="The standard to download (e.g., sdtmig, adamig)."),
    version: str = typer.Option(..., "--version", "-v", help="The version of the standard (e.g., 3-3)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", "-o", help="The directory to save the downloaded files.")
):
    """
    Download a CDISC data standard from the CDISC Library.
    """
    console.print(f"Downloading {standard} version {version} to {output_dir}...")
    try:
        download_standard_func(standard, version, output_dir)
        console.print("✅  Download complete.")
    except Exception as e:
        console.print(f"ERROR: {e}", style="bold red")
        sys.exit(1)


from cdisc_generators.edc_raw_dataset_package_generator import EDCRawDatasetPackageGenerator

@app.command()
def generate_edc_raw_dataset_package(
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects (10-200)"),
    therapeutic_area: str = typer.Option("Oncology", "--therapeutic-area", help="Therapeutic area for the study"),
    domains: List[str] = typer.Option(..., "--domains", help="List of domains to include (e.g., DM AE VS LB)"),
    study_story: str = typer.Option("none", "--study-story", help="Study story to simulate (none, high_dropout)"),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the generated package"),
    output_format: str = typer.Option("csv", "--output-format", help="Output format for datasets (csv, json, xpt)")
):
    """
    Generate an EDC Raw Dataset Package.
    """
    generator = EDCRawDatasetPackageGenerator(
        num_subjects=num_subjects,
        therapeutic_area=therapeutic_area,
        domains=domains,
        study_story=study_story,
        output_dir=output_dir,
        output_format=output_format,
    )
    generator.generate()
    console.print(f"EDC Raw Dataset Package generated successfully in {output_dir}")


@app.command()
def generate_synthetic_data(
    standard: str = typer.Option(..., "--standard", help="The standard to generate data for (e.g., sdtmig)."),
    version: str = typer.Option(..., "--version", help="The version of the standard (e.g., 3-3)."),
    domain: str = typer.Option(..., "--domain", help="The domain to generate data for (e.g., DM)."),
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the file."),
):
    """
    Generate synthetic CDISC datasets.
    """
    console.print(f"Generating synthetic data for {standard} {version} domain {domain}...")
    api_key = get_api_key()
    forms = harvest(api_key, ig_filter=version)
    domain_form = next((f for f in forms if f.domain == domain), None)
    if not domain_form:
        console.print(f"ERROR: Domain {domain} not found in {standard} {version}", style="bold red")
        sys.exit(1)

    generator = DataGenerator(domain_form)
    dataset = generator.generate(num_subjects)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{domain}.csv"
    df = pd.DataFrame(dataset)
    df.to_csv(output_file, index=False)
    console.print(f"✅  Saved dataset -> {output_file}")


@app.command()
def generate_analysis(
    language: str = typer.Option(..., "--language", help="Language for the generated code (sas or r)"),
    dataset: str = typer.Option(..., "--dataset", help="Source dataset (e.g., ADSL)"),
    output_type: str = typer.Option(..., "--output-type", help="Type of analysis output (e.g., Demographics)"),
    treatment_var: str = typer.Option(..., "--treatment-var", help="Treatment variable (e.g., TRT01A)"),
    output_file: pathlib.Path = typer.Option(..., "--output-file", help="Path to the output file")
):
    """
    Generates analysis code in SAS or R.
    """
    generator = AnalysisGenerator(language, dataset, output_type, treatment_var)
    code = generator.generate_code()

    try:
        with open(output_file, 'w') as f:
            f.write(code)
        console.print(f"Successfully generated {language.upper()} code in {output_file}")
    except IOError as e:
        console.print(f"Error writing to file: {e}", style="bold red")


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


from cdisc_generators.study_protocols_generator import StudyProtocolsGenerator

@app.command()
def generate_study_protocols(
    therapeutic_area: str = typer.Option(..., "--therapeutic-area", help="The therapeutic area of the study."),
    treatment_arms: List[str] = typer.Option(..., "--treatment-arm", help="A treatment arm of the study. Can be specified multiple times."),
    duration_weeks: int = typer.Option(..., "--duration-weeks", help="The duration of the study in weeks."),
    phase: int = typer.Option(..., "--phase", help="The phase of the study."),
    output_dir: pathlib.Path = typer.Option("my_protocol", "--output-dir", help="The directory to save the generated protocol documents.")
):
    """
    Generates a study protocol.
    """
    generator = StudyProtocolsGenerator(
        therapeutic_area=therapeutic_area,
        treatment_arms=treatment_arms,
        duration_weeks=duration_weeks,
        phase=phase,
        output_dir=str(output_dir)
    )
    generator.generate()
    console.print(f"Protocol documents generated in {output_dir}")


from cdisc_generators.adrg import generate_adrg

adrg_app = typer.Typer()
app.add_typer(adrg_app, name="adrg")

@adrg_app.command("generate")
def adrg_generate(
    crf_json_path: pathlib.Path = typer.Option(..., "--crf", help="Path to the canonical crf.json file."),
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates an Analysis Data Reviewer's Guide (ADRG) document.
    """
    generate_adrg(crf_json_path, study_config_path, output_path)
    console.print(f"ADRG document generated at: {output_path}")


from cdisc_generators.sdrg import generate_sdrg

sdrg_app = typer.Typer()
app.add_typer(sdrg_app, name="sdrg")

@sdrg_app.command("generate")
def sdrg_generate(
    crf_json_path: pathlib.Path = typer.Option(..., "--crf", help="Path to the canonical crf.json file."),
    study_config_path: pathlib.Path = typer.Option(..., "--config", help="Path to the study-specific config file."),
    output_path: pathlib.Path = typer.Option(..., "--out", help="Path to the output Word document.")
):
    """
    Generates a Study Data Reviewer's Guide (SDRG) document.
    """
    generate_sdrg(crf_json_path, study_config_path, output_path)
    console.print(f"SDRG document generated at: {output_path}")


from cdisc_generators.specification_templates_generator import SpecificationTemplatesGenerator

@app.command()
def generate_specification_templates(
    product: str = typer.Option(..., "--product", help="The CDISC product (e.g., sdtmig, adamig)."),
    version: str = typer.Option(..., "--version", help="The version of the product (e.g., 3-3)."),
    domains: List[str] = typer.Option(..., "--domains", help="A list of domains to include in the specification (e.g., DM AE VS)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="The directory to save the generated Excel file.")
):
    """
    Generate Excel-based specification templates for CDISC datasets.
    """
    generator = SpecificationTemplatesGenerator(product, version, domains, str(output_dir))
    generator.generate()


from cdisc_generators.spec import generate_dataset, validate

spec_app = typer.Typer()
app.add_typer(spec_app, name="spec")

@spec_app.command("generate-dataset")
def spec_generate_dataset(
    spec_file: pathlib.Path = typer.Option(..., "--spec-file", help="Path to the Excel specification file (e.g., sdtmig_3-3_spec.xlsx)."),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="The directory to save the generated dataset files.")
):
    """
    Generate a synthetic dataset from an Excel specification file.
    """
    generate_dataset(str(spec_file), str(output_dir))

@spec_app.command("validate")
def spec_validate(
    spec_file: pathlib.Path = typer.Option(..., "--spec-file", help="Path to the Excel specification file."),
    dataset_file: pathlib.Path = typer.Option(..., "--dataset-file", help="Path to the dataset file (e.g., a CSV).")
):
    """
    Validate a dataset against an Excel specification file.
    """
    validate(str(spec_file), str(dataset_file))


from cdisc_generators.openfda import populate_crf

openfda_app = typer.Typer()
app.add_typer(openfda_app, name="openfda")

@openfda_app.command("populate-crf")
def openfda_populate_crf(
    drug_name: str = typer.Option(..., "--drug-name", help="The name of the drug to search for."),
    domain: str = typer.Option(..., "--domain", help="The domain to populate (AE or LABEL)."),
    max_results: int = typer.Option(10, "--max-results", help="The maximum number of records to return (for AE domain)."),
    start_date: str = typer.Option(None, "--start-date", help="Start date for filtering (YYYYMMDD)."),
    end_date: str = typer.Option(None, "--end-date", help="End date for filtering (YYYYMMDD)."),
    output_format: str = typer.Option("csv", "--output-format", help="The output format (csv or json).")
):
    """
    Populate CRF data from openFDA.
    """
    populate_crf(drug_name, domain, max_results, start_date, end_date, output_format)


if __name__ == "__main__":
    app()
