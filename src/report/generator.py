from jinja2 import Template
from datetime import datetime

_REPORT_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>StudyFlow — Отчёт для студента {{ student_id }}</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            margin: 40px;
        }
        .header { text-align: center; color: #2c3e50; }
        .metric {
            display: inline-block;
            margin: 10px;
            padding: 15px;
            background: #ecf0f1;
            border-radius: 8px;
        }
        .rec {
            background: #e8f4f8;
            padding: 12px;
            margin: 10px 0;
            border-left:
            4px solid #3498db;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 StudyFlow — Персональный отчёт</h1>
        <p><strong>Студент ID:</strong> {{ student_id }}</p>
    </div>

    <div class="metric">
        <h3>📊 Текущие оценки</h3>
        <ul>
        {% for k, v in data.grades.items() if k != 'student_id' %}
            <li><strong>{{ k }}:</strong> {{ v }}</li>
        {% endfor %}
        </ul>
    </div>

    <div class="metric">
        <h3>📈 Прогноз итоговой оценки</h3>
        <p><strong>{{ predicted_grade }} / 100</strong></p>
    </div>

    <div class="metric">
        <h3>🎯 Рекомендации</h3>
        {% for rec in recommendations %}
            <div class="rec">• {{ rec }}</div>
        {% endfor %}
    </div>

    <div class="metric">
        <h3>🎨 Активность</h3>
        <div id="plot">{{ plot_html|safe }}</div>
    </div>

    <hr>
    <footer>
        Сгенерировано автоматически с помощью
        <a href="https://gitverse.ru/KostarevEgor1/studyflow">StudyFlow</a>
        • {{ now }}
    </footer>
</body>
</html>
"""


def render_student_report(
    student_id: int, data: dict, predicted_grade: float,
    recommendations: list,
    plot_html: str
) -> str:
    template = Template(_REPORT_TEMPLATE)
    return template.render(
        student_id=student_id,
        data=data,
        predicted_grade=predicted_grade,
        recommendations=recommendations,
        plot_html=plot_html,
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
    )
