import json
from pathlib import Path
import httpx
from cdisc_library_client.client import AuthenticatedClient
from cdisc_library_client.api.sdtm_implementation_guide_sdtmig import (
    get_mdr_sdtmig_version,
    get_mdr_sdtmig_version_classes,
    get_mdr_sdtmig_version_datasets,
)
from cdisc_generators.crfgen.utils import get_api_key


def _get_client() -> AuthenticatedClient:
    """
    Get an authenticated client for the CDISC Library API.
    """
    api_key = get_api_key()
    transport = httpx.HTTPTransport(retries=5)
    client = AuthenticatedClient(
        base_url="https://library.cdisc.org/api",
        token=api_key,
        headers={"Accept": "application/json", "Cache-Control": "no-cache"},
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
        httpx_args={"transport": transport},
    )
    return client


def download_standard(standard: str, version: str, output_dir: Path):
    """
    Downloads a CDISC data standard from the CDISC Library.
    """
    if standard.lower() != "sdtmig":
        raise ValueError("Only sdtmig is supported at this time.")

    client = _get_client()
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
