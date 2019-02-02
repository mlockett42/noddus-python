#!/usr/bin/python3

import sqlite3
import sys
import csv

if len(sys.argv) < 2:
    print("Error: No file specified")
    sys.exit()



conn = sqlite3.connect('grades.db')

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='grades';")
if len(c.fetchall()) == 0:
    # Create table
    c.execute('''CREATE TABLE grades
                 (id integer primary key autoincrement, student text, subject text, grade int)''')

    conn.commit()

rows_processed = 0
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile)
    is_header = True
    for row in reader:
        if not is_header:
            c.execute("INSERT INTO grades (student, subject, grade) VALUES "
                      "(?, ?, ?)", (row[0], row[1], row[2]))
            rows_processed += 1
        else:
            is_header = False

c.execute("SELECT count(*) FROM grades;")
row_count = c.fetchone()[0]

conn.commit()

conn.close()

print("{inserted} records inserted. Total records are {total}"
      .format(inserted=rows_processed, total=row_count))
