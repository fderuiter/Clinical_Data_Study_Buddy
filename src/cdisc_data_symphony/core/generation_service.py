"""
This module provides a suite of services for generating various clinical study artifacts.

The services offered include the generation of:
- TFL (Tables, Figures, and Listings) shell documents.
- Analysis code in SAS and R.
- EDC (Electronic Data Capture) raw dataset packages.
- Synthetic CDISC datasets.
- CDASH (Clinical Data Acquisition Standards Harmonization) CRF (Case Report Form) shells.
- Study protocols.
- Excel-based specification templates for CDISC datasets.
"""
import pathlib
from typing import List, Optional
import yaml
from cdisc_data_symphony.generators.data_generator import DataGenerator
from cdisc_library_client.harvest import harvest
from cdisc_data_symphony.generators.crfgen.utils import get_api_key
import pandas as pd
from cdisc_data_symphony.generators.raw_dataset_package import generate_raw_dataset_package
from cdisc_data_symphony.generators.analysisgen.generator import AnalysisGenerator
from cdisc_data_symphony.generators.tfl.tfl_shell_generator import TFLShellGenerator
from cdisc_data_symphony.generators.edc_raw_dataset_package_generator import EDCRawDatasetPackageGenerator
from cdisc_data_symphony.generators.documents.study_protocols_generator import StudyProtocolsGenerator
from cdisc_data_symphony.generators.specification_templates_generator import SpecificationTemplatesGenerator
from cdisc_data_symphony.generators.crfgen.cdash import build_domain_crf, load_ig
from cdisc_data_symphony.generators.crfgen.populators import populate_ae_from_fda
import yaml


def generate_tfl_shell(spec: str, output_file: pathlib.Path):
    """
    Generates a TFL (Tables, Figures, and Listings) shell document.

    Args:
        spec (str): The TFL specification.
        output_file (pathlib.Path): The path to the output file where the shell document will be saved.
    """
    generator = TFLShellGenerator(spec)
    shell = generator.generate()
    with open(output_file, 'w') as f:
        f.write(shell)


def generate_edc_raw_dataset_package(num_subjects: int, therapeutic_area: str, domains: List[str], study_story: str, output_dir: pathlib.Path, output_format: str):
    """
    Generates an EDC (Electronic Data Capture) Raw Dataset Package.

    Args:
        num_subjects (int): The number of subjects for the study (between 10 and 200).
        therapeutic_area (str): The therapeutic area for the study.
        domains (List[str]): A list of domains to include (e.g., ["DM", "AE", "VS", "LB"]).
        study_story (str): The study story to simulate (e.g., "none", "high_dropout").
        output_dir (pathlib.Path): The directory where the generated package will be saved.
        output_format (str): The output format for the datasets (e.g., "csv", "json", "xpt").
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


def generate_synthetic_data(standard: str, version: str, domain: str, num_subjects: int, output_dir: pathlib.Path) -> str:
    """
    Generates synthetic CDISC datasets.

    Args:
        standard (str): The standard to generate data for (e.g., "sdtmig").
        version (str): The version of the standard (e.g., "3-3").
        domain (str): The domain to generate data for (e.g., "DM").
        num_subjects (int): The number of subjects.
        output_dir (pathlib.Path): The directory where the generated file will be saved.

    Returns:
        str: The path to the generated file.

    Raises:
        ValueError: If the specified domain is not found in the given standard and version.
    """
    api_key = get_api_key()
    forms = harvest(api_key, ig_filter=version)
    domain_form = next((f for f in forms if f.domain == domain), None)
    if not domain_form:
        raise ValueError(f"Domain {domain} not found in {standard} {version}")

    generator = DataGenerator(domain_form)
    dataset = generator.generate(num_subjects)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{domain}.csv"
    df = pd.DataFrame(dataset)
    df.to_csv(output_file, index=False)
    return str(output_file)


def generate_analysis_code(language: str, dataset: str, output_type: str, treatment_var: str, output_file: pathlib.Path):
    """
    Generates analysis code in SAS or R.

    Args:
        language (str): The language for the generated code ("sas" or "r").
        dataset (str): The source dataset (e.g., "ADSL").
        output_type (str): The type of analysis output (e.g., "Demographics").
        treatment_var (str): The treatment variable (e.g., "TRT01A").
        output_file (pathlib.Path): The path to the output file where the code will be saved.
    """
    generator = AnalysisGenerator(language, dataset, output_type, treatment_var)
    code = generator.generate_code()
    with open(output_file, 'w') as f:
        f.write(code)


def generate_cdash_crf(ig_version: str, out_dir: pathlib.Path, domains: Optional[List[str]], config_path: pathlib.Path, openfda_drug_name: Optional[str], openfda_max_results: int):
    """
    Generates Word CRF (Case Report Form) shells from the CDISC Library API.

    Args:
        ig_version (str): The CDASHIG version (e.g., "v2.3").
        out_dir (pathlib.Path): The directory for the generated Word documents.
        domains (Optional[List[str]]): An optional whitelist of domains (e.g., ["AE", "CM", "VS"]).
        config_path (pathlib.Path): The path to the configuration file.
        openfda_drug_name (Optional[str]): The drug name to fetch adverse events from OpenFDA.
        openfda_max_results (int): The maximum number of adverse events to fetch from OpenFDA.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_path.is_file():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    else:
        if config_path.exists():
            print(f"Warning: Config path {config_path} is a directory, not a file. Using default values.")
        else:
            print(f"Warning: Config file not found at {config_path}. Using default values.")

    fda_adverse_events = None
    if openfda_drug_name:
        fda_adverse_events = populate_ae_from_fda(
            openfda_drug_name, max_results=openfda_max_results
        )

    ig_df = load_ig(ig_version)

    target_domains = [d.upper() for d in (domains or ig_df["Domain"].unique())]
    for dom in target_domains:
        dom_df = ig_df[ig_df["Domain"] == dom]
        if dom_df.empty:
            print(f"Domain {dom} not found in IG – skipped")
            continue
        build_domain_crf(dom_df, dom, out_dir, config, fda_adverse_events=fda_adverse_events)


def generate_study_protocols(therapeutic_area: str, treatment_arms: List[str], duration_weeks: int, phase: int, output_dir: pathlib.Path):
    """
    Generates a study protocol.

    Args:
        therapeutic_area (str): The therapeutic area of the study.
        treatment_arms (List[str]): A list of treatment arms for the study.
        duration_weeks (int): The duration of the study in weeks.
        phase (int): The phase of the study.
        output_dir (pathlib.Path): The directory where the generated protocol documents will be saved.
    """
    generator = StudyProtocolsGenerator(
        therapeutic_area=therapeutic_area,
        treatment_arms=treatment_arms,
        duration_weeks=duration_weeks,
        phase=phase,
        output_dir=str(output_dir)
    )
    generator.generate()


def generate_specification_templates(product: str, version: str, domains: List[str], output_dir: pathlib.Path):
    """
    Generates Excel-based specification templates for CDISC datasets.

    Args:
        product (str): The CDISC product (e.g., "sdtmig", "adamig").
        version (str): The version of the product (e.g., "3-3").
        domains (List[str]): A list of domains to include in the specification (e.g., ["DM", "AE", "VS"]).
        output_dir (pathlib.Path): The directory where the generated Excel file will be saved.
    """
    generator = SpecificationTemplatesGenerator(product, version, domains, str(output_dir))
    generator.generate()
