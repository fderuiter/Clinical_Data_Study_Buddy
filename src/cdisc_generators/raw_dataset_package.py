import os
import pathlib
from typing import List
import pandas as pd
from cdisc_library_client.harvest import harvest
from cdisc_generators.crfgen.utils import get_api_key
from cdisc_generators.data_generator import DataGenerator
from cdisc_generators.dataset_helpers import generate_define_xml, package_datasets, apply_study_story


def generate_raw_dataset_package(
    num_subjects: int,
    therapeutic_area: str,
    domains: List[str],
    study_story: str,
    output_dir: pathlib.Path,
    output_format: str,
):
    """
    Generates and packages a raw EDC dataset.

    :param num_subjects: Number of subjects.
    :param therapeutic_area: Therapeutic area for the study.
    :param domains: List of domains to include.
    :param study_story: Study story to simulate.
    :param output_dir: Directory to save the generated package.
    :param output_format: Output format for datasets.
    """
    print("Generating EDC Raw Dataset Package...")
    print(f"  Number of Subjects: {num_subjects}")
    print(f"  Therapeutic Area: {therapeutic_area}")
    print(f"  Domains: {', '.join(domains)}")
    print(f"  Study Story: {study_story}")
    print(f"  Output Format: {output_format}")
    print(f"  Output Directory: {output_dir}")

    api_key = get_api_key()
    forms = harvest(api_key)

    temp_dir = pathlib.Path(output_dir) / "temp_datasets"
    os.makedirs(temp_dir, exist_ok=True)

    for domain in domains:
        print(f"Generating {domain} dataset...")
        domain_form = next((f for f in forms if f.domain == domain), None)
        if not domain_form:
            print(f"Warning: Domain {domain} not found in CDISC Library. Skipping.")
            continue

        generator = DataGenerator(domain_form)
        dataset = generator.generate(num_subjects)

        output_file = temp_dir / f"{domain}.csv"
        df = pd.DataFrame(dataset)
        df.to_csv(output_file, index=False)
        print(f"{domain} dataset generated successfully.")

    if study_story != "none":
        apply_study_story(study_story, temp_dir, num_subjects, domains, output_format)

    generate_define_xml(temp_dir, domains)
    package_datasets(temp_dir, output_dir)
