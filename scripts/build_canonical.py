#!/usr/bin/env python
import argparse
import json
import sys

from cdisc_library_client.harvest import harvest
from crfgen.utils import get_api_key


def write_json(forms: list, out: str):
    with open(out, "w") as f:
        json.dump([f.to_dict() for f in forms], f, indent=2)


p = argparse.ArgumentParser()
p.add_argument("-o", "--out", default="crf.json")
p.add_argument("-v", "--version", help="IG version substring (optional)")
args = p.parse_args()

try:
    api_key = get_api_key()
except ValueError as e:
    sys.exit(f"ERROR: {e}")

forms = harvest(api_key, ig_filter=args.version)
write_json(forms, args.out)
print(f"✅  Saved {len(forms)} forms -> {args.out}")
