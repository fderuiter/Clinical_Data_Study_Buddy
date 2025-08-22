import argparse
import os
from pathlib import Path
import openpyxl

from cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient


def generate_dataset_from_spec(spec_path: str, output_dir: str):
    """
    Generates a dataset from a specification file.
    """
    path = Path(spec_path)
    filename = path.stem
    try:
        product, version, _ = filename.split("_", 2)
    except ValueError:
        print(
            "Invalid spec filename format. Expected '<product>_<version>_spec.xlsx'."
        )
        return

    workbook = openpyxl.load_workbook(path)
    domains = workbook.sheetnames

    client = CDISCDataSetGeneratorClient()

    for domain in domains:
        if domain.lower() == "metadata":
            continue
        print(f"Generating dataset for domain {domain}...")
        try:
            # The dataset_type for the generator client might not be the same as the product name.
            # SDTMIG -> SDTM. We'll need a mapping for this.
            dataset_type = "SDTM" if "sdtm" in product.lower() else product.upper()

            result = client.generate_dataset(
                dataset_type=dataset_type,
                domain=domain,
                num_subjects=50,
                therapeutic_area="Oncology",  # Added therapeutic_area
                format="csv",
            )
            download_url = result["download_url"]
            output_filename = result["filename"]
            output_path = os.path.join(output_dir, output_filename)

            print(f"Downloading dataset to {output_path}...")
            client.download_file(download_url, output_path)
            print(f"Dataset for domain {domain} downloaded successfully.")

        except Exception as e:
            print(f"Could not generate dataset for domain {domain}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a synthetic dataset from an Excel specification file."
    )
    parser.add_argument(
        "--spec-file",
        required=True,
        help="Path to the Excel specification file (e.g., sdtmig_3-3_spec.xlsx).",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="The directory to save the generated dataset files.",
    )
    args = parser.parse_args()
    generate_dataset_from_spec(args.spec_file, args.output_dir)


if __name__ == "__main__":
    main()
