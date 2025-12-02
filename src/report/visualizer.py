import plotly.graph_objects as go
import pandas as pd


def plot_student_activity(student_data: dict) -> go.Figure:
    """Строит график активности студента."""
    act = student_data["activity"]
    labels = list(act.keys())
    values = list(act.values())

    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=values,
        marker_color=['#3498db', '#2ecc71', '#e74c3c', '#f39c12'][:len(labels)]
    )])
    fig.update_layout(
        title="Активность за период",
        xaxis_title="Тип события",
        yaxis_title="Количество",
        template="plotly_white"
    )
    return fig
