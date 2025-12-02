from src.core import predictor


def test_predict_grade():
    data = {
        "id": 101,
        "activity": {"forum": 3, "quiz_attempt": 1},
        "grades": {"quiz_avg": 80, "forum_score": 90}
    }
    pred = predictor.predict_grade(data)
    assert 50 <= pred <= 100
