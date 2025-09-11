"""
This module contains the ADRGGenerator class, which is responsible for
generating an Analysis Data Reviewer's Guide (ADRG) document.
"""
from clinical_data_study_buddy.generators.documents.base_document_generator import BaseDocumentGenerator


class ADRGGenerator(BaseDocumentGenerator):
    """
    A class for generating an Analysis Data Reviewer's Guide (ADRG) document.

    This class inherits from the BaseDocumentGenerator and provides the specific
    implementation for creating the title and sections of an ADRG.
    """
    @property
    def document_type(self):
        """
        Returns the type of the document, which is "ADRG".

        Returns:
            str: The document type "ADRG".
        """
        return "ADRG"

    def _add_title(self, document):
        document.add_heading('Analysis Data Reviewer\'s Guide', level=0)

    def _add_sections(self, document):
        # Section 1: Introduction
        document.add_heading('1. Introduction', level=1)
        document.add_paragraph(f"This document describes the analysis datasets for {self.study_config.study_id}.")
        document.add_paragraph("This guide is intended to assist the reviewer in understanding the structure and content of the analysis datasets.")

        # Section 2: Protocol Description
        document.add_heading('2. Protocol Description', level=1)
        document.add_paragraph(f"Protocol: {self.study_config.protocol_id or 'N/A'}")
        document.add_paragraph(f"Protocol Title: {self.study_config.protocol_title or 'N/A'}")

        # Section 3: Analysis Datasets
        document.add_heading('3. Analysis Datasets', level=1)
        document.add_paragraph("The following analysis datasets are included in this submission:")
        document.add_paragraph("- ADSL (Subject-Level Analysis Dataset)")
        document.add_paragraph("- ADAE (Adverse Event Analysis Dataset)")

        # Section 4: Data Conformance
        document.add_heading('4. Data Conformance', level=1)
        document.add_paragraph("The analysis datasets were checked for conformance with the CDISC ADaM standard.")
        document.add_paragraph("Any conformance issues are documented in the data definition file (define.xml).")

        # Section 5: Program and Macro Catalog
        document.add_heading('5. Program and Macro Catalog', level=1)
        document.add_paragraph("This section provides a catalog of the programs and macros used to create the analysis datasets.")
        document.add_paragraph("- adsl.sas")
        document.add_paragraph("- adae.sas")

        # Section 6: Data Listings
        document.add_heading('6. Data Listings', level=1)
        document.add_paragraph("This section provides information about the data listings included in this submission.")

        # Section 7: Figures and Tables
        document.add_heading('7. Figures and Tables', level=1)
        document.add_paragraph("This section provides information about the figures and tables included in this submission.")
