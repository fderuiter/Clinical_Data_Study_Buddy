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

## Phase 4 – Crawler (Library → Forms)

* [ ] Create `src/crfgen/http.py` for cached GET + retry
* [ ] Create `src/crfgen/crawl.py` with `harvest(token, version_filter)` & `write_json()`
* [ ] Create CLI wrapper `scripts/build_canonical.py`
* [ ] `chmod +x scripts/build_canonical.py`
* [ ] Run crawl locally (`poetry run scripts/build_canonical.py -v 2-2`) and inspect `crf.json`

## Phase 5 – Templates

* [ ] Create `src/crfgen/templates/markdown.j2`
* [ ] Create `src/crfgen/templates/latex.j2`

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
