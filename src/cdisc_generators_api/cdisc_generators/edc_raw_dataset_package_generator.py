import os
import pathlib
from typing import List
import pandas as pd
from cdisc_library_client.harvest import harvest
from cdisc_generators_api.cdisc_generators.crfgen.utils import get_api_key
from cdisc_generators_api.cdisc_generators.data_generator import DataGenerator
from cdisc_generators_api.cdisc_generators.dataset_helpers import generate_define_xml, package_datasets, apply_study_story


class EDCRawDatasetPackageGenerator:
    def __init__(
        self,
        num_subjects: int,
        therapeutic_area: str,
        domains: List[str],
        study_story: str,
        output_dir: pathlib.Path,
        output_format: str,
    ):
        self.num_subjects = num_subjects
        self.therapeutic_area = therapeutic_area
        self.domains = domains
        self.study_story = study_story
        self.output_dir = output_dir
        self.output_format = output_format

    def generate(self):
        """
        Generates and packages a raw EDC dataset.
        """
        print("Generating EDC Raw Dataset Package...")
        print(f"  Number of Subjects: {self.num_subjects}")
        print(f"  Therapeutic Area: {self.therapeutic_area}")
        print(f"  Domains: {', '.join(self.domains)}")
        print(f"  Study Story: {self.study_story}")
        print(f"  Output Format: {self.output_format}")
        print(f"  Output Directory: {self.output_dir}")

        api_key = get_api_key()
        forms = harvest(api_key)

        temp_dir = pathlib.Path(self.output_dir) / "temp_datasets"
        os.makedirs(temp_dir, exist_ok=True)

        for domain in self.domains:
            print(f"Generating {domain} dataset...")
            domain_form = next((f for f in forms if f.domain == domain), None)
            if not domain_form:
                print(f"Warning: Domain {domain} not found in CDISC Library. Skipping.")
                continue

            generator = DataGenerator(domain_form)
            dataset = generator.generate(self.num_subjects)

            output_file = temp_dir / f"{domain}.csv"
            df = pd.DataFrame(dataset)
            df.to_csv(output_file, index=False)
            print(f"{domain} dataset generated successfully.")

        if self.study_story != "none":
            apply_study_story(self.study_story, temp_dir, self.num_subjects, self.domains, self.output_format)

        generate_define_xml(temp_dir, self.domains)
        package_datasets(temp_dir, self.output_dir)
