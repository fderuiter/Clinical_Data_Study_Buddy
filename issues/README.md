# Contributor Guide: Working on Issues

This document outlines the structure of the issue files in this directory and provides best practices for tackling the tasks they describe. The goal is to maintain a clear, consistent, and effective workflow for all contributors.

## Issue File Structure

Each issue is a Markdown file with a consistent structure, designed to provide all necessary context at a glance.

### YAML Frontmatter

Every issue file begins with a YAML frontmatter block that contains key metadata:

```yaml
---
title: "A concise, descriptive title of the task"
state: "open" | "in-progress" | "closed"
labels:
  - "bug"
  - "enhancement"
  - "refactoring"
  - "documentation"
assignees:
  - "GitHubUsername"
---
```

-   **`title`**: A brief and clear summary of the task.
-   **`state`**: The current status of the issue.
-   **`labels`**: A list of labels to categorize the issue.
-   **`assignees`**: The person or people responsible for the task.

### Issue Body

The body of the issue is divided into three main sections:

1.  **`### Description`**
    This section provides a detailed explanation of the problem or task. It should answer the "what" and "why" of the issue, giving enough context for a developer to understand the goals without needing to seek additional information.

2.  **`### Work Done`**
    This section is a chronological log of the work performed to resolve the issue. It should be a clear and detailed account of the steps taken, including:
    -   Code changes (e.g., "Refactored the `Foo` class into a `Bar` service").
    -   Dependencies added or removed.
    -   Configuration changes.
    -   Bugs fixed, with details on the root cause and the solution.
    -   Verification steps (e.g., "Ran the test suite and confirmed all tests pass").

3.  **`### Status`**
    This section provides a final summary of the outcome. For a completed task, it should confirm that the issue is resolved and the goals have been met.

## Principal Developer Best Practices

To ensure high-quality contributions, please follow these best practices when working on issues.

### 1. Understand the "Definition of Done"

Before writing any code, make sure you have a clear understanding of what a successful outcome looks like. The "Definition of Done" for most tasks includes:
-   The primary requirements of the issue are met.
-   The code is well-documented, clean, and follows project conventions.
-   Relevant tests have been added or updated.
-   All existing tests pass.
-   The "Work Done" section of the issue is updated with a clear summary of your changes.

### 2. Plan Your Approach

For non-trivial tasks, take a moment to plan your implementation. Think about:
-   Which files will you need to modify?
-   Are there any existing components you can reuse?
-   What is the best way to structure your code for maintainability and clarity?

### 3. Work in Small, Atomic Commits

Avoid creating a single, massive commit for a large task. Instead, break your work into small, logical, and "atomic" commits. Each commit should represent a single, complete thought or change. This makes your work easier to review and understand.

### 4. Verify Your Work

Never assume your changes work as expected. Always verify them by:
-   **Running tests:** The project's test suite is your first line of defense against regressions.
-   **Manual testing:** For CLI tools or other user-facing features, run the code manually to ensure it behaves as expected.
-   **Reading your own code:** A final read-through can often catch typos or logical errors.

### 5. Document Clearly

Update the "Work Done" section of the issue file as you complete the task. This is not just for others; it's a valuable log for your future self. Be specific and concise. Instead of "fixed a bug," write "Fixed a `NameError` in `src/crfgen/cdash.py` caused by a typo in an enum." This level of detail is invaluable for future maintenance and debugging.

By following these guidelines, you'll contribute effectively to the project and help us maintain a high-quality, stable, and easy-to-understand codebase.
