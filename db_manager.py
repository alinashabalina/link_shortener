from db import DataBase


class Link:
    def __init__(self, modified, timestamp, duration):
        self.modified = modified
        self.timestamp = timestamp
        self.duration = duration


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

    def add_link(self, link, modified_link, timestamp):
        self.cur.execute('INSERT INTO links (initial, modified, timestamp)'
                         'VALUES (%s, %s, %s)',
                         (link, modified_link, timestamp))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM links WHERE links.initial = '{link}'")
        data = self.cur.fetchone()
        return Link(data[2], data[3], "72 hours")
