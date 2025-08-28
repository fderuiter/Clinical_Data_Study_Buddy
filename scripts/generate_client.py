#!/usr/bin/env python3
"""
Generates the Python client for the CDISC Library API.
"""
import shutil
import subprocess
from pathlib import Path

# The directory where the final client should be
FINAL_CLIENT_DIR = Path("src/cdisc_library_client")

# The directory where openapi-python-client will generate the client
# This is based on the title in the OpenAPI spec.
GENERATED_CLIENT_DIR = Path("cdisc-library-api-client")

OPENAPI_SPEC = Path("openapi/cdisc-library.json")


def generate_client():
    """
    Removes the existing client and generates a new one from the OpenAPI spec.
    """
    # 1. Remove the old generated client directory if it exists
    if GENERATED_CLIENT_DIR.exists():
        print(f"Removing existing generated client at {GENERATED_CLIENT_DIR}...")
        shutil.rmtree(GENERATED_CLIENT_DIR)

    # 2. Generate the new client
    print("Generating new client...")
    command = [
        "poetry",
        "run",
        "openapi-python-client",
        "generate",
        "--path",
        str(OPENAPI_SPEC),
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error generating client:")
        print(result.stdout)
        print(result.stderr)
        exit(1)

    print(result.stdout)
    print("Client generated successfully.")

    # 3. Remove the old final client directory
    if FINAL_CLIENT_DIR.exists():
        print(f"Removing existing final client at {FINAL_CLIENT_DIR}...")
        shutil.rmtree(FINAL_CLIENT_DIR)

    # 4. Move the newly generated client to the final location
    # The client code is in a subdirectory of the generated directory
    generated_code_dir = GENERATED_CLIENT_DIR / "cdisc_library_api_client"
    print(f"Moving generated code from {generated_code_dir} to {FINAL_CLIENT_DIR}...")
    shutil.move(str(generated_code_dir), str(FINAL_CLIENT_DIR))

    # 5. Clean up the now-empty generated client directory
    print(f"Cleaning up {GENERATED_CLIENT_DIR}...")
    shutil.rmtree(GENERATED_CLIENT_DIR)

    print("Client generation and move complete.")


if __name__ == "__main__":
    generate_client()
