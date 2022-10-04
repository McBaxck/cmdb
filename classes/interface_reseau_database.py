from classes.interface_reseau import InterfaceReseau
from database import Database

class InterfaceReseauDatabase():

    def create(self) -> None:
        return
    
    def update(self) -> None:
        return
    
    def delete(self) -> None:
        return

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