---
title: "Enhance CI/CD Pipeline with PR Checks"
state: "open"
labels:
  - "enhancement"
  - "ci-cd"
assignees: []
---

### Description

The project currently has a `Makefile` with targets for formatting (`fmt`) and testing (`test`), but these checks are not automatically enforced in the CI/CD pipeline. To improve code quality and prevent regressions, a new GitHub Actions workflow should be created to run on every pull request.

### Proposed Solution

1.  **Create a new GitHub Actions workflow file:**
    *   Create a new file at `.github/workflows/pr-checks.yml`.

2.  **Define the workflow trigger:**
    *   The workflow should trigger on `pull_request` events targeting the main branch.

3.  **Define the job steps:**
    *   **Checkout Code:** Use the `actions/checkout@v3` action.
    *   **Set up Python:** Use the `actions/setup-python@v4` action to install Python 3.12.
    *   **Set up Poetry:** Use the `snok/install-poetry@v1` action or a similar community action to install Poetry.
    *   **Install Dependencies:** Run `poetry install` to install all project dependencies. This step should be cached to improve performance.
    *   **Run Linter/Formatter Check:** Run `make fmt`. This command should be configured to run in a check-only mode if possible (e.g., `black --check .`). If not, the workflow should check for any file changes after running the command and fail if there are any.
    *   **Run Tests:** Run `make test` to execute the `pytest` test suite.

### Acceptance Criteria

-   A new GitHub Actions workflow is created.
-   The workflow runs automatically on all pull requests.
-   The workflow fails if the linter/formatter check fails.
-   The workflow fails if any tests fail.
-   The workflow passes on the current state of the main branch.
