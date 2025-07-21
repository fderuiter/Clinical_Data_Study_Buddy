import argparse
import os

from crfgen.crawl import harvest, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Build canonical CRF JSON")
    parser.add_argument("--filter", dest="filter", help="Substring to match IG version", default=None)
    parser.add_argument("--output", dest="output", help="Output JSON path", default="crf.json")
    args = parser.parse_args()

    token = os.environ["CDISC_PRIMARY_KEY"]
    forms = harvest(token, ig_filter=args.filter)
    write_json(forms, args.output)


if __name__ == "__main__":
    main()
