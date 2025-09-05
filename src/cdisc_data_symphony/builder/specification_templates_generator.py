"""
This module contains the SpecificationTemplatesGenerator class, which is responsible for
generating Excel-based specification templates for CDISC datasets.
"""
import os
from openpyxl import Workbook
from cdisc_library_client.harvest import harvest
from cdisc_data_symphony.builder.crfgen.utils import get_api_key


class SpecificationTemplatesGenerator:
    """
    A class for generating Excel-based specification templates for CDISC datasets.

    This class fetches metadata from the CDISC Library for a given product and version,
    and then generates an Excel spreadsheet that outlines the specification for the
    selected domains.
    """
    def __init__(self, product, version, domains, output_dir):
        """
        Initializes the SpecificationTemplatesGenerator.

        Args:
            product (str): The CDISC product (e.g., "sdtmig", "adamig").
            version (str): The version of the product (e.g., "3-3").
            domains (list): A list of domains to include in the specification.
            output_dir (str): The directory where the generated Excel file will be saved.
        """
        self.product = product
        self.version = version
        self.domains = domains
        self.output_dir = output_dir

    def generate(self):
        """
        Generates the Excel-based specification template.

        This method fetches the necessary data from the CDISC Library and creates
        an Excel workbook with a separate sheet for each specified domain,
        detailing the variables and their properties.
        """
        print(f"Generating Excel specification for {self.product} {self.version}...")
        api_key = get_api_key()
        forms = harvest(api_key, self.product, self.version)
        wb = Workbook()
        wb.remove(wb.active)  # Remove default sheet

        for domain in self.domains:
            print(f"Generating {domain} sheet...")
            domain_form = next((f for f in forms if f.domain == domain), None)
            if not domain_form:
                print(f"Warning: Domain {domain} not found in CDISC Library. Skipping.")
                continue

            ws = wb.create_sheet(title=domain)
            ws.append(["Variable", "Label", "Type", "Length", "Codelist"])
            for item in domain_form.items:
                ws.append(
                    [
                        item.name,
                        item.label,
                        item.data_type,
                        item.length,
                        item.codelist.name if item.codelist else "",
                    ]
                )

        output_file = os.path.join(self.output_dir, f"{self.product}_{self.version}_spec.xlsx")
        wb.save(output_file)
        print(f"Excel specification generated successfully: {output_file}")
