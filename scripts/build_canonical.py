#!/usr/bin/env python
import argparse
import os
import sys

from crfgen.crawl import harvest, write_json

p = argparse.ArgumentParser()
p.add_argument("-o", "--out", default="crf.json")
p.add_argument("-v", "--version", help="IG version substring (optional)")
args = p.parse_args()

token = os.getenv("CDISC_PRIMARY_KEY")
if not token:
    sys.exit("ERROR: set CDISC_PRIMARY_KEY environment variable")

forms = harvest(token, ig_filter=args.version)
write_json(forms, args.out)
print(f"✅  Saved {len(forms)} forms -> {args.out}")
