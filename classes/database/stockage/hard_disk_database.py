from dataclasses import dataclass
from interface_database import IDatabase
from database import Database

@dataclass
class DisqueDurDatabase(IDatabase):

    def create(self, label: str, espace_libre: int, espace_utilise: int, id_serveur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Disque_Dur (label, espace_libre, espace_utilise, id_serveur) VALUES(?, ?, ?, ?, ?) ;""", (label, espace_libre, espace_utilise, id_serveur))
        con.commit()


    def update(self, label: str, espace_libre: int, espace_utilise: int, id_serveur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""UPDATE Disque_Dur SET label=?, espace_libre=?, espace_utilise=?, id_serveur=? WHERE id_disque_dur = ? ;""", (label, espace_libre, espace_utilise, id_serveur))
        con.commit()

    def delete(self, id_disque_dur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""DELETE FROM Disque_Dur WHERE id_disque_dur=? ;""", (id_disque_dur))
        con.commit()

    def selectByLabel(value: str = "") -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Disque_Dur WHERE label = ? ;""", (value))
        label = cursor.fetchall()
        return label
    
    def selectByEspaceLibre(self, valeur_basse: int, valeur_haute: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Disque_Dur WHERE espace_libre<=? AND espace_libre >=? ;""", (valeur_basse, valeur_haute))
        espace_libre = cursor.fetchall()
        return espace_libre

    def selectByEspaceUtilise(self, valeur_basse: int, valeur_haute: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Disque_Dur WHERE espace_utilise<=? AND espace_utilise>=? ;""", (valeur_basse, valeur_haute))
        espace_utilise = cursor.fetchall()
        return espace_utilise
    
    def selectByServer(self, value: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Disque_Dur WHERE id_serveur = ? ;""", (value))
        id_serveur = cursor.fetchall()
        return id_serveur