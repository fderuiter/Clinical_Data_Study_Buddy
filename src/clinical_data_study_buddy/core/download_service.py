"""
This module provides a service for downloading CDISC standards from the CDISC Library API.
"""
import json
from pathlib import Path
import httpx
from cdisc_library_client.client import AuthenticatedClient
from cdisc_library_client.api.sdtm_implementation_guide_sdtmig import (
    get_mdr_sdtmig_version,
    get_mdr_sdtmig_version_classes,
    get_mdr_sdtmig_version_datasets,
)
from clinical_data_study_buddy.services.cdisc_library_service import get_client


def download_standard(standard: str, version: str, output_dir: Path):
    """
    Downloads a CDISC data standard from the CDISC Library.

    This function currently supports downloading the "sdtmig" standard.
    It fetches the standard's data, including its classes and datasets,
    and saves it as a JSON file in the specified output directory.

    Args:
        standard (str): The name of the standard to download. Currently, only "sdtmig" is supported.
        version (str): The version of the standard to download.
        output_dir (Path): The directory where the downloaded standard will be saved.

    Raises:
        ValueError: If a standard other than "sdtmig" is requested.
    """
    if standard.lower() != "sdtmig":
        raise ValueError("Only sdtmig is supported at this time.")

    client = get_client()
    data = get_mdr_sdtmig_version.sync(client=client, version=version)

    classes = []
    for class_link in data["_links"]["classes"]:
        class_data = get_mdr_sdtmig_version_classes.sync(client=client, version=version, class_name=class_link["title"])
        classes.append(class_data)
    data["classes"] = classes

    datasets = []
    for dataset_link in data["_links"]["datasets"]:
        dataset_data = get_mdr_sdtmig_version_datasets.sync(client=client, version=version, dataset_name=dataset_link["title"])
        datasets.append(dataset_data)
    data["datasets"] = datasets

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{standard}_{version}.json"
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
