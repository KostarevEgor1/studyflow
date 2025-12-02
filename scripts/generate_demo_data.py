import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Генерация 10 студентов
students = list(range(101, 111))
events = ["login", "view", "forum", "video", "quiz_attempt"]

logs = []
grades = []

start_date = datetime(2025, 3, 1)

for sid in students:
    n_events = np.random.randint(5, 15)
    for _ in range(n_events):
        ts = start_date + timedelta(
            days=np.random.randint(0, 10),
            hours=np.random.randint(8, 20),
            minutes=np.random.randint(0, 60)
        )
        event = np.random.choice(events, p=[0.1, 0.3, 0.2, 0.2, 0.2])
        logs.append([ts, sid, event, f"{event}_{np.random.randint(1, 100)}"])

    # Оценки
    forum_posts = len([e for e in logs if e[1] == sid and e[2] == "forum"])
    quiz_attempts = len([e for e in logs if e[1] == sid and e[2] == "quiz_attempt"])
    
    forum_score = min(100, 40 + forum_posts * 10)
    quiz_avg = max(40, 80 - quiz_attempts * 3)
    final = int(0.5 * quiz_avg + 0.3 * forum_score + forum_posts * 2 + np.random.randint(-5, 6))
    
    grades.append([sid, quiz_avg, forum_score, final])

pd.DataFrame(logs, columns=["timestamp", "student_id", "event_type", "object_id"]).to_csv("data/demo_logs.csv", index=False)
pd.DataFrame(grades, columns=["student_id", "quiz_avg", "forum_score", "final_grade"]).to_csv("data/demo_grades.csv", index=False)

print("✅ Демоданные сгенерированы: data/demo_*.csv")
