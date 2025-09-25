import re

import toml


def test_readme_cli_command():
    """
    Tests that the CLI command in the README.md file is in sync with the one defined in pyproject.toml.
    """
    # Read the pyproject.toml file
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)

    # Get the CLI command from the [tool.poetry.scripts] section
    cli_command = list(pyproject_data["tool"]["poetry"]["scripts"].keys())[0]

    # Read the README.md file
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Find the command in the README.md file's Command-Line Interface (CLI) section
    cli_section = readme_content.split("### Command-Line Interface (CLI)")[1]
    match = re.search(r"poetry run (\w+)", cli_section)
    assert (
        match is not None
    ), "Could not find the CLI command in the README.md file's CLI section."
    readme_command = match.group(1)

    # Check if the command in the README.md file matches the one in pyproject.toml
    assert readme_command == cli_command, (
        f"The CLI command in README.md ('{readme_command}') does not match the one in pyproject.toml ('{cli_command}')."
        "Please update the README.md file to use the correct command."
    )
