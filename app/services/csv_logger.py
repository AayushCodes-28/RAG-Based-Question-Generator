import csv
import os
from datetime import datetime

CSV_FILE = "generated_questions.csv"

HEADER = ["timestamp", "question", "difficulty", "domains"]

def log_to_csv(question, difficulty, domains):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(HEADER)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            difficulty,
            ",".join(domains)
        ])
