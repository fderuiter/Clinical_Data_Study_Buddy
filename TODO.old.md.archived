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

* [ ] Run `poetry init` using non-interactive options:

  ```bash
  poetry init --name cdisc-crf-generator \
    --description "Generate CRFs from CDISC Library" \
    --author "You <you@example.com>" \
    --license "Apache-2.0" \
    --python ">=3.11,<4.0"
  ```

* [ ] Edit `pyproject.toml` and add the dependencies:

  ```toml
  [tool.poetry.dependencies]
  python = ">=3.11,<4.0"
  openapi-python-client = "^0.19.0"
  jinja2 = "^3.1"
  pydantic = "^2.7"
  requests = "^2.32"
  pandas = "^2.2"
  openpyxl = "^3.1"
  python-docx = "^1.1"
  odmlib = "^0.9"

  [tool.poetry.group.dev.dependencies]
  black = "^24.0"
  ruff = "^0.5.0"
  pytest = "^8.0"
  pytest-cov = "^5.0"
  pre-commit = "^4.0"
  ```

* [ ] Install the environment:

  ```bash
  poetry install
  ```

* [ ] **Checkpoint 1** – verify basic imports:

  ```bash
  poetry run python -c "import pandas, jinja2; print('ok')"
  ```

  Should print `ok` without error.

## Phase 2 – Bring the official CDISC Library OpenAPI spec into your project

*(all commands run from the repo root; assume Poetry is already initialised per Phase 1)*

### **2.0  Create a home for the spec**

```bash
mkdir -p openapi
```

### **2.1  Download the spec (JSON flavour)**

CDISC now publishes the Swagger / OAS 3 definition openly:

```bash
curl -L \
  -o openapi/cdisc-library.json \
  https://www.cdisc.org/system/files/cdisc_library/api_documentation/CDISC1-share-2.0-1.1.0-swagger.json
```

> *Tip:* add the second URL – <https://www.cdisc.org/cdisc-library/api-documentation/oas3> – to your bookmarks; CDISC updates it whenever a new IG or endpoint ships.

### **2.2  Optional – Convert JSON → YAML (makes diffs easier)**

`openapi-python-client` accepts either format, but YAML is human-friendlier for reviews.

```bash
poetry run python - <<'PY'
import json, yaml, pathlib, sys, os
raw = json.load(open("openapi/cdisc-library.json"))
yaml.safe_dump(raw, open("openapi/cdisc-library.yaml", "w"), sort_keys=False)
PY
```

Delete the original JSON if you prefer to version just one file.

### **2.3  Generate a typed Python client**

```bash
poetry run openapi-python-client generate \
   --path openapi/cdisc-library.yaml \
   --meta none \
   --config '{"package_name":"cdisc_library_client","project_name":"cdisc_library_client","package_version":"0.1.0"}'
```

* The tool creates a new directory **`cdisc_library_client/`** plus a `README.md`.
* No `pyproject.toml` is generated because we passed `--meta none`; we’ll vendor the code directly.

### **2.4  Move the generated package into `src/`**

```bash
mv cdisc_library_client src/
```

Your tree now looks like

```
src/
  ├─ cdisc_library_client/   ← <generated code>
  └─ crfgen/
openapi/
  └─ cdisc-library.yaml
```

### **2.5  Tell Poetry where to find the new code**

Edit **`pyproject.toml`** and add the package to the `[tool.poetry.packages]` table:

```toml
[tool.poetry.packages]
cdisc_library_client = { from = "src", include = "cdisc_library_client" }
crfgen                = { from = "src", include = "crfgen" }
```

### **2.6  Re-install the local environment**

```bash
poetry install
```

Poetry now puts the generated client on the editable path.

### **Checkpoint 2 – Smoke-test the client**

```bash
poetry run python - <<'PY'
from cdisc_library_client import Client
print("Generated client OK - base_url is:", Client.base_url)
PY
```

You should see something like:

```
Generated client OK - base_url is: https://library.cdisc.org/api
```

*(No HTTP call is made yet; we’re only confirming importability.)*

### **2.7  Commit the spec and generated client**

```bash
git add openapi/cdisc-library.yaml src/cdisc_library_client
git commit -m "Add CDISC Library OpenAPI spec and generated client"
```

*(If your repo uses Git LFS, add the YAML to `.gitattributes` now.)*

### **2.8  Future updates**

Whenever CDISC ships a new version:

```bash
curl -L -o openapi/cdisc-library.yaml <new-url>
poetry run openapi-python-client generate \
        --path openapi/cdisc-library.yaml --meta none \
        --config '{"package_name":"cdisc_library_client"}'
mv -f cdisc_library_client src/
poetry install
git add openapi/cdisc-library.yaml src/cdisc_library_client
git commit -m "Refresh API spec & client to <yyyy-mm-dd>"
```

CI will run and your crawler tests (added in later phases) will catch any breaking field changes.

**Phase 2 is now fully flushed-out, verified against the publicly hosted Swagger JSON, and ends with a working typed client inside your Poetry environment.**

## **Phase 3 – Domain-model layer (Pydantic)**

*The goal of this phase is to design, implement, and verify typed Python classes that will serve as the in-memory “schema” for everything downstream (crawler, exporters, tests).*

> **Prerequisite** – Phase 2 is complete and `poetry install` works.

### **3.0  Create the module scaffold**

```bash
mkdir -p src/crfgen
touch src/crfgen/__init__.py
```

**Checkpoint 3-0**

```bash
poetry run python - <<'PY'
import importlib, pathlib, sys, pkg_resources, inspect
print("crfgen import OK")
PY
```

Expected: `crfgen import OK`

### **3.1  Define atomic helper models**

Create **`src/crfgen/schema.py`**

```python
from __future__ import annotations
from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class Codelist(BaseModel):
    """Reference to an external controlled-terminology list."""
    nci_code: str = Field(..., pattern=r"^C\d+$")
    href: str

class DataType(str):
    """CDASH datatype subset we care about."""
    # Not using Enum to keep it open; we validate later
    pass

ALLOWED_DT = {"text", "integer", "float", "date", "datetime", "boolean"}

class FieldDef(BaseModel):
    oid: str
    prompt: str
    datatype: DataType
    cdash_var: str
    codelist: Optional[Codelist] = None
    control: Optional[Literal["radio", "checkbox"]] = None

    # Extra validation step
    @classmethod
    def validate_datatype(cls, value: str) -> str:
        if value.lower() not in ALLOWED_DT:
            raise ValueError(f"Datatype {value} not in {ALLOWED_DT}")
        return value.lower()

    _normalise_dt = Field(alias="datatype", pre=True)(validate_datatype)
```

**Checkpoint 3-1**

```bash
poetry run python - <<'PY'
from crfgen.schema import FieldDef, Codelist
fd = FieldDef(
    oid="VSORRES",
    prompt="Result",
    datatype="text",
    cdash_var="VSORRES",
    codelist=Codelist(nci_code="C85491", href="http://example.com")
)
print(fd.model_dump()["datatype"])
PY
```

Expected: `text`

### **3.2  Form-level model**

Append to `schema.py`:

```python
class Form(BaseModel):
    title: str
    domain: str
    scenario: Optional[str] = None
    fields: List[FieldDef]

    def field_oids(self) -> List[str]:
        return [f.oid for f in self.fields]
```

**Checkpoint 3-2**

```bash
poetry run python - <<'PY'
from crfgen.schema import Form, FieldDef
fm = Form(
    title="Vital Signs",
    domain="VS",
    fields=[FieldDef(oid="VSORRES", prompt="Res", datatype="text", cdash_var="VSORRES")]
)
assert fm.field_oids() == ["VSORRES"]
print("Form OK")
PY
```

Expected: `Form OK`

### **3.3  Utility:  convert from generated client payload**

Create **`src/crfgen/converter.py`**

```python
"""
Helpers to translate CDISC Library client DTOs -> crfgen.schema objects.
"""

from typing import Any
from crfgen.schema import Form, FieldDef, Codelist

def field_from_api(f: Any) -> FieldDef:
    cl = (
        Codelist(nci_code=f.codelist.nci_code, href=f.codelist.href)
        if getattr(f, "codelist", None) else None
    )
    return FieldDef(
        oid=f.cdash_variable,
        prompt=f.prompt,
        datatype=f.datatype,
        cdash_var=f.cdash_variable,
        codelist=cl,
    )

def form_from_api(payload: Any) -> Form:
    return Form(
        title=payload.title,
        domain=payload.domain,
        scenario=getattr(payload, "scenario", None),
        fields=[field_from_api(f) for f in payload.fields],
    )
```

**Checkpoint 3-3**

```bash
poetry run python - <<'PY'
from crfgen.converter import form_from_api
class FakeField:
    def __init__(self):
        self.cdash_variable="TEST"; self.prompt="Q"; self.datatype="text"; self.codelist=None
class FakePayload:
    title="Demo"; domain="DM"; scenario=None; fields=[FakeField()]
demo = form_from_api(FakePayload)
print(demo.domain, demo.fields[0].oid)
PY
```

Expected: `DM TEST`

### **3.4  Serialization helpers**

Add to `schema.py` bottom:

```python
import json, pathlib
from typing import Iterable

def dump_forms(forms: Iterable[Form], path: str | pathlib.Path):
    data = [f.model_dump() for f in forms]
    pathlib.Path(path).write_text(json.dumps(data, indent=2))

def load_forms(path: str | pathlib.Path) -> List[Form]:
    raw = json.loads(pathlib.Path(path).read_text())
    return [Form(**d) for d in raw]
```

**Checkpoint 3-4**

```bash
poetry run python - <<'PY'
from crfgen.schema import Form, FieldDef, dump_forms, load_forms
tmp="tests/.data/tmp.json"
forms=[Form(title="x",domain="DM",fields=[FieldDef(oid="ID",prompt="ID",datatype="text",cdash_var="ID")])]
dump_forms(forms,tmp); r=load_forms(tmp); print(len(r), r[0].domain)
PY
```

Expected: `1 DM`

### **3.5  Unit tests**

Create **`tests/test_schema_roundtrip.py`**

```python
from crfgen.schema import Form, FieldDef, dump_forms, load_forms
import tempfile, pathlib

def test_roundtrip():
    f = Form(
        title="VS",
        domain="VS",
        fields=[FieldDef(oid="VSORRES", prompt="Res", datatype="text", cdash_var="VSORRES")]
    )
    tmp = pathlib.Path(tempfile.mkdtemp()) / "tmp.json"
    dump_forms([f], tmp)
    out = load_forms(tmp)
    assert out[0].title == "VS"
```

Run:

```bash
poetry run pytest -q
```

**Checkpoint 3-5**
Output should be:

```
.
1 passed in X.XXs
```

### **Phase 3 Complete**

**Artifacts produced**

* `src/crfgen/schema.py` – canonical Pydantic models + JSON helpers
* `src/crfgen/converter.py` – API-payload → model translators
* Unit tests proving instantiation and round-trip serialization

Phase 4 (Crawler) can now consume these models with confidence.

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
## Phase 8 – Governance & Release Management

*Objective: set up project-wide policies, templates, automation, and release workflows to ensure clear ownership, smooth collaboration, and robust security practices.*

---

### 8.1 Add a CODEOWNERS file

**Path:** `.github/CODEOWNERS`

```text
# Require review from the crfgen-maintainers team on all changes
*       @your-org/crfgen-maintainers

# Specialists: review HTTP or API changes
src/crfgen/http.py   @your-org/api-team
```

**Checkpoint 8-1**

```bash
ls -1 .github/CODEOWNERS && head -n 3 .github/CODEOWNERS
```

---

### 8.2 Issue & Pull Request templates

#### 8.2.1 Issue templates

**Paths:**

* `.github/ISSUE_TEMPLATE/bug_report.md`
* `.github/ISSUE_TEMPLATE/feature_request.md`

**`bug_report.md`:**

```markdown
---
name: Bug report
about: Report a problem in the CDISC CRF generator pipeline
title: "[BUG] "
labels: bug
assignees: ''

---
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. ...
2. ...
3. `poetry run scripts/build_canonical.py ...`
4. `poetry run scripts/build.py ...`

**Expected behavior**
What you expected to happen.

**Environment (please complete the following information):**
- OS: [e.g. Ubuntu 22.04]
- Python version: [e.g. 3.11.5]
- Poetry version: [e.g. 1.8.0]

**Additional context**
Add any other context about the problem here.
```

**`feature_request.md`:**

```markdown
---
name: Feature request
about: Suggest an enhancement for the CRF generator
title: "[FEATURE] "
labels: enhancement
assignees: ''

---
**Is your feature request related to a problem? Please describe.**

**Describe the solution you'd like**

**Describe alternatives you've considered**

**Additional context**
```

**Checkpoint 8-2**

```bash
ls -1 .github/ISSUE_TEMPLATE | sed -e '1,2!d'
```

#### 8.2.2 Pull Request template

**Path:** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## Description
Please include a summary of the change and the motivation.

## Related issue
Closes #<issue number>

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change

## Checklist
- [ ] My code follows project style (black, isort, ruff)
- [ ] I added tests and they pass
- [ ] I updated documentation if needed
```

**Checkpoint 8-3**

```bash
head -n 5 .github/PULL_REQUEST_TEMPLATE.md
```

---

### 8.3 Automated dependency updates (Dependabot)

**Path:** `.github/dependabot.yml`

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "github-actions"
    directory: "/.github/workflows"
    schedule:
      interval: "weekly"
```

**Checkpoint 8-4**

```bash
grep -R "package-ecosystem" .github/dependabot.yml
```

---

### 8.4 Security scanning with CodeQL

**Path:** `.github/workflows/codeql-analysis.yml`

```yaml
name: CodeQL Analysis

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    strategy:
      fail-fast: false
      matrix:
        language: [ "python" ]
    steps:
      - uses: actions/checkout@v4
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}
      - name: Autobuild
        uses: github/codeql-action/autobuild@v2
      - name: Analyze
        uses: github/codeql-action/analyze@v2
```

**Checkpoint 8-5**

```bash
ls .github/workflows | grep codeql-analysis.yml
```

---

### 8.5 Release automation

**Path:** `.github/workflows/release.yml`

```yaml
name: Release Artefacts

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build_release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Poetry
        uses: snok/install-poetry@v1

      - name: Install dependencies
        run: poetry install --no-dev

      - name: Generate CRF JSON
        env:
          CDISC_API_KEY: ${{ secrets.CDISC_API_KEY }}
        run: poetry run scripts/build_canonical.py -o crf.json

      - name: Build all formats
        run: poetry run scripts/build.py --outdir artefacts

      - name: Archive artefacts
        run: zip -r artefacts.zip artefacts/

      - name: Upload release asset
        uses: softprops/action-gh-release@v1
        with:
          tag_name: ${{ github.ref_name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Upload ZIP
        uses: softprops/action-gh-release@v1
        with:
          tag_name: ${{ github.ref_name }}
          asset_path: artefacts.zip
          asset_name: crf-artefacts-${{ github.ref_name }}.zip
          asset_content_type: application/zip
```

**Checkpoint 8-6**

```bash
grep -R "push:" .github/workflows/release.yml
```

---

### 8.6 Repository metadata & policies

Create **`CONTRIBUTING.md`**:

````markdown
# Contributing

1. Fork the repo & create a feature branch from main.
2. Ensure the code passes `pre-commit` locally:
   ```bash
   poetry install
   poetry run pre-commit run --all-files
   ```

3. Write tests and update docs.
4. Submit a pull request using the PR template.
````

Create **`CODE_OF_CONDUCT.md`** (Contributor Covenant excerpt):

```markdown
# Contributor Covenant Code of Conduct

…[standard text]…
````

Create **`SECURITY.md`**:

```markdown
# Security Policy

Report vulnerabilities to security@your-org.org. We will respond within 3 business days.
```

**Checkpoint 8-7**

```bash
ls CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
```

---

### 8.7 Branch protection & repository settings

> *This step is manual or via the GitHub CLI.*

1. **Protect `main` branch**:

   * Require pull-request reviews before merging (at least 1 approval).
   * Require status checks: `lint-test-build`, `CodeQL Analysis`.
   * Include administrators.
2. **Enforce signed commits** (optional).

**Checkpoint 8-8**
In your repo **Settings → Branches → Branch protection rules**, verify the above policies are active.

---

## **Phase 8 complete**

* CODEOWNERS, issue/PR templates, contributing guides, and security policies are in place.
* Dependabot and CodeQL scanning run automatically.
* Release workflow builds & publishes artefacts on tag.
* Branch protection enforces reviews and CI checks.

## Phase 9 – Scheduled Library Sync & Auto-Update PRs

*Objective: keep your `crf.json` canon in sync with CDISC Library on a regular cadence, creating a PR whenever new or changed forms appear.*

### 9.1  Add the sync workflow file

**Path:** `.github/workflows/weekly-sync.yml`

```yaml
name: Weekly CDISC Library Sync

# Run every Monday at 04:00 UTC, plus manually via workflow_dispatch
on:
  schedule:
    - cron: "0 4 * * 1"
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    permissions:
      contents: write      # for creating branches & PRs
      pull-requests: write # for creating PRs
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Poetry
        uses: snok/install-poetry@v1

      - name: Install dependencies
        run: poetry install --no-root

      - name: Crawl CDISC Library → crf.json
        env:
          CDISC_API_KEY: ${{ secrets.CDISC_API_KEY }}
        run: poetry run scripts/build_canonical.py -o crf.json

      - name: Check for crf.json changes
        id: diff
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          # If crf.json changed, exit 1 so next step runs
          git diff --exit-code crf.json

      - name: Create Pull Request
        if: failure() && github.event_name != 'workflow_dispatch'
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GH_TOKEN }}
          commit-message: "chore: weekly CDISC Library sync"
          branch: "sync/cdisc-${{ github.run_id }}"
          title: "Weekly CDISC Library Sync"
          body: |
            This PR updates `crf.json` with the latest forms from the CDISC Library.
            Review the changes below and merge if everything looks good.
          base: main
```

**Checkpoint 9-1**

```bash
ls .github/workflows/weekly-sync.yml
grep -R "schedule:" .github/workflows/weekly-sync.yml
```

You should see the file and the cron expression.

### 9.2  Add required repository secrets

1. **CDISC_API_KEY** – your Library bearer token (already used by CI).
2. **GH_TOKEN** – a fine-grained GitHub token (or `${{ secrets.GITHUB_TOKEN }}`) with `contents: write` and `pull-requests: write` permissions.

**Checkpoint 9-2**

* In GitHub UI, go to **Settings → Secrets → Actions** and confirm both `CDISC_API_KEY` and `GH_TOKEN` are present.
* Or run (with `gh` CLI):

  ```bash
  gh secret list | grep -E 'CDISC_API_KEY|GH_TOKEN'
  ```

### 9.3  Manual trigger verification

1. Push changes to `main` so weekly-sync job appears in Actions.
2. In the **Actions** tab, select **Weekly CDISC Library Sync** and click **Run workflow**.
3. Choose `main` branch and click **Run workflow**.

**Checkpoint 9-3**

* Observe a new run starting.
* In **Checks**, you should see **`Crawl CDISC Library → crf.json`** succeed and **`Create Pull Request`** skip if no differences.

### 9.4  Simulate a diff to test PR creation

1. Locally, edit `crf.json` (e.g. change a form title).
2. Commit that change on a feature branch and push.
3. Dispatch the workflow manually again.

**Checkpoint 9-4**

* A new branch `sync/cdisc-<run_id>` is created.
* A PR appears titled **Weekly CDISC Library Sync** with your modified `crf.json` as the diff.

### 9.5  Monitor and clean up old sync branches

By default, each run creates a new branch. You may:

* **Auto-merge** trivial PRs via the **merge queue** or **GitHub Actions** after validation.
* **Delete** stale branches manually or via a scheduled cleanup action.

**Checkpoint 9-5**

* In the **Branches** list, confirm sync branches exist.
* Delete one via the GitHub UI or CLI:

  ```bash
  gh pr close <PR-number> && gh repo delete-branch sync/cdisc-<run_id>
  ```

### 9.6  (Optional) Add a badge to README

```markdown
![Weekly Sync Status](https://github.com/<org>/<repo>/actions/workflows/weekly-sync.yml/badge.svg)
```

**Checkpoint 9-6**

* View README in GitHub; the badge shows the latest run status.

---

## **Phase 9 complete**

* A scheduled workflow pulls the latest CDISC CRFs weekly.
* Changes to `crf.json` automatically surface in a pull request for review.
* Secrets and permissions are configured to let the bot create PRs.
* You’ve manually tested both “no diff” and “diff” scenarios.

## Phase 10 – Documentation & Developer Onboarding

### 10.1  Write a “Getting Started” guide in the README

Add a **Quickstart** section showing how to clone the repo, set up a Python 3.11
virtual environment or dev container, configure the `CDISC_API_KEY`, fetch the
latest `crf.json` and generate all artefacts. Include a command to open one of
the generated documents. Verify the block renders correctly on GitHub.

### 10.2  Create a Makefile for common tasks

Add a `Makefile` with targets:

- `init` – create a venv and install dependencies with Poetry
- `clean` – remove build artefacts
- `build-json` – run `scripts/build_canonical.py`
- `build-all` – run `scripts/build.py`
- `test` – run `pytest`
- `fmt` – run Black, isort and Ruff
- `docs` – serve the MkDocs site locally

Run `make build-json build-all test fmt` to ensure each target succeeds.

### 10.3  Add a VS Code Dev Container

Create `.devcontainer/Dockerfile` installing system dependencies, Poetry and the
project itself. Add a matching `devcontainer.json` that builds the image and
runs `make build-json` after creation. Open the project in VS Code using
“Reopen in Container” and run `make build-all` to verify it works.

### 10.4  Generate & publish project docs with MkDocs

Add `mkdocs` and `mkdocs-material` as development dependencies. Create a
`mkdocs.yml` with navigation and pages under `docs/`. Add a GitHub Actions
workflow `.github/workflows/docs.yml` that deploys the site on pushes to `main`.
Run `make docs` locally to preview.

### 10.5  Add badges to the README

Include CI, pre‑commit, weekly sync and docs badges at the top of the README.
Push the change and verify the badges display correctly.

## Phase 11 – GitHub Actions CI

* [ ] Create `.github/workflows/ci.yml` with steps:

  * checkout, setup-Python, install Poetry
  * lint (ruff), format check (black), tests
  * install Pandoc
  * `build_canonical.py` → `crf.json`
  * `build.py` → `artefacts/`
  * upload artefacts
* [ ] Push and confirm green build + downloadable artefacts

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

## Phase 15 – Feature Expansion (inspired by cdiscdataset.com)

*This section outlines potential future features for the generator, expanding its scope from CRF generation to a more comprehensive clinical data generation tool. The generated data is synthetic, intended for testing and educational purposes, and not for regulatory submission.*

---

### **15.1 Dataset Generation (UI)**

*   [ ] **Implement Core Dataset Generator:**
    *   [ ] Generate synthetic, CDISC-compliant datasets for **SDTM**, **ADaM**, and **SEND**.
    *   [ ] **(Enhancement)** Implement advanced cross-domain logic for greater data realism (e.g., linking AEs to MH or CM).
    *   [ ] **(Enhancement)** Add a "learn from example" mode to generate statistically similar data from a user-provided template dataset.
    *   [ ] **(Enhancement)** Add an "imperfect data" simulation mode to intentionally introduce realistic errors for testing validation scripts.

*   [ ] **UI for Dataset Generation:**
    *   [ ] Allow selection of dataset type: SDTM, ADaM, SEND.
    *   [ ] Allow selection of a specific domain from a list of standard domains (e.g., SDTM: DM, AE, LB, VS; ADaM: ADSL, ADAE, ADLB, ADVS, ADTTE; SEND: TS, DM, LB, MI, MA, OM).
    *   [ ] Allow selection of therapeutic area, with condition/terminology presets.
    *   [ ] Allow specification of number of subjects and treatment arms.
    *   [ ] Allow selection of output format.
    *   [ ] **(Enhancement)** Add a "live preview" panel to show a sample of data as parameters are adjusted.
    *   [ ] **(Enhancement)** Allow users to save and load generation settings as named "presets" or "profiles".
    *   [ ] **(Enhancement)** Add an "advanced" UI mode for granular control over variable distributions and correlations.

*   [ ] **Supported Output Formats:**
    *   [ ] CSV.
    *   [ ] SAS Program (`.sas`).
    *   [ ] SAS Transport File (`.xpt`).
    *   [ ] *Future consideration:* CDISC JSON (currently disabled on reference site).
    *   [ ] **(Enhancement)** Add support for efficient formats like **Apache Parquet**.
    *   [ ] **(Enhancement)** Add support for generating data directly into a database (e.g., **PostgreSQL**, **SQLite**).

---

### **15.2 Document & Template Generators**

*   [ ] **Generate EDC Raw Dataset Package:**
    *   [ ] Generate a ZIP file with multiple raw EDC datasets.
    *   [ ] Use consistent subjects across all selected domains.
    *   [ ] Allow user to set number of subjects (e.g., 10-200), therapeutic area, and which datasets to include.
    *   [ ] **(Enhancement)** Allow users to select a "study story" to generate data reflecting specific scenarios (e.g., high dropout rate).
    *   [ ] **(Enhancement)** Include a draft `define.xml` file in the generated package.

*   [ ] **Generate SAS Reference Code:**
    *   [ ] Produce reference SAS code for generating analysis outputs.
    *   [ ] Allow user to choose source dataset (SDTM/ADaM options), output type, and treatment variable (e.g., TRT01A, TRT01P, ARM, ACTARM, or custom).
    *   [ ] Support RTF output format.
    *   [ ] **(Enhancement)** Add support for generating equivalent code in **R** (using `tidyverse`).
    *   [ ] **(Enhancement)** Generate a complete program including data import, manipulation, analysis, and output steps.

*   [ ] **Generate Blank CRFs:**
    *   [ ] Generate blank Case Report Forms for SDTM annotation practice.
    *   [ ] **(Enhancement)** Generate interactive, web-based (HTML) CRFs for a more realistic data entry simulation.
    *   [ ] **(Enhancement)** *[Advanced]* Attempt to auto-generate draft CRFs by parsing a user-uploaded study protocol.

*   [ ] **Generate TFL Shells:**
    *   [ ] Generate Tables, Figures, and Listings mock shell documents.
    *   [ ] Support download in PDF or RTF format.
    *   [ ] **(Enhancement)** Add an option to populate the TFLs with the generated synthetic data.
    *   [ ] **(Enhancement)** Allow customization of TFL style and branding (e.g., logos, colors).

*   [ ] **Generate Specification Templates:**
    *   [ ] Generate Excel-based specification templates for SDTM and ADaM.
    *   [ ] **(Enhancement)** Create a two-way system: generate a dataset from a spec, and validate a dataset against a spec.

*   [ ] **Generate Study Protocols:**
    *   [ ] Generate study protocol documents (Phase 1-4 or custom).
    *   [ ] For custom protocols, take inputs for therapeutic area, treatment arms, and duration.
    *   [ ] **(Enhancement)** Integrate with clinical trial registries (e.g., ClinicalTrials.gov) to use real protocols as templates.
    *   [ ] **(Enhancement)** Generate a visual Gantt chart timeline of the study.

*   [ ] **Investigate ADRG/SDRG Generation:**
    *   [ ] The reference site navigation mentions "Generate ADRG/SDRG", but functionality is unconfirmed. Investigate the purpose and feasibility of this feature.
    *   [ ] **(Enhancement)** If feasible, expand investigation to include other regional standards (e.g., EMA, NMPA).

---

### **15.3 Utility and Supporting Features**

*   [ ] **REST API for Programmatic Access:**
    *   [ ] Expose all generation features through a well-documented REST API.
    *   [ ] Update `openapi.yaml` to include new endpoints.
    *   [ ] Provide comprehensive API documentation.
    *   [ ] **(Enhancement)** Implement **webhook support** for notifying users about the completion of long-running jobs.
    *   [ ] **(Enhancement)** Auto-generate and provide **client libraries** in popular languages (e.g., Python, R) to simplify API usage.
*   [ ] **(Enhancement)** Integrate with the **CDISC Rules Engine** to validate generated datasets.
    *   [ ] After a dataset is generated, automatically run it through the CDISC Rules Engine.
    *   [ ] The engine should be used to validate the dataset against the appropriate standard and version (e.g., SDTMIG v3.4).
    *   [ ] Provide a user-friendly validation report based on the engine's output (JSON or XLSX).
    *   [ ] The UI should clearly present the validation results, including any errors or warnings.

---
