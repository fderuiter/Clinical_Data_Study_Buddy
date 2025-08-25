import typer
from rich.console import Console
import pathlib
from typing import List, Optional
from dotenv import load_dotenv
import json
import sys
import yaml
from cdisc_library_client.harvest import harvest
from crfgen.utils import get_api_key
from src.crfgen.cdash import build_domain_crf, load_ig
from crfgen.populators import populate_ae_from_fda
import crfgen.exporter.csv  # noqa
import crfgen.exporter.docx  # noqa
import crfgen.exporter.latex  # noqa
import crfgen.exporter.pdf  # noqa
import crfgen.exporter.rtf  # noqa
import crfgen.exporter.markdown  # noqa
import crfgen.exporter.odm  # noqa
import crfgen.exporter.xlsx  # noqa
from crfgen.exporter import registry as reg
from crfgen.schema import Form
from analysisgen.generator import AnalysisGenerator
from src.cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient
import os
import zipfile
from pathlib import Path
import pandas as pd
import random
import shutil
import httpx
from odmlib import odm_parser as P
from odmlib import odm_loader as L
from odmlib.define_2_1 import model as DEF
from odmlib.odm_1_3_2 import model as ODM
from src.cdisc_library_client.client import AuthenticatedClient


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


def _generate_define_xml(temp_dir, domains):
    console.print("Generating define.xml...")

    # Create the basic ODM structure
    root = ODM.ODM(
        FileOID="cdisc.com/Foundational/CDISC_ODM_2_0_0/define-2-1/2025-08-22/EDC_Raw_Dataset",
        CreationDateTime="2025-08-22T14:00:00",
        AsOfDateTime="2025-08-22T14:00:00",
        FileType="Snapshot",
        Originator="CDISC Dataset Generator",
        SourceSystem="CDISC Dataset Generator",
        SourceSystemVersion="0.1.0"
    )
    study = ODM.Study(OID="CDISC_STUDY.CDISC.TA.1")
    study.GlobalVariables = ODM.GlobalVariables()
    study.GlobalVariables.StudyName = ODM.StudyName(_content="CDISC TA Study")
    study.GlobalVariables.StudyDescription = ODM.StudyDescription(_content="A study in the TA therapeutic area")
    study.GlobalVariables.ProtocolName = ODM.ProtocolName(_content="CDISC-TA-1")
    root.Study.append(study)

    meta_data_version = DEF.MetaDataVersion(
        OID="MDV.CDISC_STUDY.CDISC.TA.1.SDTM.1.0",
        Name="CDISC TA Study SDTM 1.0",
        Description="Metadata for the CDISC TA Study",
        DefineVersion="2.1.0"
    )
    study.MetaDataVersion.append(meta_data_version)

    # Instantiate the CDISC Library client
    api_key = os.environ.get("CDISC_API_KEY")
    if not api_key:
        console.print("Warning: CDISC_API_KEY environment variable not set. Cannot fetch metadata.", style="yellow")
        # Create an empty define.xml
        define_xml_path = temp_dir / "define.xml"
        with open(define_xml_path, "w") as f:
            f.write("<ODM></ODM>")
        return

    client = AuthenticatedClient(
        base_url="https://library.cdisc.org/api",
        token=api_key,
        headers={"Accept": "application/json"},
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
    )

    sdtmig_version = "3-3" # Using a recent version as a default

    for domain in domains:
        domain_file = next(temp_dir.glob(f"sdtm_{domain.lower()}*.csv"), None)
        if not domain_file:
            continue

        # Create ItemGroupDef for the domain
        item_group_class = DEF.Class(Name="SPECIAL PURPOSE")
        item_group = DEF.ItemGroupDef(
            OID=f"IG.{domain.upper()}",
            Name=domain.upper(),
            Repeating="Yes",
            IsReferenceData="No",
            SASDatasetName=domain.upper(),
            Purpose="Tabulation",
            Structure="One record per subject",
            Class=item_group_class
        )
        meta_data_version.ItemGroupDef.append(item_group)

        # Get variable names from the CSV header
        df = pd.read_csv(domain_file)
        variables = list(df.columns)

        for var_name in variables:
            # Get variable metadata from CDISC Library using direct API call
            try:
                url = f"https://library.cdisc.org/products/sdtmig/{sdtmig_version}/datasets/{domain.upper()}/variables/{var_name}"
                headers = {"api-key": api_key, "Accept": "application/json"}
                response = httpx.get(url, headers=headers, timeout=60.0, follow_redirects=True)
                response.raise_for_status()
                variable_metadata = response.json()

                if variable_metadata:
                    item_def = DEF.ItemDef(
                        OID=f"IT.{domain.upper()}.{var_name}",
                        Name=var_name,
                        DataType=variable_metadata.get("datatype"),
                        Length=variable_metadata.get("length"),
                        SASFieldName=var_name
                    )
                    item_def.Description = DEF.Description()
                    item_def.Description.TranslatedText.append(
                        ODM.TranslatedText(_content=variable_metadata.get("label"), lang="en")
                    )
                    item_group.ItemRef.append(DEF.ItemRef(ItemOID=item_def.OID, OrderNumber=variables.index(var_name) + 1, Mandatory="No"))
                    meta_data_version.ItemDef.append(item_def)
                else:
                    console.print(f"  - Could not find metadata for variable {var_name} in domain {domain}", style="yellow")
            except httpx.HTTPStatusError as e:
                console.print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e.response.status_code}", style="yellow")
            except Exception as e:
                console.print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e}", style="yellow")


    # Write the file
    define_xml_path = temp_dir / "define.xml"
    root.write_xml(str(define_xml_path))
    console.print("define.xml generated.")

def _package_datasets(temp_dir, output_dir):
    zip_filename = Path(output_dir) / "edc_raw_datasets.zip"
    console.print(f"Packaging datasets into {zip_filename}...")
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in temp_dir.glob("*"):
            zipf.write(file, file.name)
    console.print("Packaging complete.")

    # Clean up the temporary directory
    console.print("Cleaning up temporary files...")
    shutil.rmtree(temp_dir)
    console.print("Cleanup complete.")

def _apply_study_story(study_story, temp_dir, num_subjects, domains, file_format):
    if study_story == "high_dropout":
        console.print("Applying 'high_dropout' study story...")
        dropout_rate = 0.3
        num_dropouts = int(num_subjects * dropout_rate)

        # Assuming DM is always present and contains the full subject list
        dm_file = next(temp_dir.glob("sdtm_dm*.csv"), None)
        if not dm_file:
            console.print("Warning: DM domain not found. Cannot apply high dropout story.", style="yellow")
            return

        if file_format == 'csv':
            dm_df = pd.read_csv(dm_file)
            all_subject_ids = dm_df["USUBJID"].unique()
            dropout_subject_ids = random.sample(list(all_subject_ids), num_dropouts)

            for domain in domains:
                if domain.upper() == "DM":
                    continue  # Don't remove subjects from DM

                domain_file = next(temp_dir.glob(f"sdtm_{domain.lower()}*.csv"), None)
                if domain_file:
                    df = pd.read_csv(domain_file)
                    df = df[~df["USUBJID"].isin(dropout_subject_ids)]
                    df.to_csv(domain_file, index=False)
                    console.print(f"  - Applied dropout to {domain} domain.")
        else:
            console.print(f"Warning: High dropout story not implemented for '{file_format}' format yet.", style="yellow")


@app.command()
def generate_raw_dataset_package(
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
    console.print("Generating EDC Raw Dataset Package...")
    console.print(f"  Number of Subjects: {num_subjects}")
    console.print(f"  Therapeutic Area: {therapeutic_area}")
    console.print(f"  Domains: {', '.join(domains)}")
    console.print(f"  Study Story: {study_story}")
    console.print(f"  Output Format: {output_format}")
    console.print(f"  Output Directory: {output_dir}")

    client = CDISCDataSetGeneratorClient()
    temp_dir = Path(output_dir) / "temp_datasets"
    os.makedirs(temp_dir, exist_ok=True)

    for domain in domains:
        console.print(f"Generating {domain} dataset...")
        try:
            result = client.generate_dataset(
                dataset_type="SDTM",
                domain=domain,
                num_subjects=num_subjects,
                therapeutic_area=therapeutic_area,
                format=output_format,
            )
            download_url = result["download_url"]
            filename = result["filename"]
            output_path = temp_dir / filename
            console.print(f"Downloading dataset to {output_path}...")
            client.download_file(download_url, str(output_path))
            console.print(f"{domain} dataset downloaded successfully.")
        except Exception as e:
            console.print(f"Error generating dataset for domain {domain}: {e}", style="bold red")

    if study_story != "none":
        _apply_study_story(study_story, temp_dir, num_subjects, domains, output_format)

    _generate_define_xml(temp_dir, domains)
    _package_datasets(temp_dir, output_dir)


@app.command()
def generate_synthetic_data(
    dataset_type: str = typer.Option(..., "--dataset-type", help="Type of dataset to generate (SDTM, ADaM, SEND)"),
    domain: str = typer.Option(..., "--domain", help="Domain for the dataset"),
    num_subjects: int = typer.Option(50, "--num-subjects", help="Number of subjects"),
    therapeutic_area: str = typer.Option("Oncology", "--therapeutic-area", help="Therapeutic area"),
    format: str = typer.Option("csv", "--format", help="Output format (csv, json, xpt)"),
    output_dir: pathlib.Path = typer.Option(".", "--output-dir", help="Directory to save the downloaded file")
):
    """
    Generate synthetic CDISC datasets.
    """
    client = CDISCDataSetGeneratorClient()
    console.print(f"Generating {dataset_type} dataset for domain {domain}...")
    result = client.generate_dataset(
        dataset_type=dataset_type,
        domain=domain,
        num_subjects=num_subjects,
        therapeutic_area=therapeutic_area,
        format=format,
    )
    console.print("Dataset generated successfully.")

    download_url = result["download_url"]
    filename = result["filename"]
    output_path = os.path.join(output_dir, filename)

    console.print(f"Downloading dataset to {output_path}...")
    client.download_file(download_url, output_path)
    console.print("Dataset downloaded successfully.")


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


if __name__ == "__main__":
    app()
