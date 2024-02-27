import psycopg2


def connect():
    """Connect to the PostgreSQL database server"""
    try:
        with psycopg2.connect(
            host="db", database="db", user="postgres", password="postgres"
        ) as conn:
            conn.autocommit = True
            print("Connected to the PostgreSQL server.")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        raise error
