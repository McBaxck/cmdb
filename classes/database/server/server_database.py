from dataclasses import dataclass
from classes.database.interfaces.interface_database import IDatabase
from classes.database.database import Database
from typing import Any


@dataclass
class ServerDatabase(IDatabase):

    def create(self, id_server: int, label: str, hostname: str, serveur_type: str, cpu: str, gpu: str) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Serveur (id_serveur, label, hostname, serveur_type, cpu, gpu) VALUES(?, ?, ?, ?, ?, ?) ;""",
                       (id_server, label, hostname, serveur_type, cpu, gpu))
        con.commit()
        con.close()
        return 'OK CREATE'

    def update(self, label: str, hostname: str, serveur_type: str, cpu: str, gpu: str, id_server: str) -> str:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""UPDATE Serveur SET label=?, hostname=?, serveur_type=?, cpu=?, gpu=? WHERE id_serveur=? ;""",
                       (label, hostname, serveur_type, cpu, gpu, id_server))
        con.commit()
        con.close()
        return 'OK UPDATE'

    def single_update(self, field: str, value: Any, id_serveur: int) -> str:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            f"""UPDATE Serveur SET {field}=? WHERE id_serveur=?;""", (str(value), str(id_serveur)))
        con.commit()
        con.close()
        return f'OK UPDATE FOR {field}'

    def delete(self, id_server: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """DELETE FROM Serveur WHERE id_serveur=? ;""", (str(id_server),))
        con.commit()
        con.close()
        return 'OK DELETE'

    def selectAll(self) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Serveur ;""")
        label = cursor.fetchall()
        con.close()
        return label

    def selectByLabel(self, label: str = "") -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Serveur WHERE label=? ;""", (label))
        label = cursor.fetchall()
        con.close()
        return label

    def selectByHostname(self, hostname: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Serveur WHERE hostname=?;""", (hostname))
        server = cursor.fetchall()
        con.close()
        return server

    def selectById(self, id: int) -> Any:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Serveur WHERE id_serveur=? ;""", (str(id)))
        label = cursor.fetchall()
        con.close()
        return label

    def selectLastId(self) -> Any:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Serveur WHERE id_serveur=? ;""", (str(id)))
        label = cursor.fetchall()
        con.close()
        return label
