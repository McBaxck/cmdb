import sqlite3
import logger
from sqlite3 import Error
from dataclasses import dataclass


@dataclass
class Database():
    _path: str

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value

    def _open(self) -> sqlite3.Connection:
        """ Open a database and return the current connection """
        conn = None
        try:
            conn = sqlite3.connect(self._path)
        except Error as e:
            quit(code=e)
        return conn

    def _close(self, connection: sqlite3.Connection) -> None:
        """ Close the current database connection """
        connection.close()
