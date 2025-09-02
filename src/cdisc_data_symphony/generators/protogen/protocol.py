from pydantic import BaseModel
from typing import List
from jinja2 import Environment, FileSystemLoader
import os
from datetime import date, timedelta

from cdisc_data_symphony.generators.protogen.gantt import generate_gantt_chart

class StudyProtocol(BaseModel):
    therapeutic_area: str
    treatment_arms: List[str]
    duration_weeks: int
    phase: int

def generate_protocol_markdown(protocol: StudyProtocol, output_dir: str):
    """
    Generates a study protocol in Markdown format.
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
    env = Environment(loader=FileSystemLoader("src/cdisc_data_symphony/templates/protogen"))
    template = env.get_template("protocol.md.j2")
    markdown_content = template.render(protocol=protocol)

    # Save markdown file
    output_path = os.path.join(output_dir, "protocol.md")
    with open(output_path, "w") as f:
        f.write(markdown_content)

    return output_path
