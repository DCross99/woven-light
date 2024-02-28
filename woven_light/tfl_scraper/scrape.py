from datetime import datetime

import requests


def scrape_urls_from_db(conn):
    with conn.cursor() as cursor:
        sql_select = """
                               SELECT id, schedule_time, tfl_url FROM tasks
                               WHERE schedule_time <= NOW() + INTERVAL '5 minute'
                               AND tfl_url IS NOT NULL
                               AND tfl_response IS NULL;
                           """
        cursor.execute(sql_select)
        rows = cursor.fetchall()
    print(f"Found {len(rows)} rows to scrape")
    for row in rows:
        print("Url to scrape:", row[2])
        description = scrape(str(row[2]))
        if description:
            with conn.cursor() as cur:
                current_time = datetime.now()
                sql_update = f"UPDATE tasks SET tfl_response = '{description}', scrape_time = '{current_time}' WHERE id = {row[0]};"
                cur.execute(sql_update)
                conn.commit()


def scrape(url_to_scrape: str) -> str | None:
    description = ""
    response = requests.get(url_to_scrape)
    if response.status_code == 200:
        try:
            json_response = response.json()
            print(json_response)
            description = json_response[0]["description"]
        except KeyError:
            print("ERROR: No description returned")
    else:
        print("ERROR: Response code:", response.status_code)
    if description != "":
        return description
