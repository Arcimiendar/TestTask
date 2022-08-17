import psycopg2


class ConnectionFactory:
    """
    Factory of connection
    """
    url: str | None

    @classmethod
    def get_connection(cls) -> 'psycopg2.connection':
        """
        :return: produce new connection to DB
        """
        if cls.url is None:
            raise RuntimeError('Cursor factory needs to be initialized first')
        return psycopg2.connect(cls.url)

    @classmethod
    def initialize(cls, url):
        cls.url = url


# Dependency
def get_connection():
    """
    Created for using in "Depends" function of FastAPI
    :return: generator yields connection then closes it on next step.
    """
    conn = ConnectionFactory.get_connection()
    try:
        yield conn
    finally:
        conn.close()
