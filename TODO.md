# TODO

## Key Initiatives

- [ ] **Fully transition to CDISC Library API:** The primary goal is to phase out the old web crawler and use the generated API client for all data standard interactions. This will involve updating existing scripts and potentially creating new ones to leverage the full power of the API.
- [ ] **Enhance CRF Generation:** Improve the CRF generation capabilities with more customization options and support for more complex forms.
- [ ] **Expand Synthetic Data Generation:** Increase the realism and coverage of the synthetic data generator.

## Detailed Task List

### Core Development

- [x] **[API Integration]** Integrate with the CDISC Library API by generating a Python client from the OpenAPI specification.
- [ ] **[API Integration]** Replace the existing web crawler (`src/crfgen/crawl.py`) with API calls to the CDISC Library.
- [ ] **[Data Standards]** Automate the download and storage of CDISC data standards from the CDISC website or API.
- [ ] **[CRF Generation]** Refactor CRF generation logic to work exclusively with data from the CDISC Library API.
- [ ] **[Synthetic Data]** Enhance the synthetic data generator to use the full breadth of information available from the API.

### Completed Tasks

- [x] **[Data Standards]** Manually download and store the CDISC data standards.
- [x] **[CRF Generation]** Implement a web crawler to extract CRF metadata.
- [x_] **[CRF Generation]** Develop a schema for storing the extracted CRF metadata.
- [x] **[CRF Generation]** Create a script to generate CRFs in various formats (e.g., CSV, DOCX, Markdown).
- [x] **[Synthetic Data]** Generate synthetic data based on the CRF metadata.
- [x] **[Tooling]** Create a CLI for generating CRFs and synthetic data.

### Ongoing Tasks

- [ ] **[Testing]** Add comprehensive tests for all components, especially for the new API-driven functionality.
- [ ] **[Documentation]** Improve documentation for all modules, including a guide on how to use the CDISC Library API client.
