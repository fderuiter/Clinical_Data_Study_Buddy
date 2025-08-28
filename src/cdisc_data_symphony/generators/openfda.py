import csv
import sys
import json
from cdisc_data_symphony.generators.crfgen.populators import populate_ae_from_fda, populate_label_from_fda

def output_csv(data, writer):
    if not data:
        return
    headers = data[0].keys()
    writer.writerow(headers)
    for item in data:
        writer.writerow(item.values())

def populate_crf(drug_name: str, domain: str, max_results: int, start_date: str, end_date: str, output_format: str):
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
