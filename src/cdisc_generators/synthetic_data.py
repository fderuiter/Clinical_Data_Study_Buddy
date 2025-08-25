import os
import pathlib
from cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient


def generate_and_download_synthetic_data(
    dataset_type: str,
    domain: str,
    num_subjects: int,
    therapeutic_area: str,
    data_format: str,
    output_dir: pathlib.Path,
) -> str:
    """
    Generates and downloads a synthetic CDISC dataset.

    :param dataset_type: Type of dataset (SDTM, ADaM, SEND).
    :param domain: Domain for the dataset.
    :param num_subjects: Number of subjects.
    :param therapeutic_area: Therapeutic area.
    :param data_format: Output format (csv, json, xpt).
    :param output_dir: Directory to save the file.
    :return: Path to the downloaded file.
    """
    client = CDISCDataSetGeneratorClient()
    print(f"Generating {dataset_type} dataset for domain {domain}...")
    result = client.generate_dataset(
        dataset_type=dataset_type,
        domain=domain,
        num_subjects=num_subjects,
        therapeutic_area=therapeutic_area,
        format=data_format,
    )
    print("Dataset generated successfully.")

    download_url = result["download_url"]
    filename = result["filename"]
    output_path = os.path.join(output_dir, filename)

    print(f"Downloading dataset to {output_path}...")
    client.download_file(download_url, str(output_path))
    print("Dataset downloaded successfully.")
    return output_path
