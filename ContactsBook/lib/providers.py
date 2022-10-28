import sqlite3


class SQLiteProvider(object):

    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()
