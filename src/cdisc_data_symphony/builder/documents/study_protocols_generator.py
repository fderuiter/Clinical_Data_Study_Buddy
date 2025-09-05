import os
from cdisc_data_symphony.builder.protogen.protocol import StudyProtocol, generate_protocol_markdown

class StudyProtocolsGenerator:
    def __init__(self, therapeutic_area, treatment_arms, duration_weeks, phase, output_dir):
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
