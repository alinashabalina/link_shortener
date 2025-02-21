from db import DataBase


class Link:
    def __init__(self, modified, expiration):
        self.modified = modified
        self.expiration = expiration


class LinkDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS links
(
    id
    serial \
    PRIMARY
    KEY,
    initial
    varchar, modified varchar, timestamp timestamp);
    CREATE INDEX IF NOT EXISTS link_idx
  ON links (modified ASC);

''')
        self.conn.commit()

    def add_link(self, link, modified_link, timestamp, expiration_time):
        self.cur.execute('INSERT INTO links (initial, modified, timestamp, expiration_time)'
                         'VALUES (%s, %s, %s, %s)',
                         (link, modified_link, timestamp, expiration_time))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM links WHERE links.initial = '{link}' ORDER BY links.id DESC")
        data = self.cur.fetchone()
        return Link(data[2], data[4])

    def check_link(self, modified_link):
        self.cur.execute(f"SELECT * FROM links WHERE links.modified = '{modified_link}'")
        data = self.cur.fetchone()
        return Link(data[1], data[4])
