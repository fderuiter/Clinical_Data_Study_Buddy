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
