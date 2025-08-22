#!/usr/bin/env python
import argparse
import sys

from crfgen.auth import get_client
from crfgen.crawl import harvest, write_json

p = argparse.ArgumentParser()
p.add_argument("-o", "--out", default="crf.json")
p.add_argument("-v", "--version", help="IG version substring (optional)")
args = p.parse_args()

try:
    client = get_client()
except ValueError as e:
    sys.exit(f"ERROR: {e}")

forms = harvest(client, ig_filter=args.version)
write_json(forms, args.out)
print(f"✅  Saved {len(forms)} forms -> {args.out}")
