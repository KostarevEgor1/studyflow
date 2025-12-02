def generate_recommendations(student_data: dict) -> list:
    """Генерирует персонализированные рекомендации."""
    act = student_data["activity"]
    grades = student_data["grades"]
    recs = []

    forum_count = act.get("forum", 0)
    quiz_avg = grades.get("quiz_avg", 0)
    forum_score = grades.get("forum_score", 0)

    if forum_count < 2 and forum_score > quiz_avg:
        recs.append(
            "💬 Участие в форуме повышает оценку. Пишите ≥2 поста в неделю."
        )

    if act.get("quiz_attempt", 0) > 3:
        recs.append(
            "🔁 Повторные попытки тестов снижают эффективность. Лучше подготовиться заранее."
        )

    if act.get("view", 0) == 0 and act.get("video", 0) > 0:
        recs.append(
            "📄 Лекции в текстовом формате помогают глубже понять материал — попробуйте их."
        )

    if not recs:
        recs.append("✅ Вы на правильном пути! Продолжайте в том же темпе.")

    return recs
