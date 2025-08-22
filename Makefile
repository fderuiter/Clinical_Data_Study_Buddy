# Makefile for cdisc-crf-generator

# Phony targets
.PHONY: init clean build-json build-all test fmt docs

# Default target
all: build-all

init:
	poetry install

clean:
	rm -rf artefacts/ crf.json

build-json:
	poetry run scripts/build_canonical.py -o crf.json

build-all:
	poetry run scripts/build.py --source crf.json --outdir artefacts

test:
	poetry run pytest

fmt:
	poetry run black .
	poetry run ruff check . --fix
	poetry run isort .

docs:
	poetry run mkdocs serve
