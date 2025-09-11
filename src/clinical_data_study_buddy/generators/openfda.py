"""
This module provides functionality to interact with the OpenFDA API to populate
Case Report Forms (CRFs) with adverse event and drug label information.
"""
import csv
import sys
import json
from clinical_data_study_buddy.generators.crfgen.populators import populate_ae_from_fda, populate_label_from_fda

def output_csv(data, writer):
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        data (list): A list of dictionaries to be written to CSV.
        writer: A csv.writer object.
    """
    if not data:
        return
    headers = data[0].keys()
    writer.writerow(headers)
    for item in data:
        writer.writerow(item.values())

def populate_crf(drug_name: str, domain: str, max_results: int, start_date: str, end_date: str, output_format: str):
    """
    Populates a CRF with data from OpenFDA.

    This function fetches data from OpenFDA for a given drug and domain,
    and then outputs the data in the specified format (JSON or CSV).

    Args:
        drug_name (str): The name of the drug to fetch data for.
        domain (str): The domain of data to fetch ("AE" for adverse events, "LABEL" for drug labels).
        max_results (int): The maximum number of results to return.
        start_date (str): The start date for the data search (YYYY-MM-DD).
        end_date (str): The end date for the data search (YYYY-MM-DD).
        output_format (str): The desired output format ("json" or "csv").
    """
    results = None
    if domain == "AE":
        results = populate_ae_from_fda(
            drug_name,
            max_results=max_results,
            start_date=start_date,
            end_date=end_date
        )
    elif domain == "LABEL":
        results = populate_label_from_fda(drug_name)

    if not results:
        return

    if output_format == "json":
        print(json.dumps(results, indent=2))
    elif output_format == "csv":
        csv_writer = csv.writer(sys.stdout)
        if isinstance(results, list):
            output_csv(results, csv_writer)
        elif isinstance(results, dict):
            csv_writer.writerow(["Field", "Value"])
            for key, value in results.items():
                csv_writer.writerow([key, ", ".join(value) if isinstance(value, list) else value])
