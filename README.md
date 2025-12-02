# 📊 StudyFlow — AI-Powered Learning Engagement Analyzer

> *Understand how students learn — and help them learn better.*

![Tests](https://github.com/KostarevEgor1/studyflow/workflows/CI/badge.svg)
![Report Status](https://github.com/KostarevEgor1/studyflow/workflows/Report%20Generator/badge.svg)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://kostarevegor1.github.io/studyflow/)

## 🔍 Что делает?
StudyFlow анализирует логи учебных платформ (Moodle, Canvas и др.) и:
- 📈 Находит корреляцию между активностью и успеваемостью
- 🧠 Строит прогноз итоговой оценки по текущему поведению
- 💡 Выдаёт персонализированные рекомендации студентам
- 📊 Формирует интерактивный отчёт с визуализацией

> Пример вывода:  
> *«Для вас участие в форуме повышает итоговую оценку на 18%, а повторные попытки тестов — снижают. Рекомендуем: участвуйте в обсуждениях ≥2 раза в неделю»*

---

## 🚀 Установка

```bash
git clone https://github.com/KostarevEgor1/studyflow.git
cd studyflow
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
