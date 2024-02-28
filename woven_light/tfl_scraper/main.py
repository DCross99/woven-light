import time
from db_connector import connect
from scrape import scrape_urls_from_db


def main():
    while True:
        try:
            conn = connect()
            break
        except:
            print("Sleeping for 1 minutes as db is not ready")
            time.sleep(60)
    while True:
        scrape_urls_from_db(conn)
        # Sleep for 5 minutes, so we do not hammer tfl endpoint/ db
        print("Sleeping for 5 minutes")
        time.sleep(300)


main()
