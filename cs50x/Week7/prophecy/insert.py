from cs50 import SQL
import csv

db = SQL("sqlite:///roster.db")

with open("students.csv", "r") as file:
    insert = csv.DictReader(file)

    for row in insert:
        print(row['house'])
        try:
            db.execute("INSERT INTO link (student_id, student_house) VALUES (?, ?);", row['id'], row['house'])
        except Exception:
            continue
