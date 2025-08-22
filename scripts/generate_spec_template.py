import argparse
import os
from pathlib import Path
import json

import openpyxl
from cdisc_library_client.client import AuthenticatedClient
from cdisc_library_client.api.sdtm_implementation_guide_sdtmig import (
    get_mdr_sdtmig_version_datasets_dataset,
)
from cdisc_library_client.api.analysis_data_model_and_implementation_guide_a_da_m_and_a_da_mig import (
    get_mdr_adam_product_datastructures_structure,
)

from dotenv import load_dotenv


def get_client():
    load_dotenv()
    api_key = os.environ.get("CDISC_PRIMARY_KEY")
    if not api_key:
        raise ValueError(
            "CDISC Library API key not found. Please set the CDISC_PRIMARY_KEY environment variable."
        )
    # The client needs to be authenticated with the API key.
    # The key is passed in the headers, not as a bearer token.
    headers = {"api-key": api_key}
    return AuthenticatedClient(
        base_url="https://library.cdisc.org/api", headers=headers, token="dummy"
    )


def generate_spec_template(
    product: str, version: str, domains: list[str], output_dir: str
):
    client = get_client()
    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)  # Remove default sheet

    print(f"Generating spec for {product} v{version} for domains: {', '.join(domains)}")

    for domain in domains:
        print(f"Fetching data for domain: {domain}")
        worksheet = workbook.create_sheet(title=domain)
        # Add header row
        header = [
            "Variable Name",
            "Variable Label",
            "Data Type",
            "Role",
            "Core",
            "Codelist",
            "Description",
        ]
        worksheet.append(header)
        try:
            variables = []
            if product.lower() == "sdtmig":
                response = get_mdr_sdtmig_version_datasets_dataset.sync(
                    client=client, version=version, dataset=domain
                )
                if response and hasattr(response, "to_dict"):
                    dataset = response.to_dict()
                    # print(json.dumps(dataset, indent=2)) # Uncomment for debugging
                    variables = dataset.get("datasetVariables", [])
            elif product.lower() == "adamig":
                adam_product_id = f"adamig-{version}"
                response = get_mdr_adam_product_datastructures_structure.sync(
                    client=client, product=adam_product_id, structure=domain
                )
                if response and hasattr(response, "to_dict"):
                    dataset = response.to_dict()
                    # print(json.dumps(dataset, indent=2)) # Uncomment for debugging
                    varsets = dataset.get("analysisVariableSets", [])
                    for varset in varsets:
                        variables.extend(varset.get("analysisVariables", []))

            if not variables:
                print(f"No variables found for domain {domain}")
                worksheet.append([f"No variables found for domain {domain}"])
                continue

            for variable in variables:
                codelist_info = ""
                if variable.get("_links", {}).get("codelist"):
                    codelists = variable["_links"]["codelist"]
                    codelist_info = ", ".join([c.get("href", "") for c in codelists])
                row = [
                    variable.get("name"),
                    variable.get("label"),
                    variable.get("simpleDatatype"),
                    variable.get("role"),
                    variable.get("core"),
                    codelist_info,
                    variable.get("description"),
                ]
                worksheet.append(row)

        except Exception as e:
            print(f"Could not fetch data for domain {domain}: {e}")
            worksheet.append([f"Error fetching data for {domain}"])

    output_path = Path(output_dir) / f"{product}_{version}_spec.xlsx"
    workbook.save(output_path)
    print(f"Specification template generated at: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Excel-based specification templates for CDISC datasets."
    )
    parser.add_argument(
        "--product",
        required=True,
        help="The CDISC product (e.g., sdtmig, adamig).",
    )
    parser.add_argument(
        "--version",
        required=True,
        help="The version of the product (e.g., 3-3).",
    )
    parser.add_argument(
        "--domains",
        required=True,
        nargs="+",
        help="A list of domains to include in the specification (e.g., DM AE VS).",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="The directory to save the generated Excel file.",
    )
    args = parser.parse_args()
    generate_spec_template(args.product, args.version, args.domains, args.output_dir)


if __name__ == "__main__":
    main()
