import numpy as np


def predict_grade(student_data: dict) -> float:
    """
    Простая модель прогноза: линейная комбинация активностей и текущих оценок.
    В реальном проекте — заменить на sklearn модель.
    """
    act = student_data["activity"]
    grades = student_data["grades"]

    # Простая эвристика: веса подобраны на основе корреляций
    score = 0.0
    score += grades.get("quiz_avg", 0) * 0.5
    score += grades.get("forum_score", 0) * 0.3
    score += act.get("forum", 0) * 2.5    # каждый пост в форуме +2.5 балла
    score += act.get("view", 0) * 0.8    # просмотр лекции +0.8
    score += act.get("video", 0) * 1.2   # видео +1.2
    score += act.get("quiz_attempt", 0) * (-1.0)  # повторные попытки — штраф

    # Ограничиваем диапазон [0, 100]
    return np.clip(score, 0, 100)
