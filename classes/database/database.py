import sqlite3
from sqlite3 import Error, Connection
from dataclasses import dataclass
from classes.database import DATABASE_PATH


@dataclass
class Database():
    _path: str = DATABASE_PATH

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value

    def _open(self) -> Connection:
        """ Open a database and return the current connection """
        conn = None
        try:
            conn = sqlite3.connect(self._path)
        except Error as e:
            quit(code=e)
        return conn
