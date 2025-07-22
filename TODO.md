# CDISC CRF Generator Build Checklist

This file tracks progress across all phases of the project. Tick off each task after completion.

---

## Phase 0 – Create & prime the repository

* [ ] Create project folder `cdisc-crf-gen` and `cd` into it
* [ ] Run `git init`
* [ ] *(Optional)* Create GitHub repo (`gh repo create …`)
* [ ] Make base directories:

  * `openapi/`
  * `src/crfgen/exporter/`
  * `src/crfgen/templates/`
  * `src/crfgen/style/`
  * `scripts/`
  * `tests/.data/`
  * `.github/workflows/`
* [ ] Create top-level files: `README.md`, `LICENSE`, `.gitignore`
* [ ] Populate `.gitignore` with:

  ```
  __pycache__/
  *.py[cod]
  *.egg-info/
  .dist/
  build/
  .venv/
  .cache/
  artefacts/
  .env
  ```

## Phase 1 – Initialize Poetry project

* [ ] Run `poetry init` (set name, version, description, Python ≥3.11, license)
* [ ] Add runtime deps in `pyproject.toml`:

  * `openapi-python-client`
  * `jinja2`
  * `pydantic`
  * `requests`
  * `pandas`
  * `openpyxl`
  * `python-docx`
  * `odmlib`
* [ ] Add dev deps under `[tool.poetry.group.dev.dependencies]`:

  * `black`, `ruff`, `isort`, `pre-commit`, `pytest`, `pytest-cov`
* [ ] Run `poetry install` and verify imports (`pandas`, `jinja2`)

## Phase 2 – Bring in the OpenAPI spec & generate client

* [ ] Download spec JSON → `openapi/cdisc-library.json` (or YAML)
* [ ] *(Optional)* Convert JSON → YAML (`openapi/cdisc-library.yaml`)
* [ ] Generate client:

  ```
  poetry run openapi-python-client generate \
    --path openapi/cdisc-library.yaml \
    --meta none \
    --config '{"package_name":"cdisc_library_client",…}'
  ```
* [ ] Move `cdisc_library_client/` → `src/`
* [ ] Add to `pyproject.toml` under `[tool.poetry.packages]`:

  ```toml
  cdisc_library_client = { from = "src", include = "cdisc_library_client" }
  crfgen                = { from = "src", include = "crfgen" }
  ```
* [ ] Run `poetry install` and verify `import cdisc_library_client`

## Phase 3 – Core domain models

* [ ] Create `src/crfgen/schema.py` with Pydantic models:

  * `Codelist`
  * `Field`
  * `Form`
* [ ] *(Optional)* Add serialization helpers (`dump_forms` / `load_forms`)
* [ ] Verify via `poetry run python -c "from crfgen.schema import Form; …"`

## **Phase 4 – Crawler → `crf.json`**

*Objective: use the generated CDISC Library client to pull every CDASH form, translate to our `crfgen.schema.Form` objects, and persist them as `crf.json`. The crawler must respect rate limits, cache responses, and be unit-testable.*

---

### **Overview of deliverables**

| File                          | Purpose                                                                |
| ----------------------------- | ---------------------------------------------------------------------- |
| `src/crfgen/http.py`          | Session wrapper: bearer auth, exponential-back-off, on-disk JSON cache |
| `src/crfgen/crawl.py`         | `harvest()` + `write_json()` functions                                 |
| `scripts/build_canonical.py`  | CLI entry-point (`poetry run scripts/build_canonical.py`)              |
| `tests/test_crawl_fixture.py` | Offline unit test with JSON fixture                                    |
| `tests/test_crawl_live.py`    | *Optional* live “smoke” test (skipped when no `CDISC_PRIMARY_KEY`)         |

Each sub-step below ends with a **Checkpoint** command.

---

## **4.0  Auth & env assumptions**

The Library uses a **Bearer token**.
We’ll read it from `os.environ["CDISC_PRIMARY_KEY"]` only when needed.

---

## **4.1  HTTP utility module**

Create **`src/crfgen/http.py`**

```python
"""
Light wrapper around requests to add retry/back-off and
JSON disk-cache (protects Library quota & speeds tests).
"""

from __future__ import annotations
import json, os, time, pathlib
from typing import Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

CACHE_DIR = pathlib.Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)

def _retry_session() -> requests.Session:
    r = Retry(total=5, backoff_factor=0.4, status_forcelist=[502, 503, 504, 429])
    s = requests.Session()
    s.mount("https://", HTTPAdapter(max_retries=r))
    return s

def cached_get(url: str, headers: dict[str, str], ttl_days: int = 30) -> Any:
    fname = CACHE_DIR / (url.replace("/", "_").replace(":", "") + ".json")
    if fname.exists() and (time.time() - fname.stat().st_mtime) < ttl_days * 86400:
        return json.loads(fname.read_text())

    sess = _retry_session()
    r = sess.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    fname.write_text(r.text)
    return r.json()
```

**Checkpoint 4-1**

```bash
poetry run python - <<'PY'
from crfgen.http import cached_get
data = cached_get("https://httpbin.org/json", headers={})
print("title" in data)
PY
```

Expected: prints `True` and a file appears in `.cache/`.

---

## **4.2  Implement the crawler**

Create **`src/crfgen/crawl.py`**

```python
from __future__ import annotations
from typing import List, Optional
import os, time

from cdisc_library_client.api.default import md_r_cdashig_get  # endpoint names come from generated code
from cdisc_library_client.client import AuthenticatedClient
from crfgen.schema import Form
from crfgen.converter import form_from_api
from crfgen.http import cached_get

BASE = "https://library.cdisc.org/api"
ACCEPT = "application/vnd.cdisc+json"
DELAY = 0.2  # seconds between calls (<= 60 req/min)

def _client(token: str) -> AuthenticatedClient:
    return AuthenticatedClient(base_url=BASE, token=token, timeout=30.0)

def _json(url: str, token: str):
    hdr = {"Authorization": f"Bearer {token}", "Accept": ACCEPT}
    data = cached_get(url, hdr)
    time.sleep(DELAY)  # politeness
    return data

def harvest(token: str, ig_filter: Optional[str] = None) -> List[Form]:
    """Pull CDASH IG → domains → scenarios, convert to Form."""
    root = _json(f"{BASE}/mdr/cdashig", token)
    forms: list[Form] = []
    for ver in root["_links"]["versions"]:
        if ig_filter and ig_filter not in ver["title"]:
            continue
        ig = _json(ver["href"], token)
        for dom_link in ig["_links"]["domains"]:
            dom = _json(dom_link["href"], token)
            scenarios = dom["_links"].get("scenarios") or []
            payloads = [dom] + [_json(s["href"], token) for s in scenarios]
            for p in payloads:
                forms.append(form_from_api(p))
    return forms

# Convenience writer
import json, pathlib
def write_json(forms: List[Form], path="crf.json"):
    pathlib.Path(path).write_text(json.dumps([f.model_dump() for f in forms], indent=2))
```

**Checkpoint 4-2** *(requires API key, but tiny pull)*

```bash
export CDISC_PRIMARY_KEY=YOURTOKEN
poetry run python - <<'PY'
from crfgen.crawl import harvest
import os
forms = harvest(os.environ["CDISC_PRIMARY_KEY"], ig_filter="2-2")
print("forms:", len(forms))
print(forms[0].domain, "fields:", len(forms[0].fields))
PY
```

Expect: non-zero forms & sensible field counts.

---

## **4.3  CLI script**

Create **`scripts/build_canonical.py`**

```python
#!/usr/bin/env python
import argparse, os, sys
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
```

Make executable:

```bash
chmod +x scripts/build_canonical.py
```

**Checkpoint 4-3**

```bash
poetry run scripts/build_canonical.py -v 2-2 -o tmp.json
jq '.|length' tmp.json
```

You should see a number (> 0).

---

## **4.4  Offline unit-test with captured fixture**

1. Capture a tiny sample once:

```bash
poetry run scripts/build_canonical.py -v 2-2 -o tests/.data/sample_crf.json
```

*(Then commit that fixture to the repo.)*

2. Create **`tests/test_crawl_fixture.py`**

```python
import json
from crfgen.schema import Form

def test_fixture_loads():
    data = json.load(open("tests/.data/sample_crf.json"))
    forms = [Form(**d) for d in data]
    assert forms, "fixture empty"
    vs = [f for f in forms if f.domain == "VS"]
    assert vs and vs[0].fields, "Vitals missing fields"
```

**Checkpoint 4-4**

```bash
poetry run pytest tests/test_crawl_fixture.py -q
```

Expected: `.` (pass)

---

## **4.5  Optional live smoke-test**

**`tests/test_crawl_live.py`**

```python
import os, pytest
from crfgen.crawl import harvest

token = os.getenv("CDISC_PRIMARY_KEY")
@pytest.mark.skipif(not token, reason="no API key in env")
def test_live_pull_small():
    forms = harvest(token, ig_filter="2-2")
    assert len(forms) >= 40  # CDASH 2.2 domains
```

This runs in local dev & CI where the secret is available.

**Checkpoint 4-5**

Run `poetry run pytest -q` locally (should show 2 tests, skip if no key).

---

## **4.6  Git‐add & commit**

```bash
git add src/crfgen/http.py src/crfgen/crawl.py scripts/build_canonical.py tests
git commit -m "Phase 4: crawler + cache + CLI with unit tests"
```

---

## **Phase 4 complete – Acceptance criteria**

| Item                         | How to verify                                                      |
| ---------------------------- | ------------------------------------------------------------------ |
| **Crawler returns ≥ 1 form** | `poetry run scripts/build_canonical.py -o crf.json` prints a count |
| **Disk cache used**          | Subsequent runs hit `.cache/…json` files & skip remote call        |
| **Unit tests pass**          | `poetry run pytest -q` all green                                   |
| **Rate-limit friendly**      | No HTTP 429 seen when pulling full IG (observe in console)         |

You can now proceed to Phase 5 (templates & exporters) with confidence that `crf.json` is always reproducible and validated.

## **Phase 5 – Templates & Exporters**

*Goal : take `crf.json`, run each exporter, and drop multi-format artefacts into `artefacts/`.
We’ll add exporters incrementally, each with its own validation checkpoint and unit test.*

---

### 5.0  Prepare directories

```bash
mkdir -p src/crfgen/templates artefacts
```

Add these to **`pyproject.toml`** *if not present* so Poetry packages the templates:

```toml
[tool.poetry.package]
include = ["src/crfgen/templates/*.j2", "src/crfgen/style/*"]
```

**Checkpoint 5-0** – `git add` the new paths; `git status` is clean.

---

## **5 A – Markdown**

#### 5A-1  Template

`src/crfgen/templates/markdown.j2`

```jinja
# {{ form.title }}{% if form.scenario %} ({{ form.scenario }}){% endif %}

| OID | Prompt | Datatype | Codelist |
|-----|--------|----------|----------|
{% for fld in form.fields -%}
| `{{ fld.oid }}` | {{ fld.prompt|replace('|','\\|') }} | {{ fld.datatype }} | {% if fld.codelist %}{{ fld.codelist.nci_code }}{% endif %} |
{% endfor %}
```

#### 5A-2  Exporter

`src/crfgen/exporter/markdown.py`

```python
from pathlib import Path
from typing import List
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ..schema import Form
from .registry import register

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent.parent / "templates"),
    autoescape=select_autoescape()
)

@register("md")
def render_md(forms: List[Form], out_dir: Path):
    tpl = env.get_template("markdown.j2")
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in forms:
        (out_dir / f"{f.domain}.md").write_text(tpl.render(form=f))
```

#### **Checkpoint 5A**

```bash
poetry run scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats md
ls artefacts/*.md | head
```

At least one `*.md` file appears.

---

## **5 B – LaTeX**

#### 5B-1  Template

`src/crfgen/templates/latex.j2`

```jinja
\section*{ {{ form.title }}{% if form.scenario %} ({{ form.scenario }}){% endif %} }
\begin{tabular}{llll}
\textbf{OID} & \textbf{Prompt} & \textbf{Datatype} & \textbf{Codelist}\\ \hline
{% for fld in form.fields -%}
{{ fld.oid }} & {{ fld.prompt|replace('&','\\&') }} & {{ fld.datatype }} & {% if fld.codelist %}{{ fld.codelist.nci_code }}{% endif %} \\
{% endfor %}
\end{tabular}
```

#### 5B-2  Exporter

`src/crfgen/exporter/latex.py`

```python
from pathlib import Path
from typing import List
from jinja2 import Environment, FileSystemLoader
from ..schema import Form
from .registry import register

env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent / "templates"))

@register("tex")
def render_tex(forms: List[Form], out_dir: Path):
    out_dir.mkdir(exist_ok=True, parents=True)
    tpl = env.get_template("latex.j2")
    for f in forms:
        (out_dir / f"{f.domain}.tex").write_text(tpl.render(form=f))
```

#### **Checkpoint 5B**

```bash
poetry run scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats tex
ls artefacts/*.tex | head
```

---

## **5 C – DOCX (via Pandoc)**

> Ensure Pandoc is installed locally; CI step installs it with `apt-get install -y pandoc`.

#### 5C-1  Add a reference doc (optional branding)

Place a styled Word file at `src/crfgen/style/reference.docx`.
*(An empty doc is fine for now.)*

#### 5C-2  Exporter

`src/crfgen/exporter/docx.py`

```python
import subprocess, tempfile, shutil
from pathlib import Path
from typing import List
from .markdown import render_md
from ..schema import Form
from .registry import register

@register("docx")
def render_docx(forms: List[Form], out_dir: Path,
               reference_doc="src/crfgen/style/reference.docx"):
    tmp = Path(tempfile.mkdtemp(prefix="md-"))
    try:
        render_md(forms, tmp)
        out_dir.mkdir(parents=True, exist_ok=True)
        for md in tmp.glob("*.md"):
            subprocess.run(
                ["pandoc", md, "-o", out_dir / (md.stem + ".docx"),
                 "--reference-doc", reference_doc],
                check=True
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
```

#### **Checkpoint 5C**

```bash
poetry run scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats docx
file artefacts/*.docx | head
```

A DOCX file should report “Microsoft Word”.

---

## **5 D – CSV**

`src/crfgen/exporter/csv.py`

```python
import pandas as pd
from pathlib import Path
from typing import List
from ..schema import Form
from .registry import register

@register("csv")
def render_csv(forms: List[Form], out_dir: Path):
    rows = []
    for f in forms:
        for fld in f.fields:
            rows.append({
                "form": f.title,
                "domain": f.domain,
                "scenario": f.scenario or "",
                "oid": fld.oid,
                "prompt": fld.prompt,
                "datatype": fld.datatype,
                "codelist": fld.codelist.nci_code if fld.codelist else ""
            })
    out_dir.mkdir(exist_ok=True, parents=True)
    pd.DataFrame(rows).to_csv(out_dir / "forms.csv", index=False)
```

#### **Checkpoint 5D**

```bash
poetry run scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats csv
head artefacts/forms.csv
```

---

## **5 E – XLSX**

`src/crfgen/exporter/xlsx.py`

```python
import pandas as pd
from pathlib import Path
from typing import List
from ..schema import Form
from .registry import register

@register("xlsx")
def render_xlsx(forms: List[Form], out_dir: Path):
    out_dir.mkdir(exist_ok=True, parents=True)
    with pd.ExcelWriter(out_dir / "forms.xlsx") as xw:
        for f in forms:
            df = pd.DataFrame([{
                "OID": fld.oid,
                "Prompt": fld.prompt,
                "Datatype": fld.datatype,
                "Codelist": fld.codelist.nci_code if fld.codelist else ""
            } for fld in f.fields])
            sheet = f"{f.domain[:28]}{('-'+f.scenario) if f.scenario else ''}"[:31]
            df.to_excel(xw, sheet_name=sheet or f.domain, index=False)
```

#### **Checkpoint 5E**

```bash
poetry run python - <<'PY'
import openpyxl, pathlib
wb=openpyxl.load_workbook("artefacts/forms.xlsx")
print("Sheets:", wb.sheetnames[:3])
PY
```

---

## **5 F – ODM XML (minimal)**

`src/crfgen/exporter/odm.py`

```python
from pathlib import Path
from typing import List
from odmlib.odm_1_3 import odm_element_factory
from ..schema import Form
from .registry import register

@register("odm")
def render_odm(forms: List[Form], out_dir: Path):
    odm = odm_element_factory("ODM")
    odm.set_attribute("Description", "Generated CRFs")
    study = odm.new_element("Study")
    study.set_attribute("OID", "ST.CRFGEN")
    mdv = study.new_element("MetaDataVersion")
    mdv.set_attribute("OID", "MDV.1")
    for f in forms:
        formdef = mdv.new_element("FormDef")
        formdef.set_attribute("OID", f"F.{f.domain}")
        formdef.set_attribute("Name", f.title)
    out_dir.mkdir(exist_ok=True, parents=True)
    (out_dir / "forms.odm.xml").write_text(odm.to_xml())
```

#### **Checkpoint 5F**

```bash
grep "<FormDef" artefacts/forms.odm.xml | head
```

Should list `<FormDef OID="F.VS" …>` etc.

---

## **5 G – Registry import side-effects**

Make sure **`scripts/build.py`** imports every exporter once:

```python
import crfgen.exporter.markdown   # noqa
import crfgen.exporter.latex      # noqa
import crfgen.exporter.docx       # noqa
import crfgen.exporter.csv        # noqa
import crfgen.exporter.xlsx       # noqa
import crfgen.exporter.odm        # noqa
```

*(We already did earlier, but confirm all six.)*

---

## **5 H – Unit tests for exporters**

`tests/test_exporters.py`

```python
import pathlib, json, tempfile
from crfgen.schema import Form
from crfgen.exporter import registry as reg
import importlib

# import exporters so they register
for m in ("markdown","latex","csv"):
    importlib.import_module(f"crfgen.exporter.{m}")

forms = [Form(**json.load(open("tests/.data/sample_crf.json"))[0])]

def _tmpdir():
    return pathlib.Path(tempfile.mkdtemp())

def test_md():
    out=_tmpdir(); reg.get("md")(forms, out)
    assert any(out.glob("*.md"))

def test_csv():
    out=_tmpdir(); reg.get("csv")(forms, out)
    assert (out/"forms.csv").exists()
```

Run:

```bash
poetry run pytest -q
```

**Checkpoint 5H** – All exporter tests pass.

---

## **5 I – End-to-end manual build**

```bash
export CDISC_API_KEY=YOURTOKEN
poetry run scripts/build_canonical.py -o crf.json
poetry run scripts/build.py --outdir artefacts
tree artefacts | head
```

You should see:

```
├─ VS.md
├─ VS.tex
├─ VS.docx
├─ forms.csv
├─ forms.xlsx
└─ forms.odm.xml
```

**Checkpoint 5I** – All six formats present and non-empty (> 0 B).

---

## **Phase 5 complete – exit criteria**

| Criterion                                       | Evidence                                                                                     |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Each exporter writes file(s) without exceptions | Manual run (Checkpoint 5I)                                                                   |
| Unit tests green                                | `pytest -q` passes incl. exporter tests                                                      |
| Pandoc not found → friendly error               | Uninstall Pandoc locally & try DOCX exporter – should raise `FileNotFoundError` with message |
| Styles overridable                              | Replace `style/reference.docx`, regenerate – DOCX adopts styles                              |

## Phase 6 – Exporter Registry

* [ ] Create `src/crfgen/exporter/registry.py` with `register()`, `get()`, `formats()`

## **Phase 6 – Build Dispatcher CLI**

*Objective: wire up a single "build" script (`scripts/build.py`) that reads `crf.json`, invokes all registered exporters, and writes to an `artefacts/` directory. We’ll validate both manually and via a unit test.*

---

### 6.0  Ensure preconditions

* You’ve completed Phases 1–5.
* `crf.json` exists (from Phase 4).
* `scripts/` directory exists and is on PATH in CI.

**Checkpoint 6-0**

```bash
ls scripts build_canonical.py
test -f src/crfgen/exporter/registry.py
```

No errors.

---

### 6.1  Create `scripts/build.py`

```bash
cat > scripts/build.py <<'EOF'
#!/usr/bin/env python3
"""
Dispatch to each exporter to generate all formats from crf.json.
"""
import sys, json, importlib
from pathlib import Path
from crfgen.schema import Form
from crfgen.exporter import registry as reg

# Import exporters to register them
import crfgen.exporter.markdown  # noqa
import crfgen.exporter.latex     # noqa
import crfgen.exporter.docx      # noqa
import crfgen.exporter.csv       # noqa
import crfgen.exporter.xlsx      # noqa
import crfgen.exporter.odm       # noqa

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--source", "-s", default="crf.json",
                   help="Path to the canonical JSON")
    p.add_argument("--outdir", "-o", default="artefacts",
                   help="Directory to emit artifacts")
    p.add_argument("--formats", "-f", nargs="+",
                   default=reg.formats(),
                   help="Which formats to generate")
    args = p.parse_args()

    src = Path(args.source)
    if not src.exists():
        sys.exit(f"ERROR: source file not found: {src}")

    with src.open() as fp:
        data = json.load(fp)
    forms = [Form(**d) for d in data]

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for fmt in args.formats:
        fn = reg.get(fmt)
        print(f"[build] Rendering {fmt} → {outdir}")
        fn(forms, outdir)

if __name__ == "__main__":
    main()
EOF
```

Make it executable:

```bash
chmod +x scripts/build.py
```

**Checkpoint 6-1**

```bash
head -n 5 scripts/build.py
# should show the shebang and docstring
```

---

### 6.2  Manual smoke-test

Use the sample fixture:

```bash
poetry run scripts/build.py \
  --source tests/.data/sample_crf.json \
  --outdir tmp_artifacts \
  --formats md csv tex
```

**Checkpoint 6-2**

```bash
ls tmp_artifacts
# Expect: DM.md  -- or whatever domain in fixture
#         forms.csv
#         DM.tex
```

Open one briefly:

```bash
head tmp_artifacts/DM.md
```

---

### 6.3  Unit test for the build CLI

Create **`tests/test_build_cli.py`**:

```python
import subprocess, sys, pathlib
import pytest

@pytest.mark.parametrize("fmt", [["md"], ["csv"], ["md","csv"]])
def test_build_cli(tmp_path, fmt):
    # Run build.py with the mini fixture
    cmd = [
        sys.executable,
        "scripts/build.py",
        "--source", "tests/.data/sample_crf.json",
        "--outdir", str(tmp_path),
        "--formats", *fmt
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

    # Check output files exist
    for f in fmt:
        if f == "md":
            assert any(tmp_path.glob("*.md"))
        elif f == "csv":
            assert (tmp_path / "forms.csv").exists()
        elif f == "tex":
            assert any(tmp_path.glob("*.tex"))
```

**Checkpoint 6-3**

```bash
poetry run pytest tests/test_build_cli.py -q
```

Should see all parameterized runs pass.

---

### 6.4  Integrate into CI

In **`.github/workflows/ci.yml`**, after the crawl step, replace individual calls with:

```yaml
      - name: Build all formats
        run: |
          poetry run scripts/build.py --source crf.json --outdir artefacts
```

Ensure that step runs *after* `build_canonical.py`.

**Checkpoint 6-4**
Trigger a PR or push to main; confirm in Actions log that:

```
[build] Rendering md → artefacts
[build] Rendering tex → artefacts
...
```

and that the `artefacts/` directory is populated in the uploaded artifact.

---

### 6.5  Commit & push

```bash
git add scripts/build.py tests/test_build_cli.py
git commit -m "Phase 6: add build dispatcher CLI + tests"
git push
```

---

## **Phase 6 complete**

* **scripts/build.py** exists, executable, and imports all exporters.
* Manual and automated tests verify the CLI correctly writes selected formats.
* CI pipeline updated to invoke one command to generate all artifacts.

## **Phase 7 – Linting, Formatting, and CI Quality Gates**

*Objective: enforce consistent code style, catch errors early, and surface lint/test failures in CI.*

---

### **7.0  Confirm dev dependencies**

Ensure the following are in your `pyproject.toml` under `[tool.poetry.group.dev.dependencies]`:

```toml
black = "^24.0"
ruff = "^0.5.0"
isort = "^5.12.0"
pre-commit = "^4.0"
pytest = "^8.0"
pytest-cov = "^5.0"
```

**Checkpoint 7-0**

```bash
poetry show black ruff isort pre-commit pytest
```

You should see each package listed with its version.

---

### **7.1  Create Pre-commit configuration**

Add **`.pre-commit-config.yaml`** at the repo root:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.12.0
    hooks:
      - id: isort
        args: ["--profile=black"]

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.5.3
    hooks:
      - id: ruff
        args: ["--max-line-length=88"]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
```

**Checkpoint 7-1**

```bash
git add .pre-commit-config.yaml
pre-commit run --all-files
```

No errors or failures (it may auto-fix some files).

---

### **7.2  Install and validate hooks locally**

```bash
poetry run pre-commit install
```

Now, every `git commit` will run Black, isort, Ruff, and the basic hooks.

**Checkpoint 7-2**

```bash
# Make a trivial change that violates style, e.g. add "x=1" to README.md, then:
git add README.md
git commit -m "style test"
```

You should see Black/isort/Ruff run and either pass or auto-fix (blocking commit if errors remain).

---

### **7.3  Enforce in CI**

Update **`.github/workflows/ci.yml`**, adding a **“Lint & Format”** step before tests:

```yaml
    steps:
      - uses: actions/checkout@v4

      - name: Install Poetry
        uses: snok/install-poetry@v1

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Poetry install (dev deps)
        run: poetry install

      - name: Pre-commit checks
        run: poetry run pre-commit run --all-files --show-diff-on-failure

      - name: Run tests
        run: poetry run pytest -q --cov=crfgen
```

> **Tip:** if you prefer separate lint + format steps, replace the “Pre-commit” step with:
>
> ```yaml
> - name: Lint (Ruff)
>   run: poetry run ruff src tests
> - name: Format check (Black & isort)
>   run: |
>     poetry run black --check src tests
>     poetry run isort --check-only src tests
> ```

**Checkpoint 7-3**
Push a trivial style violation commit (e.g. remove a space) to trigger CI.

* The **pre-commit** step should fail, blocking the merge until style is fixed.
* Fix locally, commit, and see CI green.

---

## **Phase 7 complete**

* **Local**: Pre-commit hooks enforce Black, isort, Ruff, and basic checks on every commit.
* **CI**: The same checks run on all branches & PRs, preventing style or lint regressions.
* **Tests**: `pytest` continues to validate functionality immediately after lint/format checks.

## Phase 7 – Exporters

* [ ] Markdown: `src/crfgen/exporter/markdown.py`
* [ ] DOCX: `src/crfgen/exporter/docx.py` (requires Pandoc)
* [ ] LaTeX: `src/crfgen/exporter/latex.py`
* [ ] CSV: `src/crfgen/exporter/csv.py`
* [ ] XLSX: `src/crfgen/exporter/xlsx.py`
* [ ] ODM-XML: `src/crfgen/exporter/odm.py`
* [ ] Verify each exporter via `scripts/build.py --formats <fmt>`

## Phase 8 – Build dispatcher CLI

* [ ] Create `scripts/build.py` to load `crf.json`, call all exporters
* [ ] `chmod +x scripts/build.py`
* [ ] Test manually: `poetry run scripts/build.py --formats md csv`

## Phase 9 – Minimal tests

* [ ] Add fixture `tests/.data/mini_crf.json`
* [ ] Write `tests/test_schema.py`
* [ ] Write `tests/test_export_md.py`
* [ ] Run `poetry run pytest -q`

## Phase 10 – Pre-commit hooks

* [ ] Create `.pre-commit-config.yaml` (Black, isort, Ruff, EOF fixer)
* [ ] Run `poetry run pre-commit install`
* [ ] Commit and verify hooks fire

## Phase 11 – GitHub Actions CI

* [ ] Create `.github/workflows/ci.yml` with steps:

  * checkout, setup-Python, install Poetry
  * lint (ruff), format check (black), tests
  * install Pandoc
  * `build_canonical.py` → `crf.json`
  * `build.py` → `artefacts/`
  * upload artefacts
* [ ] Push and confirm green build + downloadable artefacts

## Phase 12 – Weekly sync workflow

* [ ] Create `.github/workflows/weekly-sync.yml` (cron + dispatch)
* [ ] Add GitHub secret `GH_TOKEN` if needed
* [ ] Manual dispatch to verify no-change run
* [ ] Edit `crf.json`, dispatch to verify PR creation

## Phase 13 – Release flow

* [ ] Bump version in `pyproject.toml`
* [ ] `git tag vX.Y.Z && git push origin vX.Y.Z`
* [ ] *(Optional)* Create `.github/workflows/release.yml` to zip & attach artefacts

## Phase 14 – Documentation polish

* [ ] In `README.md`, add **Environment Variables** table
* [ ] In `README.md`, add **Regenerating the OpenAPI Client** snippet
* [ ] In `README.md`, add **CLI Usage Examples**
* [ ] Create `CHANGELOG.md` with `[Unreleased]` section
* [ ] Add regeneration guide to MkDocs (`docs/regeneration.md`, update `mkdocs.yml`)
* [ ] Commit all docs changes

---

## **Overall Acceptance**

* Every item above completed
* All checkpoints passed
* CI/CD pipelines are green
* Weekly sync runs automatically
* Release artifacts published on tagging

Once every box is ticked, your **14-phase build** is fully done! 🎉