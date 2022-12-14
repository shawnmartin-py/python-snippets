from collections import abc
from contextlib import suppress
from operator import itemgetter
import sqlite3


class SQLDict(abc.MutableMapping):
    def __init__(self, dbname, items = None, *kwargs):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        c = self.conn.cursor()
        with suppress(sqlite3.OperationalError):
            c.execute("CREATE TABLE Dict (key text, value text)")
            c.execute("CREATE UNIQUE INDEX Kndx ON Dict (key)")
        self.update(**kwargs)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        with self.conn as c:
            c.execute("INSERT INTO Dict VALUES (?, ?)", (key, value))

    def __getitem__(self, key):
        c = self.conn.execute("SELECT value FROM Dict WHERE key=?", (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return row[0]

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        with self.conn as c:
            c.execute("DELETE FROM Dict WHERE key=?", (key,))

    def __len__(self):
        return next(self.conn.execute("SELECT COUNT(*) FROM Dict"))[0]

    def __iter__(self):
        c = self.conn.execute("SELECT key FROM Dict")
        return map(itemgetter(0), c.fetchall())

    def __repr__(self):
        return (
            f"{type(self).__name__}(dbname={self.dbname!r}, "
            f"items={list(self.items())}"
        )

    def close(self):
        self.conn.close()