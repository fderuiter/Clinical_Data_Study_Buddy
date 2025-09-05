#!/usr/bin/env python
"""
This script updates the internal 'parent' and 'dependencies' links within the
issue markdown files to use the new hierarchical naming scheme.

It contains a mapping of old filenames to new filenames and iterates through
all markdown files in a specified directory, replacing any occurrences of the
old names in the relevant fields.
"""
import os
import re
import argparse

# The mapping of old filenames to their new hierarchical names.
# This is the source of truth for the update process.
FILENAME_MAP = {
    # Children of 00-epic
    "01-task-repository-restructuring.md": "00.01-task-repository-restructuring.md",
    "02-task-cli-refactoring.md": "00.02-task-cli-refactoring.md",
    "03-chore-enhance-ci-cd-pipeline.md": "00.03-chore-enhance-ci-cd-pipeline.md",
    "05-chore-refactor-remaining-scripts.md": "00.04-chore-refactor-remaining-scripts.md",
    # Children of 04-epic
    "15-task-improve-module-documentation.md": "04.01-task-improve-module-documentation.md",
    # Children of 06-epic
    "07-epic-transition-to-cdisc-api.md": "06.01-epic-transition-to-cdisc-api.md",
    "08-epic-enhance-crf-generation.md": "06.02-epic-enhance-crf-generation.md",
    "09-epic-expand-synthetic-data-generation.md": "06.03-epic-expand-synthetic-data-generation.md",
    "14-chore-add-comprehensive-tests.md": "06.04-chore-add-comprehensive-tests.md",
    "16-theme-feature-expansion-clinical-data-generation.md": "06.05-theme-feature-expansion-clinical-data-generation.md",
    # Grandchildren of 06-epic
    "10-task-replace-web-crawler.md": "06.01.01-task-replace-web-crawler.md",
    "11-task-automate-standard-download.md": "06.01.02-task-automate-standard-download.md",
    "12-task-refactor-crf-logic-for-api.md": "06.02.01-task-refactor-crf-logic-for-api.md",
    "13-task-enhance-synthetic-data-generator.md": "06.03.01-task-enhance-synthetic-data-generator.md",
    "17-initiative-dataset-generation-ui.md": "06.05.01-initiative-dataset-generation-ui.md",
    "18-initiative-document-template-generators.md": "06.05.02-initiative-document-template-generators.md",
    "19-initiative-utility-and-supporting-features.md": "06.05.03-initiative-utility-and-supporting-features.md",
    # Great-grandchildren of 06-epic
    "20-epic-core-dataset-generator.md": "06.05.01.01-epic-core-dataset-generator.md",
    "21-epic-ui-for-dataset-generation.md": "06.05.01.02-epic-ui-for-dataset-generation.md",
    "22-epic-generate-edc-raw-dataset-package.md": "06.05.02.01-epic-generate-edc-raw-dataset-package.md",
    "23-epic-generate-sas-reference-code.md": "06.05.02.02-epic-generate-sas-reference-code.md",
    "24-epic-generate-blank-crfs.md": "06.05.02.03-epic-generate-blank-crfs.md",
    "25-epic-generate-tfl-shells.md": "06.05.02.04-epic-generate-tfl-shells.md",
    "26-epic-generate-specification-templates.md": "06.05.02.05-epic-generate-specification-templates.md",
    "27-epic-generate-study-protocols.md": "06.05.02.06-epic-generate-study-protocols.md",
    "28-spike-investigate-adrg-sdrg-generation.md": "06.05.02.07-spike-investigate-adrg-sdrg-generation.md",
    "29-epic-rest-api-for-programmatic-access.md": "06.05.03.01-epic-rest-api-for-programmatic-access.md",
    "30-epic-integrate-with-cdisc-rules-engine.md": "06.05.03.02-epic-integrate-with-cdisc-rules-engine.md",
}


def update_links_in_file(filepath, filename_map):
    """
    Reads a file and updates the parent and dependencies fields based on the map.
    """
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return

    original_content = content

    # Iterate through the map and replace old names with new names
    for old_name, new_name in filename_map.items():
        # Regex to find 'parent: "old_name"' or 'parent: old_name'
        content = re.sub(
            rf'(parent:\s*["\']?){re.escape(old_name)}["\']?',
            rf"\g<1>{new_name}",
            content,
        )
        # Regex to find '- "old_name"' or '- old_name' in a list
        content = re.sub(
            rf'(-\s*["\']?){re.escape(old_name)}["\']?',
            rf"\g<1>{new_name}",
            content,
        )

    # Write the content back only if it has changed
    if content != original_content:
        try:
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Updated links in: {filepath}")
        except IOError as e:
            print(f"Error writing to file {filepath}: {e}")


def main():
    """
    Main function to parse arguments and walk through the directory.
    """
    parser = argparse.ArgumentParser(
        description="Update parent and dependency links in issue markdown files."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default="issues",
        help="The directory containing the issue files (default: 'issues').",
    )
    args = parser.parse_args()

    issues_dir = args.directory
    if not os.path.isdir(issues_dir):
        print(f"Error: Directory not found at '{issues_dir}'")
        return

    print(f"Scanning for markdown files in '{issues_dir}'...")
    for root, _, files in os.walk(issues_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                update_links_in_file(filepath, FILENAME_MAP)

    print("Link update process complete.")


if __name__ == "__main__":
    main()
