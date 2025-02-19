import psycopg2


class DataBase:
    database = "link_db"
    host = "localhost"
    port = "5432"

    def __init__(self):
        self.conn = psycopg2.connect(database=self.database, host=self.host,
                                     port=self.port)
        self.cur = self.conn.cursor()
