"""
This module provides classes and functions for generating study protocol
documents in Markdown format. It includes a Pydantic model for the study
protocol and a function to render the protocol using a Jinja2 template.
"""
from pydantic import BaseModel
from typing import List
from jinja2 import Environment, FileSystemLoader
import os
from datetime import date, timedelta

from clinical_data_study_buddy.generators.protogen.gantt import generate_gantt_chart


class StudyProtocol(BaseModel):
    """
    A Pydantic model representing the key parameters of a study protocol.

    Attributes:
        therapeutic_area (str): The therapeutic area of the study.
        treatment_arms (List[str]): A list of treatment arms in the study.
        duration_weeks (int): The duration of the study in weeks.
        phase (int): The phase of the clinical trial.
    """
    therapeutic_area: str
    treatment_arms: List[str]
    duration_weeks: int
    phase: int


def generate_protocol_markdown(protocol: StudyProtocol, output_dir: str):
    """
    Generates a study protocol in Markdown format, including a Gantt chart.

    This function takes a StudyProtocol object, generates a Gantt chart for
    the study timeline, and then renders a Markdown document from a Jinja2
    template, embedding the Gantt chart.

    Args:
        protocol (StudyProtocol): The StudyProtocol object containing the
                                  protocol details.
        output_dir (str): The directory where the generated Markdown file
                          and Gantt chart will be saved.

    Returns:
        str: The path to the generated Markdown file.
    """
    # Create Gantt chart
    gantt_chart_path = os.path.join(output_dir, "gantt_chart.png")
    # Create some sample tasks for the Gantt chart
    start_date = date.today()
    tasks = [
        {'name': 'Startup', 'start': start_date.isoformat(), 'end': (start_date + timedelta(weeks=4)).isoformat()},
        {'name': 'Treatment', 'start': (start_date + timedelta(weeks=4)).isoformat(), 'end': (start_date + timedelta(weeks=protocol.duration_weeks)).isoformat()},
        {'name': 'Follow-up', 'start': (start_date + timedelta(weeks=protocol.duration_weeks)).isoformat(), 'end': (start_date + timedelta(weeks=protocol.duration_weeks + 4)).isoformat()},
    ]
    generate_gantt_chart(tasks, gantt_chart_path)

    # Render markdown template
    env = Environment(loader=FileSystemLoader("templates/protogen"))
    template = env.get_template("protocol.md.j2")
    markdown_content = template.render(protocol=protocol)

    # Save markdown file
    output_path = os.path.join(output_dir, "protocol.md")
    with open(output_path, "w") as f:
        f.write(markdown_content)

    return output_path
