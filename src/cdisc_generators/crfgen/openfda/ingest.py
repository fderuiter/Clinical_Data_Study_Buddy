import asyncio
import httpx
import os
import zipfile
from datetime import datetime
from io import BytesIO
from typing import Dict

# Placeholder for the official download links
DOWNLOAD_LINKS: Dict[str, str] = {
    "device/udi": "https://download.open.fda.gov/device/udi/device-udi-0001-of-0001.json.zip",
    "device/event": "https://download.open.fda.gov/device/event/device-event-0001-of-0001.json.zip",
    "device/recall": "https://download.open.fda.gov/device/recall/device-recall-0001-of-0001.json.zip",
    "device/enforcement": "https://download.open.fda.gov/device/enforcement/device-enforcement-0001-of-0001.json.zip",
    "device/classification": "https://download.open.fda.gov/device/classification/device-classification-0001-of-0001.json.zip",
    "device/510k": "https://download.open.fda.gov/device/510k/device-510k-0001-of-0001.json.zip",
    "device/pma": "https://download.open.fda.gov/device/pma/device-pma-0001-of-0001.json.zip",
    "device/registrationlisting": "https://download.open.fda.gov/device/registrationlisting/device-registrationlisting-0001-of-0001.json.zip",
}

async def download_and_extract(endpoint: str, output_dir: str):
    """
    Downloads and extracts a bulk data zip file from the openFDA download portal.

    Args:
        endpoint: The endpoint to download data for.
        output_dir: The directory to store the extracted data.
    """
    if endpoint not in DOWNLOAD_LINKS:
        raise ValueError(f"Invalid endpoint: {endpoint}")

    url = DOWNLOAD_LINKS[endpoint]

    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()

    today = datetime.now().strftime("%Y%m%d")
    endpoint_path = endpoint.replace('/', '_')
    extract_path = os.path.join(output_dir, endpoint_path, today)
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(BytesIO(response.content)) as z:
        for i, member in enumerate(z.infolist()):
            if not member.is_dir():
                output_filename = os.path.join(extract_path, f"part-{i:04d}.jsonl")
                with open(output_filename, "wb") as f:
                    f.write(z.read(member.filename))

async def main():
    """
    An example of how to use the download_and_extract function.
    """
    await download_and_extract("device/udi", "data/openfda")

if __name__ == "__main__":
    asyncio.run(main())
