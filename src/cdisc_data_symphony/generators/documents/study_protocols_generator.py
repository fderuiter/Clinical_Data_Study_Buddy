"""
This module contains the StudyProtocolsGenerator class, which is responsible for
generating study protocol documents in Markdown format.
"""
import os
from cdisc_data_symphony.generators.protogen.protocol import StudyProtocol, generate_protocol_markdown


class StudyProtocolsGenerator:
    """
    A class for generating study protocol documents.

    This class takes study parameters, creates a StudyProtocol object, and then
    uses the `generate_protocol_markdown` function to generate the final
    document.
    """
    def __init__(self, therapeutic_area, treatment_arms, duration_weeks, phase, output_dir):
        """
        Initializes the StudyProtocolsGenerator.

        Args:
            therapeutic_area (str): The therapeutic area of the study.
            treatment_arms (list): A list of treatment arms in the study.
            duration_weeks (int): The duration of the study in weeks.
            phase (int): The phase of the clinical trial.
            output_dir (str): The directory where the protocol document will be saved.
        """
        self.therapeutic_area = therapeutic_area
        self.treatment_arms = treatment_arms
        self.duration_weeks = duration_weeks
        self.phase = phase
        self.output_dir = output_dir

    def generate(self):
        """
        Generates a study protocol.
        """
        print(f"Generating study protocol in {self.output_dir}...")
        os.makedirs(self.output_dir, exist_ok=True)

        protocol = StudyProtocol(
            therapeutic_area=self.therapeutic_area,
            treatment_arms=self.treatment_arms,
            duration_weeks=self.duration_weeks,
            phase=self.phase,
        )

        output_path = generate_protocol_markdown(protocol, self.output_dir)

        print(f"Protocol document generated at {output_path}")
