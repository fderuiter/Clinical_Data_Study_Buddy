import json
from docx import Document
from abc import ABC, abstractmethod
from cdisc_data_symphony.core.models.config import StudyConfig

class BaseDocumentGenerator(ABC):
    def __init__(self, study_config_path):
        with open(study_config_path, 'r') as f:
            config_dict = json.load(f)
        self.study_config = StudyConfig(**config_dict)

    def generate(self, output_path):
        document = Document()
        self._add_title(document)
        self._add_sections(document)
        document.save(output_path)
        print(f"{self.document_type} document generated at: {output_path}")

    @property
    @abstractmethod
    def document_type(self):
        pass

    @abstractmethod
    def _add_title(self, document):
        pass

    @abstractmethod
    def _add_sections(self, document):
        pass
