"""
This module provides helper functions for dataset generation.

The functions in this module are used to:
- Generate a define.xml file from a set of domains.
- Package generated datasets into a zip archive.
- Apply a "study story" to the datasets to simulate real-world scenarios.
"""
import os
import zipfile
from pathlib import Path
import pandas as pd
import random
import shutil
import httpx
from odmlib import odm_parser as P
from odmlib import odm_loader as L
from odmlib.define_2_1 import model as DEF
from odmlib.odm_1_3_2 import model as ODM
from rich.console import Console
from cdisc_library_client.client import AuthenticatedClient

console = Console()


def generate_define_xml(temp_dir, domains):
    """
    Generates a define.xml file for the given domains.

    This function creates a define.xml file by fetching metadata from the CDISC Library
    for the specified domains and their variables. The generated file is saved in the
    temporary directory.

    Args:
        temp_dir (pathlib.Path): The temporary directory containing the dataset files.
        domains (list): A list of domain names to include in the define.xml file.
    """
    console.print("Generating define.xml...")

    # Create the basic ODM structure
    root = ODM.ODM(
        FileOID="cdisc.com/Foundational/CDISC_ODM_2_0_0/define-2-1/2025-08-22/EDC_Raw_Dataset",
        CreationDateTime="2025-08-22T14:00:00",
        AsOfDateTime="2025-08-22T14:00:00",
        FileType="Snapshot",
        Originator="CDISC Dataset Generator",
        SourceSystem="CDISC Dataset Generator",
        SourceSystemVersion="0.1.0"
    )
    study = ODM.Study(OID="CDISC_STUDY.CDISC.TA.1")
    study.GlobalVariables = ODM.GlobalVariables()
    study.GlobalVariables.StudyName = ODM.StudyName(_content="CDISC TA Study")
    study.GlobalVariables.StudyDescription = ODM.StudyDescription(_content="A study in the TA therapeutic area")
    study.GlobalVariables.ProtocolName = ODM.ProtocolName(_content="CDISC-TA-1")
    root.Study.append(study)

    meta_data_version = DEF.MetaDataVersion(
        OID="MDV.CDISC_STUDY.CDISC.TA.1.SDTM.1.0",
        Name="CDISC TA Study SDTM 1.0",
        Description="Metadata for the CDISC TA Study",
        DefineVersion="2.1.0"
    )
    study.MetaDataVersion.append(meta_data_version)

    # Instantiate the CDISC Library client
    api_key = os.environ.get("CDISC_API_KEY")
    if not api_key:
        console.print("Warning: CDISC_API_KEY environment variable not set. Cannot fetch metadata.", style="yellow")
        # Create an empty define.xml
        define_xml_path = temp_dir / "define.xml"
        with open(define_xml_path, "w") as f:
            f.write("<ODM></ODM>")
        return

    client = AuthenticatedClient(
        base_url="https://library.cdisc.org/api",
        token=api_key,
        headers={"Accept": "application/json"},
        auth_header_name="api-key",
        prefix="",
        timeout=30.0,
    )

    sdtmig_version = "3-3" # Using a recent version as a default

    for domain in domains:
        domain_file = next(temp_dir.glob(f"sdtm_{domain.lower()}*.csv"), None)
        if not domain_file:
            continue

        # Create ItemGroupDef for the domain
        item_group_class = DEF.Class(Name="SPECIAL PURPOSE")
        item_group = DEF.ItemGroupDef(
            OID=f"IG.{domain.upper()}",
            Name=domain.upper(),
            Repeating="Yes",
            IsReferenceData="No",
            SASDatasetName=domain.upper(),
            Purpose="Tabulation",
            Structure="One record per subject",
            Class=item_group_class
        )
        meta_data_version.ItemGroupDef.append(item_group)

        # Get variable names from the CSV header
        df = pd.read_csv(domain_file)
        variables = list(df.columns)

        for var_name in variables:
            # Get variable metadata from CDISC Library using direct API call
            try:
                url = f"https://library.cdisc.org/products/sdtmig/{sdtmig_version}/datasets/{domain.upper()}/variables/{var_name}"
                headers = {"api-key": api_key, "Accept": "application/json"}
                response = httpx.get(url, headers=headers, timeout=60.0, follow_redirects=True)
                response.raise_for_status()
                variable_metadata = response.json()

                if variable_metadata:
                    item_def = DEF.ItemDef(
                        OID=f"IT.{domain.upper()}.{var_name}",
                        Name=var_name,
                        DataType=variable_metadata.get("datatype"),
                        Length=variable_metadata.get("length"),
                        SASFieldName=var_name
                    )
                    item_def.Description = DEF.Description()
                    item_def.Description.TranslatedText.append(
                        ODM.TranslatedText(_content=variable_metadata.get("label"), lang="en")
                    )
                    item_group.ItemRef.append(DEF.ItemRef(ItemOID=item_def.OID, OrderNumber=variables.index(var_name) + 1, Mandatory="No"))
                    meta_data_version.ItemDef.append(item_def)
                else:
                    console.print(f"  - Could not find metadata for variable {var_name} in domain {domain}", style="yellow")
            except httpx.HTTPStatusError as e:
                console.print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e.response.status_code}", style="yellow")
            except Exception as e:
                console.print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e}", style="yellow")


    # Write the file
    define_xml_path = temp_dir / "define.xml"
    root.write_xml(str(define_xml_path))
    console.print("define.xml generated.")


def package_datasets(temp_dir, output_dir):
    """
    Packages the generated datasets into a zip file.

    This function takes all the files in the temporary directory, packages them into a
    zip archive named "edc_raw_datasets.zip", and saves it in the output directory.
    After packaging, it cleans up the temporary directory.

    Args:
        temp_dir (pathlib.Path): The temporary directory containing the dataset files.
        output_dir (pathlib.Path): The directory where the zip file will be saved.
    """
    zip_filename = Path(output_dir) / "edc_raw_datasets.zip"
    console.print(f"Packaging datasets into {zip_filename}...")
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in temp_dir.glob("*"):
            zipf.write(file, file.name)
    console.print("Packaging complete.")

    # Clean up the temporary directory
    console.print("Cleaning up temporary files...")
    shutil.rmtree(temp_dir)
    console.print("Cleanup complete.")


def apply_study_story(study_story, temp_dir, num_subjects, domains, file_format):
    """
    Applies a study story to the generated datasets.

    This function modifies the datasets to simulate a real-world scenario, such as
    a high dropout rate.

    Args:
        study_story (str): The name of the study story to apply (e.g., "high_dropout").
        temp_dir (pathlib.Path): The temporary directory containing the dataset files.
        num_subjects (int): The total number of subjects in the study.
        domains (list): A list of domain names.
        file_format (str): The file format of the datasets (e.g., "csv").
    """
    if study_story == "high_dropout":
        console.print("Applying 'high_dropout' study story...")
        dropout_rate = 0.3
        num_dropouts = int(num_subjects * dropout_rate)

        # Assuming DM is always present and contains the full subject list
        dm_file = next(temp_dir.glob("sdtm_dm*.csv"), None)
        if not dm_file:
            console.print("Warning: DM domain not found. Cannot apply high dropout story.", style="yellow")
            return

        if file_format == 'csv':
            dm_df = pd.read_csv(dm_file)
            all_subject_ids = dm_df["USUBJID"].unique()
            dropout_subject_ids = random.sample(list(all_subject_ids), num_dropouts)

            for domain in domains:
                if domain.upper() == "DM":
                    continue  # Don't remove subjects from DM

                domain_file = next(temp_dir.glob(f"sdtm_{domain.lower()}*.csv"), None)
                if domain_file:
                    df = pd.read_csv(domain_file)
                    df = df[~df["USUBJID"].isin(dropout_subject_ids)]
                    df.to_csv(domain_file, index=False)
                    console.print(f"  - Applied dropout to {domain} domain.")
        else:
            console.print(f"Warning: High dropout story not implemented for '{file_format}' format yet.", style="yellow")
