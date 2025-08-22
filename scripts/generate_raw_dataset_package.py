#!/usr/bin/env python
import argparse
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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


from src.cdisc_dataset_generator_client.client import CDISCDataSetGeneratorClient
from src.cdisc_library_client.client import AuthenticatedClient, Client
from src.cdisc_library_client.api.sdtm_implementation_guide_sdtmig import get_mdr_sdtmig_version_datasets_dataset_variables_var

def generate_define_xml(temp_dir, domains):
    print("Generating define.xml...")

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
        print("Warning: CDISC_API_KEY environment variable not set. Cannot fetch metadata.")
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
                    print(f"  - Could not find metadata for variable {var_name} in domain {domain}")
            except httpx.HTTPStatusError as e:
                print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e.response.status_code}")
            except Exception as e:
                print(f"  - Error fetching metadata for variable {var_name} in domain {domain}: {e}")


    # Write the file
    define_xml_path = temp_dir / "define.xml"
    root.write_xml(str(define_xml_path))
    print("define.xml generated.")

def package_datasets(temp_dir, output_dir):
    zip_filename = Path(output_dir) / "edc_raw_datasets.zip"
    print(f"Packaging datasets into {zip_filename}...")
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in temp_dir.glob("*"):
            zipf.write(file, file.name)
    print("Packaging complete.")

    # Clean up the temporary directory
    print("Cleaning up temporary files...")
    shutil.rmtree(temp_dir)
    print("Cleanup complete.")

def apply_study_story(study_story, temp_dir, num_subjects, domains, file_format):
    if study_story == "high_dropout":
        print("Applying 'high_dropout' study story...")
        dropout_rate = 0.3
        num_dropouts = int(num_subjects * dropout_rate)

        # Assuming DM is always present and contains the full subject list
        dm_file = next(temp_dir.glob("sdtm_dm*.csv"), None)
        if not dm_file:
            print("Warning: DM domain not found. Cannot apply high dropout story.")
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
                    print(f"  - Applied dropout to {domain} domain.")
        else:
            print(f"Warning: High dropout story not implemented for '{file_format}' format yet.")


def main():
    parser = argparse.ArgumentParser(description="Generate an EDC Raw Dataset Package.")
    parser.add_argument(
        "--num-subjects",
        type=int,
        default=50,
        help="Number of subjects (10-200).",
    )
    parser.add_argument(
        "--therapeutic-area",
        default="Oncology",
        help="Therapeutic area for the study.",
    )
    parser.add_argument(
        "--domains",
        nargs="+",
        required=True,
        help="List of domains to include (e.g., DM AE VS LB)."
    )
    parser.add_argument(
        "--study-story",
        choices=["none", "high_dropout"],
        default="none",
        help="Study story to simulate.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to save the generated package."
    )
    parser.add_argument(
        "--output-format",
        default="csv",
        choices=["csv", "json", "xpt"],
        help="Output format for datasets."
    )

    args = parser.parse_args()

    print("Generating EDC Raw Dataset Package...")
    print(f"  Number of Subjects: {args.num_subjects}")
    print(f"  Therapeutic Area: {args.therapeutic_area}")
    print(f"  Domains: {', '.join(args.domains)}")
    print(f"  Study Story: {args.study_story}")
    print(f"  Output Format: {args.output_format}")
    print(f"  Output Directory: {args.output_dir}")

    client = CDISCDataSetGeneratorClient()
    temp_dir = Path(args.output_dir) / "temp_datasets"
    os.makedirs(temp_dir, exist_ok=True)

    for domain in args.domains:
        print(f"Generating {domain} dataset...")
        try:
            result = client.generate_dataset(
                dataset_type="SDTM",
                domain=domain,
                num_subjects=args.num_subjects,
                therapeutic_area=args.therapeutic_area,
                format=args.output_format,
            )
            download_url = result["download_url"]
            filename = result["filename"]
            output_path = temp_dir / filename
            print(f"Downloading dataset to {output_path}...")
            client.download_file(download_url, str(output_path))
            print(f"{domain} dataset downloaded successfully.")
        except Exception as e:
            print(f"Error generating dataset for domain {domain}: {e}")

    if args.study_story != "none":
        apply_study_story(args.study_story, temp_dir, args.num_subjects, args.domains, args.output_format)

    generate_define_xml(temp_dir, args.domains)
    package_datasets(temp_dir, args.output_dir)


if __name__ == "__main__":
    main()
