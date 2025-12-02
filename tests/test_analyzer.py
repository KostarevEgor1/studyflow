import pandas as pd
from src.core import analyzer


def test_correlate_activities():
    logs = pd.DataFrame({
        "student_id": [101, 101, 102, 102],
        "event_type": ["forum", "quiz", "forum", "video"]
    })
    grades = pd.DataFrame({
        "student_id": [101, 102],
        "final_grade": [85, 55]
    })
    result = analyzer.correlate_activities(logs, grades)
    assert "forum" in result
    assert isinstance(result["forum"], float)
