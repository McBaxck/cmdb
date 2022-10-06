from typing import Any
from classes.database.database import Database
from classes.database.interfaces.interface_database import IDatabase
from dataclasses import dataclass
import sys
sys.path.append("./")


@dataclass
class ServerDatabase(IDatabase):

    def create(self, id_server: int, label: str, hostname: str, serveur_type: str, cpu: str, gpu: str) -> None:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Serveur (id_serveur, label, hostname, serveur_type, cpu, gpu) VALUES(?, ?, ?, ?, ?, ?) ;""",
                       (id_server, label, hostname, serveur_type, cpu, gpu))
        conn.commit()
        conn.close()
        return "OK"

    def update(self, label: str, hostname: str, serveur_type: str, cpu: str, gpu: str, id_server: str) -> str:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute("""UPDATE Serveur SET label=?, hostname=?, serveur_type=?, cpu=?, gpu=? WHERE id_serveur=? ;""",
                       (label, hostname, serveur_type, cpu, gpu, id_server))
        con.commit()
        conn.close()
        return 'OK UPDATE SERVER'

    def tailored_update(self, id_serveur: int, field: str, value: Any) -> str:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE Serveur SET {field}=? WHERE id_serveur=? ;""",
                       (str(value), id_serveur))
        conn.commit()
        conn.close()
        return f'OK UPDATE FIELD {field} FOR SERVER'

    def delete(self, id_server: int) -> None:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute(
            """DELETE FROM Serveur WHERE id_serveur=? ;""", (str(id_server),))
        conn.commit()
        conn.close()
        return "OK"

    def selectAll(self) -> list:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Serveur ;""")
        label = cursor.fetchall()
        conn.close()
        return label

    def selectByLabel(self, label: str = "") -> list:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Serveur WHERE label=? ;""", (label))
        label = cursor.fetchall()
        conn.close()
        return label

    def selectByHostname(self, hostname: int) -> list:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM Serveur WHERE hostname=?;""", (hostname))
        server = cursor.fetchall()
        conn.close()
        return server

    def selectById(self, id: int) -> Any:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM Serveur WHERE id_serveur=?;""", str(id))
        server = cursor.fetchall()
        conn.close()
        return server

    def selectLastId(self) -> Any:
        return 'ok'
