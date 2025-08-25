import os
import pathlib
from typing import List
from cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient
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

    client = CDISCDataSetGeneratorClient()
    temp_dir = pathlib.Path(output_dir) / "temp_datasets"
    os.makedirs(temp_dir, exist_ok=True)

    for domain in domains:
        print(f"Generating {domain} dataset...")
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
            print(f"Downloading dataset to {output_path}...")
            client.download_file(download_url, str(output_path))
            print(f"{domain} dataset downloaded successfully.")
        except Exception as e:
            print(f"Error generating dataset for domain {domain}: {e}")

    if study_story != "none":
        apply_study_story(study_story, temp_dir, num_subjects, domains, output_format)

    generate_define_xml(temp_dir, domains)
    package_datasets(temp_dir, output_dir)
