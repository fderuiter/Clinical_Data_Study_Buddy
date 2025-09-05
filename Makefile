# Makefile for cdisc-crf-generator

# Phony targets
.PHONY: init clean build-json build-all test fmt docs help

# Default target
all: build-all

help:
	@echo "Makefile for cdisc-crf-generator"
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  init              Install dependencies"
	@echo "  clean             Remove generated files"
	@echo "  update-spec       Download the latest CDISC Library spec"
	@echo "  generate-client   Generate the CDISC Library client"
	@echo "  update-sdk        Update the spec and generate the client"
	@echo "  build-json        Build the canonical JSON from the spec using the CLI"
	@echo "  build-all         Build all artifacts from the canonical JSON using the CLI"
	@echo "  test              Run tests"
	@echo "  fmt               Format the code"
	@echo "  docs              Serve the documentation"


init: ## Install dependencies
	poetry install

clean: ## Remove generated files
	rm -rf artefacts/ crf.json

update-spec: ## Download the latest CDISC Library spec
	poetry run python build_scripts/download_spec.py

generate-client: ## Generate the CDISC Library client
	poetry run python build_scripts/generate_client.py

update-sdk: update-spec generate-client ## Update the spec and generate the client

build-json: ## Build the canonical JSON from the spec
	poetry run cdisc build build-canonical

build-all: ## Build all artifacts from the canonical JSON
	poetry run cdisc build

test: ## Run tests
	poetry run pytest

fmt: ## Format the code
	poetry run black .
	poetry run ruff check . --fix
	poetry run isort .

docs: ## Serve the documentation
	poetry run mkdocs serve
