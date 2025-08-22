#!/usr/bin/env python
import argparse
import os

from src.cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic CDISC datasets.")
    parser.add_argument("--dataset-type", required=True, choices=["SDTM", "ADaM", "SEND"], help="Type of dataset to generate.")
    parser.add_argument("--domain", required=True, help="Domain for the dataset.")
    parser.add_argument("--num-subjects", type=int, default=50, help="Number of subjects.")
    parser.add_argument("--therapeutic-area", default="Oncology", help="Therapeutic area.")
    parser.add_argument("--format", default="csv", choices=["csv", "json", "xpt"], help="Output format.")
    parser.add_argument("--output-dir", default=".", help="Directory to save the downloaded file.")
    args = parser.parse_args()

    client = CDISCDataSetGeneratorClient()
    print(f"Generating {args.dataset_type} dataset for domain {args.domain}...")
    result = client.generate_dataset(
        dataset_type=args.dataset_type,
        domain=args.domain,
        num_subjects=args.num_subjects,
        therapeutic_area=args.therapeutic_area,
        format=args.format,
    )
    print("Dataset generated successfully.")

    download_url = result["download_url"]
    filename = result["filename"]
    output_path = os.path.join(args.output_dir, filename)

    print(f"Downloading dataset to {output_path}...")
    client.download_file(download_url, output_path)
    print("Dataset downloaded successfully.")

if __name__ == "__main__":
    main()
