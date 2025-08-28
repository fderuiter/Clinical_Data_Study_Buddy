"""
This module provides services for generating various CDISC artifacts.
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
from cdisc_data_symphony.generators.study_protocols_generator import StudyProtocolsGenerator
from cdisc_data_symphony.generators.specification_templates_generator import SpecificationTemplatesGenerator
from cdisc_data_symphony.generators.crfgen.cdash import build_domain_crf, load_ig
from cdisc_data_symphony.generators.crfgen.populators import populate_ae_from_fda
import yaml


def generate_tfl_shell(spec: str, output_file: pathlib.Path):
    """
    Generates a TFL shell document.

    :param spec: TFL specification
    :param output_file: Path to the output file
    """
    generator = TFLShellGenerator(spec)
    shell = generator.generate()
    with open(output_file, 'w') as f:
        f.write(shell)


def generate_sas_code(dataset: str, output_type: str, treatment_var: str, output_file: pathlib.Path):
    """
    Generates analysis code in SAS.

    :param dataset: Source dataset (e.g., ADSL)
    :param output_type: Type of analysis output (e.g., Demographics)
    :param treatment_var: Treatment variable (e.g., TRT01A)
    :param output_file: Path to the output file
    """
    generator = AnalysisGenerator("sas", dataset, output_type, treatment_var)
    code = generator.generate_code()
    with open(output_file, 'w') as f:
        f.write(code)


def generate_edc_raw_dataset_package(num_subjects: int, therapeutic_area: str, domains: List[str], study_story: str, output_dir: pathlib.Path, output_format: str):
    """
    Generate an EDC Raw Dataset Package.

    :param num_subjects: Number of subjects (10-200)
    :param therapeutic_area: Therapeutic area for the study
    :param domains: List of domains to include (e.g., DM AE VS LB)
    :param study_story: Study story to simulate (none, high_dropout)
    :param output_dir: Directory to save the generated package
    :param output_format: Output format for datasets (csv, json, xpt)
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


def generate_synthetic_data(standard: str, version: str, domain: str, num_subjects: int, output_dir: pathlib.Path):
    """
    Generate synthetic CDISC datasets.

    :param standard: The standard to generate data for (e.g., sdtmig).
    :param version: The version of the standard (e.g., 3-3).
    :param domain: The domain to generate data for (e.g., DM).
    :param num_subjects: Number of subjects.
    :param output_dir: Directory to save the file.
    :return: Path to the generated file.
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

    :param language: Language for the generated code (sas or r)
    :param dataset: Source dataset (e.g., ADSL)
    :param output_type: Type of analysis output (e.g., Demographics)
    :param treatment_var: Treatment variable (e.g., TRT01A)
    :param output_file: Path to the output file
    """
    generator = AnalysisGenerator(language, dataset, output_type, treatment_var)
    code = generator.generate_code()
    with open(output_file, 'w') as f:
        f.write(code)


def generate_cdash_crf(ig_version: str, out_dir: pathlib.Path, domains: Optional[List[str]], config_path: pathlib.Path, openfda_drug_name: Optional[str], openfda_max_results: int):
    """
    Generate Word CRF shells from CDISC Library API.

    :param ig_version: CDASHIG version (e.g., v2.3)
    :param out_dir: Directory for generated Word documents
    :param domains: Optional domain whitelist (e.g. AE CM VS)
    :param config_path: Path to the configuration file.
    :param openfda_drug_name: Drug name to fetch adverse events from OpenFDA.
    :param openfda_max_results: Max adverse events to fetch from OpenFDA.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
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

    :param therapeutic_area: The therapeutic area of the study.
    :param treatment_arms: A treatment arm of the study. Can be specified multiple times.
    :param duration_weeks: The duration of the study in weeks.
    :param phase: The phase of the study.
    :param output_dir: The directory to save the generated protocol documents.
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
    Generate Excel-based specification templates for CDISC datasets.

    :param product: The CDISC product (e.g., sdtmig, adamig).
    :param version: The version of the product (e.g., 3-3).
    :param domains: A list of domains to include in the specification (e.g., DM AE VS).
    :param output_dir: The directory to save the generated Excel file.
    """
    generator = SpecificationTemplatesGenerator(product, version, domains, str(output_dir))
    generator.generate()
