import pandas as pd


def correlate_activities(logs_df: pd.DataFrame, grades_df: pd.DataFrame) -> dict:
    """Вычисляет корреляцию между типами активности и итоговой оценкой."""
    # Считаем количество событий по каждому студенту и типу
    activity_counts = (
        logs_df.groupby(["student_id", "event_type"])
        .size()
        .unstack(fill_value=0)
    )
    merged = activity_counts.merge(grades_df, on="student_id")

    correlations = {}
    for activity in activity_counts.columns:
        if "final_grade" in merged.columns:
            corr = merged[activity].corr(merged["final_grade"])
            correlations[activity] = round(corr, 3)
    return correlations


def get_student_data(logs_df: pd.DataFrame, 
                     grades_df: pd.DataFrame, 
                     student_id: int) -> dict:
    """Возвращает данные студента: активность + оценки."""
    student_logs = logs_df[logs_df["student_id"] == student_id]
    student_grade_row = grades_df[grades_df["student_id"] == student_id]

    if student_grade_row.empty:
        return None

    grade_data = student_grade_row.iloc[0].to_dict()
    activity_summary = student_logs["event_type"].value_counts().to_dict()

    return {
        "id": student_id,
        "activity": activity_summary,
        "grades": grade_data
    }
