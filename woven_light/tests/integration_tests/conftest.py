import psycopg2
import pytest


@pytest.fixture()
def postgres_connection():
    """Connect to the PostgreSQL database server"""
    with psycopg2.connect(
        host="db", database="db_test", user="postgres", password="postgres"
    ) as conn:
        conn.autocommit = True
        print("Connected to the PostgreSQL server.")
