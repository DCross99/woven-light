import csv
import sqlite3


def prepare_fixture_data():
    conn = sqlite3.connect("database.db")

    with open('data.csv', 'r') as f:
        tasks = [(i['id'], i['schedule_time'], i["tube_lines"]) for i in csv.DictReader(f)]

    conn.cursor().executemany("INSERT INTO tasks (id, schedule_time, tube_lines) VALUES (?, ?, ?);", tasks)
    conn.commit()
    conn.close()


# TODO: Ran out of time, I would of liked to write integration tests for both post and get endpoint of tasks
"""
These tests would of included:

Post:
    Valid single tube line and valid date
    Valid multiple tube lines and valid date
    Valid single tube line but no date
    Valid multiple tube line but no date
    
    Invalid single tube (not a tube line)
    Invalid multiple tube lines (not a tube line)
    Invalid single tube (capitalised)
    
    Invalid date

Get:
    No tasks in db
    Tasks in db
    
    Valid id given
    Invalid id given
    Valid id but no task associated
"""
