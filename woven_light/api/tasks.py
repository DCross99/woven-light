import json

from db.db_connector import connect


def get_tasks(id: str | None = None) -> str:
    if id:  # get task from one id
        return get_one_task(id)
    else:  # get all tasks
        return get_all_tasks()


def get_one_task(id: str) -> str:
    try:
        casting_id = int(id)
    except:
        raise ValueError(f"Invalid id: {id}")

    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT id, schedule_time, tfl_url FROM tasks WHERE id={casting_id};"
        )
        row = cursor.fetchone()
    if len(row) == 0 or row[0] is None:
        return f"No task found for id {casting_id}"

    dict = {
        row[0]: {"schedule_time": row[1], "tfl_url": row[2], "tfl_response": row[3]}
    }
    return json.dumps(dict, indent=4, default=str)


def get_all_tasks() -> str:
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, schedule_time, tfl_url FROM tasks;")
        rows = cursor.fetchall()
    dict = {}
    for row in rows:
        dict[row[0]] = {
            "schedule_time": str(row[1]),
            "tfl_url": row[2],
            "tfl_response": row[3],
        }
    return json.dumps(dict, indent=4, default=str)
