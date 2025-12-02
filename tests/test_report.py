from src.report import generator


def test_render_student_report():
    html = generator.render_student_report(
        student_id=101,
        data={"activity": {"forum": 2}, "grades": {"final_grade": 85}},
        predicted_grade=87.3,
        recommendations=["Пишите в форум!"],
        plot_html="<div>Mock Plot</div>"
    )
    assert "Студент ID:</strong> 101" in html
    assert "87.3" in html
    assert "Пишите в форум!" in html
