from datetime import datetime

from flask import Request

from db.db_connector import connect
from tfl_url import base_tfl_url


class LinesToSchedule:
    def __init__(self, request: Request):
        self.request_json = request.get_json()
        self._get_schedule_time()
        self._get_tfl_url()

    def _get_schedule_time(self):
        datetime_format = "%Y-%m-%dT%H:%M:%S"
        self.schedule_time = datetime.strptime(
            self.request_json["scheduler_time"], datetime_format
        )

    def _get_tfl_url(self):
        tube_lines_string = self.request_json["lines"]
        tube_lines = tube_lines_string.replace(" ", "").split(",")
        self.tfl_url = base_tfl_url(tube_lines)


def schedule_lines(request: Request) -> str:
    lines_to_schedule = LinesToSchedule(request)
    conn = connect()
    with conn.cursor() as cursor:
        sql_insert = f"INSERT INTO tasks (schedule_time, tfl_url) VALUES ('{lines_to_schedule.schedule_time}', '{lines_to_schedule.tfl_url}');"
        cursor.execute(sql_insert)
        conn.commit()
    return f"A schedule task has been added at {lines_to_schedule.schedule_time} for the URL {lines_to_schedule.tfl_url}"
