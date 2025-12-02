#!/usr/bin/env python3
"""
Основной CLI-интерфейс StudyFlow.
Запуск: python src/main.py --logs data/logs.csv --grades data/grades.csv [--student ID]
"""

import argparse
import os

from src.core import parser, analyzer, predictor, recommender
from src.report import generator, visualizer


def main():
    parser_ = argparse.ArgumentParser(description="StudyFlow: Анализ эффективности обучения")
    parser_.add_argument("--logs", required=True, help="Путь к CSV с логами LMS")
    parser_.add_argument("--grades", required=True, help="Путь к CSV с оценками")
    parser_.add_argument("--student", type=int, help="ID студента для персонального отчёта")
    parser_.add_argument("--all", action="store_true", help="Сгенерировать отчёты для всех")
    parser_.add_argument(
        "--output",
        default="reports",
        help="Папка или путь к файлу для сохранения отчёта"
    )

    args = parser_.parse_args()

    # Создаём папку reports, если не существует
    os.makedirs("reports", exist_ok=True)

    # Загрузка данных
    logs_df = parser.load_logs(args.logs)
    grades_df = parser.load_grades(args.grades)

    if args.student:
        # Персональный отчёт
        student_data = analyzer.get_student_data(logs_df, grades_df, args.student)
        if student_data is None:
            print(f"❌ Студент ID={args.student} не найден")
            return

        pred_grade = predictor.predict_grade(student_data)
        recommendations = recommender.generate_recommendations(student_data)
        fig = visualizer.plot_student_activity(student_data)

        report_html = generator.render_student_report(
            student_id=args.student,
            data=student_data,
            predicted_grade=round(pred_grade, 1),
            recommendations=recommendations,
            plot_html=fig.to_html(full_html=False, include_plotlyjs='cdn')
        )

        out_path = args.output if args.output.endswith(".html") else f"{args.output}/report_student_{args.student}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report_html)
        print(f"✅ Отчёт сохранён: {out_path}")

    elif args.all:
        # Отчёт для всех
        all_students = grades_df["student_id"].unique()
        for sid in all_students:
            student_data = analyzer.get_student_data(logs_df, grades_df, sid)
            if student_data is None:
                continue
            pred_grade = predictor.predict_grade(student_data)
            recommendations = recommender.generate_recommendations(student_data)
            fig = visualizer.plot_student_activity(student_data)

            report_html = generator.render_student_report(
                student_id=sid,
                data=student_data,
                predicted_grade=round(pred_grade, 1),
                recommendations=recommendations,
                plot_html=fig.to_html(full_html=False, include_plotlyjs='cdn')
            )
            with open(f"reports/report_student_{sid}.html", "w", encoding="utf-8") as f:
                f.write(report_html)

        print(f"✅ Сгенерировано {len(all_students)} отчётов в папке 'reports/'")

    else:
        # Общий анализ
        correlation = analyzer.correlate_activities(logs_df, grades_df)
        print("🔍 Корреляция активности и итоговой оценки:")
        for act, corr in sorted(correlation.items(), key=lambda x: abs(x[1]), reverse=True):
            print(f"  {act}: {corr:+.3f}")


if __name__ == "__main__":
    main()
