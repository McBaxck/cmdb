from classes.database.interfaces.interface_database import IDatabase
from classes.database.interfaces.interface_reseau_route_database import InterfaceReseauRouteDatabase
from classes.server.config.interface_reseau import InterfaceReseau
from classes.database.database import Database

class InterfaceReseauDatabase(IDatabase):

    def create(self, interfaceReseau: InterfaceReseau, idServeur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO interface_reseau(id_interface_reseau, ip_source, port, ip_passerelle, id_serveur) VALUES (?, ?, ?, ?, ?) """, (self.selectLastId()+1, interfaceReseau.ipSource, interfaceReseau.port, interfaceReseau.passerelle, idServeur))
        con.commit()
        return
    
    def update(self, interfaceReseau: InterfaceReseau) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE interface_reseau SET ip_source = ?, port = ?, ip_passerelle = ?) WHERE id_interface_reseau = ?""", (interfaceReseau.ipSource, interfaceReseau.port, interfaceReseau.passerelle, interfaceReseau.idInterfaceReseau))
        con.commit()
        return
    
    def delete(self, interfaceReseau: InterfaceReseau) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" DELETE FROM interface_reseau WHERE id_interface_reseau = ? """, (interfaceReseau.idInterfaceReseau))
        con.commit()
        return

    def selectLastId(self) -> int:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT ir.id_interface_reseau FROM interface_reseau AS ir ORDER BY ir.id_interface_reseau DESC LIMIT 0,1""")
        rs = cursor.fetchone()
        return rs

    def selectAll(self):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau""")
        rs = cursor.fetchall()
        return rs

    def selectById(id: int) -> InterfaceReseau:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau AS ir WHERE ir.id_interface_reseau = ?""", (id))
        rs = cursor.fetchone()
        return rs

    def selectByIpSource(ipSource: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau AS ir WHERE ir.ip_source = ?""", (ipSource))
        rs = cursor.fetchall()
        return rs
    
    def selectByPort(port: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau AS ir WHERE ir.port = ?""", (port))
        rs = cursor.fetchall()
        return rs

    def selectByPasserelle(passerelle: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau AS ir WHERE ir.passerelle = ?""", (passerelle))
        rs = cursor.fetchall()
        return rs
    
    def selectByServeur(serverId: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM interface_reseau WHERE id_server = ?""", (serverId))
        rs = cursor.fetchall()
        return rs