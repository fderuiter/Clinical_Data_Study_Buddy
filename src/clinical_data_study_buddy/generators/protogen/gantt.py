"""
This module provides a function for generating Gantt charts using matplotlib.
"""

import matplotlib.pyplot as plt
import pandas as pd


def generate_gantt_chart(tasks, output_path):
    """
    Generates a Gantt chart from a list of tasks and saves it as an image file.

    Args:
        tasks (list): A list of dictionaries, where each dictionary represents a task.
                      Each task dictionary should have 'name', 'start', and 'end' keys.
                      'start' and 'end' should be date strings in 'YYYY-MM-DD' format.
        output_path (str): The path to save the Gantt chart image file.
    """
    df = pd.DataFrame(tasks)
    df["start"] = pd.to_datetime(df["start"])
    df["end"] = pd.to_datetime(df["end"])
    df = df.sort_values(by="start").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(10, 5))

    for i, task in df.iterrows():
        ax.barh(
            y=task["name"],
            width=(task["end"] - task["start"]),
            left=task["start"],
            height=0.5,
        )

    ax.xaxis_date()
    fig.autofmt_xdate()

    plt.title("Study Timeline")
    plt.xlabel("Date")
    plt.ylabel("Task")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
