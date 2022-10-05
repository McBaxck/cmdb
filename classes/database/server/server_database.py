from dataclasses import dataclass
from classes.database.interfaces.interface_database import IDatabase
from database import Database

@dataclass
class ServerDatabase(IDatabase):

    def create(self,id_server: int, label: str, hostname: str, serveur_type: str, cpu: str, gpu: str) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Serveur (id_server, label, hostname, serveur_type, cpu, gpu) VALUES(?, ?, ?, ?, ?, ?) ;""", (id_server, label, hostname, serveur_type, cpu, gpu))
        con.commit()
        cursor.close()


    def update(self,label: str, hostname: str, serveur_type: str, cpu: str, gpu: str, id_server: str) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""UPDATE Securite SET label=?, hostname=?, serveur_type=?, cpu=?, gpu=? WHERE id_server=? ;""", (label, hostname, serveur_type, cpu, gpu, id_server))
        con.commit()
        cursor.close()

    def delete(self, id_server: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""DELETE FROM Server WHERE id_server=? ;""", (id_server))
        con.commit()
        cursor.close()

    def selectByLabel(label: str = "") -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Serveur WHERE label=? ;""", (label))
        label = cursor.fetchall()
        cursor.close()
        return label
    
    def selectByHostname(self, hostname: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Serveur WHERE hostname=?;""", (hostname))
        server = cursor.fetchall()
        cursor.close()
        return server