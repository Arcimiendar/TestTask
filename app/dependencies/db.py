from typing import Union

import psycopg2


class ConnectionFactory:
    url: str | None

    @classmethod
    def get_connection(cls) -> 'psycopg2.connection':
        if cls.url is None:
            raise RuntimeError('Cursor factory needs to be initialized first')
        return psycopg2.connect(cls.url)

    @classmethod
    def initialize(cls, url):
        cls.url = url


# Dependency
def get_connection():
    conn = ConnectionFactory.get_connection()
    try:
        yield conn
    finally:
        conn.close()
