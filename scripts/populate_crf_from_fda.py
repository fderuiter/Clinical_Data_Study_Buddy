import argparse
import csv
import sys
import logging
import json
from crfgen.populators import populate_ae_from_fda, populate_label_from_fda

def output_csv(data, writer):
    if not data:
        return
    # Assuming data is a list of dicts, get headers from the first item
    headers = data[0].keys()
    writer.writerow(headers)
    for item in data:
        writer.writerow(item.values())

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description="Populate CRF data from openFDA.")
    parser.add_argument("--drug-name", required=True, help="The name of the drug to search for.")
    parser.add_argument("--domain", required=True, choices=["AE", "LABEL"], help="The domain to populate.")
    parser.add_argument("--max-results", type=int, default=10, help="The maximum number of records to return (for AE domain).")
    parser.add_argument("--start-date", help="Start date for filtering (YYYYMMDD).")
    parser.add_argument("--end-date", help="End date for filtering (YYYYMMDD).")
    parser.add_argument("--output-format", default="csv", choices=["csv", "json"], help="The output format.")
    args = parser.parse_args()

    results = None
    if args.domain == "AE":
        results = populate_ae_from_fda(
            args.drug_name,
            max_results=args.max_results,
            start_date=args.start_date,
            end_date=args.end_date
        )
    elif args.domain == "LABEL":
        results = populate_label_from_fda(args.drug_name)

    if not results:
        return

    if args.output_format == "json":
        print(json.dumps(results, indent=2))
    elif args.output_format == "csv":
        csv_writer = csv.writer(sys.stdout)
        if isinstance(results, list):
            output_csv(results, csv_writer)
        elif isinstance(results, dict):
            # For label data, write key-value pairs
            csv_writer.writerow(["Field", "Value"])
            for key, value in results.items():
                csv_writer.writerow([key, ", ".join(value) if isinstance(value, list) else value])

if __name__ == "__main__":
    main()
