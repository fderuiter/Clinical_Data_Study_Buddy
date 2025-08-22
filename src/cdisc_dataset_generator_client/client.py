import requests

class CDISCDataSetGeneratorClient:
    def __init__(self, base_url: str = "https://cdiscdataset.com/api"):
        self.base_url = base_url

    def generate_dataset(self, dataset_type: str, domain: str, num_subjects: int, therapeutic_area: str, format: str):
        """
        Generates a dataset using the cdiscdataset.com API.
        """
        endpoint_map = {
            "SDTM": "generate-sdtm",
            "ADaM": "generate-adam",
            "SEND": "generate-send",
        }
        endpoint = endpoint_map.get(dataset_type)
        if not endpoint:
            raise ValueError(f"Invalid dataset_type: {dataset_type}")

        url = f"{self.base_url}/{endpoint}"
        payload = {
            "domain": domain,
            "numSubjects": num_subjects,
            "therapeuticArea": therapeutic_area,
            "format": format,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def download_file(self, download_url: str, output_path: str):
        """
        Downloads a file from the given URL.
        """
        response = requests.get(f"https://cdiscdataset.com{download_url}")
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
