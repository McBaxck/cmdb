from dataclasses import dataclass
from classes.database.interfaces.interface_database import IDatabase
from database import Database

@dataclass
class SecuriteDatabase(IDatabase):

    def create(self,ip_firewall: str, id_securite: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Securite (ip_firewall, id_securite) VALUES(?, ?) ;""", (ip_firewall, id_securite))
        con.commit()


    def update(self, ip_firewall: str, id_securite: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""UPDATE Securite SET ip_firewall=? WHERE id_securite=? ;""", (ip_firewall, id_securite))
        con.commit()

    def delete(self, id_securite: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""DELETE FROM Securite WHERE id_securite=? ;""", (id_securite))
        con.commit()

    def selectByIp(ip: str = "") -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Securite WHERE ip_firewall=? ;""", (ip))
        label = cursor.fetchall()
        return label
    
    def selectByServer(self, id_server: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Securite\
                        WHERE id_securite IN(\
                        SELECT id_securite FROM serveur_securite\
                        WHERE id_serveur = ?);""", (id_server))
        server = cursor.fetchall()
        return server