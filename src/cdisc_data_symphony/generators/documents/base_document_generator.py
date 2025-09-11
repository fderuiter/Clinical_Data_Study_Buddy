"""
This module contains the BaseDocumentGenerator class, which serves as an
abstract base class for all document generators in the system.
"""
import json
from docx import Document
from abc import ABC, abstractmethod
from cdisc_data_symphony.core.models.config import StudyConfig


class BaseDocumentGenerator(ABC):
    """
    An abstract base class for document generators.

    This class provides a common framework for generating documents, including
    loading study configuration, creating a document, adding a title and sections,
    and saving the final document. Subclasses must implement the abstract methods
    to provide the specific content for each document type.

    Args:
        study_config_path (str): The path to the study configuration JSON file.
    """

    def __init__(self, study_config_path):
        """
        Initializes the BaseDocumentGenerator.

        Args:
            study_config_path (str): The path to the study configuration JSON file.
        """
        with open(study_config_path, 'r') as f:
            config_dict = json.load(f)
        self.study_config = StudyConfig(**config_dict)

    def generate(self, output_path):
        """
        Generates and saves the document.

        This method orchestrates the document generation process by creating a
        new document, adding the title and sections, and then saving it to the
        specified output path.

        Args:
            output_path (str): The path where the generated document will be saved.
        """
        document = Document()
        self._add_title(document)
        self._add_sections(document)
        document.save(output_path)
        print(f"{self.document_type} document generated at: {output_path}")

    @property
    @abstractmethod
    def document_type(self):
        """
        An abstract property that should return the type of the document.

        Returns:
            str: The document type (e.g., "SDRG", "ADRG").
        """
        pass

    @abstractmethod
    def _add_title(self, document):
        """
        An abstract method to add the title to the document.

        Args:
            document (Document): The python-docx Document object.
        """
        pass

    @abstractmethod
    def _add_sections(self, document):
        """
        An abstract method to add the main sections to the document.

        Args:
            document (Document): The python-docx Document object.
        """
        pass
