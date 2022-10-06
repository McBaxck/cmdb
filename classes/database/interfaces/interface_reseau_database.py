from classes.database.database import Database
from classes.server.config.interface_reseau import InterfaceReseau
from classes.database.interfaces.interface_database import IDatabase
import sys
sys.path.append("./")


class InterfaceReseauDatabase(IDatabase):

    def create(self, interfaceReseau: InterfaceReseau, id_serveur) -> str:
        db = Database()
        con = db._open()
        cursor = con.cursor()

        cursor.execute(""" INSERT INTO interface_reseau(id_interface_reseau, ip_source, port, ip_passerelle, id_serveur) VALUES (?, ?, ?, ?, ?) """,
                       (self.selectLastId()[0]+1, interfaceReseau.ipSource, interfaceReseau.port, interfaceReseau.passerelle, id_serveur))
        con.commit()
        con.close()
        return 'OK'

    def update(self, interfaceReseau: InterfaceReseau) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE interface_reseau SET ip_source = ?, port = ?, ip_passerelle = ?, id_serveur = ?) WHERE id_interface_reseau = ?""",
                       (interfaceReseau.ipSource, interfaceReseau.port, interfaceReseau.passerelle, interfaceReseau.ipServer, interfaceReseau.idInterfaceReseau))
        con.commit()
        con.close()
        return 'OK'

    def delete(self, id_interface_reseau: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" DELETE FROM interface_reseau WHERE id_interface_reseau = ?;""",
                       (str(id_interface_reseau)))
        con.commit()
        con.close()
        return 'OK'

    def selectLastId(self) -> int:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT ir.id_interface_reseau FROM interface_reseau AS ir ORDER BY ir.id_interface_reseau DESC LIMIT 0,1""")
        rs = cursor.fetchone()
        con.commit()
        con.close()
        return rs

    def selectAll(self):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau""")
        rs = cursor.fetchall()
        con.close()
        return rs

    def selectById(self, id: int) -> InterfaceReseau:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM interface_reseau AS ir WHERE ir.id_interface_reseau = ?""", (id))
        rs = cursor.fetchone()
        con.commit()
        con.close()
        return rs

    def selectByIpSource(self, ipSource: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM interface_reseau AS ir WHERE ir.ip_source = ?""", (ipSource))
        rs = cursor.fetchall()
        con.close()
        return rs

    def selectByPort(self, port: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM interface_reseau AS ir WHERE ir.port = ?""", (port))
        rs = cursor.fetchall()
        con.commit()
        con.close()
        return rs

    def selectByPasserelle(self, passerelle: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM interface_reseau AS ir WHERE ir.passerelle = ?""", (passerelle))
        rs = cursor.fetchall()
        con.commit()
        con.close()
        return rs

    def selectByServeur(self, serverId: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM interface_reseau WHERE id_server = ?""", (serverId))
        rs = cursor.fetchall()
        con.commit()
        con.close()
        return rs
