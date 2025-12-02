import pandas as pd
from src.core import parser


def test_load_logs():
    df = parser.load_logs("data/sample_logs.csv")
    assert isinstance(df, pd.DataFrame)
    assert "student_id" in df.columns
    assert len(df) > 0


def test_load_grades():
    df = parser.load_grades("data/sample_grades.csv")
    assert isinstance(df, pd.DataFrame)
    assert "final_grade" in df.columns
    assert len(df) == 2
