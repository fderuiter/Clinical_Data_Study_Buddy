"""
This module contains the SDRGGenerator class, which is responsible for
generating a Study Data Reviewer's Guide (SDRG) document.
"""
from clinical_data_study_buddy.generators.documents.base_document_generator import BaseDocumentGenerator


class SDRGGenerator(BaseDocumentGenerator):
    """
    A class for generating a Study Data Reviewer's Guide (SDRG) document.

    This class inherits from the BaseDocumentGenerator and provides the specific
    implementation for creating the title and sections of an SDRG.
    """
    @property
    def document_type(self):
        """
        Returns the type of the document, which is "SDRG".

        Returns:
            str: The document type "SDRG".
        """
        return "SDRG"

    def _add_title(self, document):
        document.add_heading('Study Data Reviewer\'s Guide', level=0)

    def _add_sections(self, document):
        # Section 1: Introduction
        document.add_heading('1. Introduction', level=1)
        document.add_paragraph(f"This document describes the study data for {self.study_config.study_id}.")
        document.add_paragraph("This guide is intended to assist the reviewer in understanding the structure and content of the study data.")

        # Section 2: Protocol Description
        document.add_heading('2. Protocol Description', level=1)
        document.add_paragraph(f"Protocol: {self.study_config.protocol_id or 'N/A'}")
        document.add_paragraph(f"Protocol Title: {self.study_config.protocol_title or 'N/A'}")

        # Section 3: List of Included Documents
        document.add_heading('3. List of Included Documents', level=1)
        document.add_paragraph("This submission includes the following documents:")
        document.add_paragraph("- SDRG (this document)")
        document.add_paragraph("- define.xml")
        document.add_paragraph("- Annotated CRF")

        # Section 4: Data Collection and Processing
        document.add_heading('4. Data Collection and Processing', level=1)
        document.add_paragraph("This section describes how the data was collected and processed.")

        # Section 5: SDTM Datasets
        document.add_heading('5. SDTM Datasets', level=1)
        document.add_paragraph("The following SDTM datasets are included in this submission:")
        document.add_paragraph("- DM (Demographics)")
        document.add_paragraph("- AE (Adverse Events)")

        # Section 6: Data Conformance
        document.add_heading('6. Data Conformance', level=1)
        document.add_paragraph("The study data were checked for conformance with the CDISC SDTM standard.")
        document.add_paragraph("Any conformance issues are documented in the data definition file (define.xml).")

        # Section 7: Appendices
        document.add_heading('7. Appendices', level=1)
        document.add_paragraph("This section contains any appendices.")
