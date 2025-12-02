import pandas as pd


def load_logs(path: str) -> pd.DataFrame:
    """Загружает логи LMS из CSV."""
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def load_grades(path: str) -> pd.DataFrame:
    """Загружает оценки из CSV."""
    return pd.read_csv(path)
