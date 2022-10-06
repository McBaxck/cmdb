from classes.database.stockage.partition_database import PartitionDatabase
from classes.server.stockage.dd import HardDisk
from classes.database.database import Database
from classes.database.interfaces.interface_database import IDatabase
from classes.server.stockage.dd import *
from dataclasses import dataclass
import sys
sys.path.append("./")


@dataclass
class DisqueDurDatabase(IDatabase):

    def create(self, label: str, espace_libre: int, espace_utilise: int, format_disque: str, id_serveur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Disque_Dur (label, espace_libre, espace_utilise, format_disque, id_serveur) VALUES(?, ?, ?, ?, ?) ;""",
                       (label, espace_libre, espace_utilise, format_disque, id_serveur))
        con.commit()
        con.close()
        return 'OK'

    def update(self, label: str, espace_libre: int, espace_utilise: int, id_serveur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""UPDATE Disque_Dur SET label=?, espace_libre=?, espace_utilise=?, id_serveur=? WHERE id_disque_dur = ? ;""",
                       (label, espace_libre, espace_utilise, id_serveur))
        con.commit()
        con.close()
        return 'OK'

    def delete(self, id_disque_dur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """DELETE FROM Disque_Dur WHERE id_disque_dur=? ;""", (str(id_disque_dur),))
        con.commit()
        con.close()
        return 'OK DELETE DISK'

    def selectByLabel(value: str = "") -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE label = ? ;""", (value))
        rs = cursor.fetchall()
        rs = DisqueDurDatabase.toObject(rs)
        con.close()
        return rs

    def selectByEspaceLibre(self, valeur_basse: int, valeur_haute: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE espace_libre<=? AND espace_libre >=? ;""", (valeur_basse, valeur_haute))
        rs = cursor.fetchall()
        rs = DisqueDurDatabase.toObject(rs)
        con.close()
        return rs

    def selectByEspaceUtilise(self, valeur_basse: int, valeur_haute: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE espace_utilise<=? AND espace_utilise>=? ;""", (valeur_basse, valeur_haute))
        rs = cursor.fetchall()
        rs = DisqueDurDatabase.toObject(rs)
        con.close()
        return rs

    def selectByServer(self, value: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE id_serveur = ? ;""", (str(value)))
        rs = cursor.fetchall()
        rs = DisqueDurDatabase.toObject(rs)
        con.close()
        return rs

    def selectLastId(self) -> int:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT dd.id_disque_dur FROM Disque_Dur AS dd ORDER BY dd.id_disque_dur DESC LIMIT 0,1""")
        rs = cursor.fetchone()
        con.close()
        return rs

    def selectAll(self, id_serveur: int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE id_serveur=? ;""", (str(id_serveur),))
        rs = cursor.fetchall()
        rs = DisqueDurDatabase.toObject(rs)
        con.close()
        return rs

    def selectById(self, id) -> HardDisk:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM Disque_Dur WHERE id_disque_dur=?""", str(id))
        rs = cursor.fetchone()
        rs = HardDisk(rs[1], rs[2], rs[3],
                      PartitionDatabase.selectByIdDisk(rs[0]))
        con.close()
        return [rs]

    def toObject(rs):
        list_disk = []
        for i in rs:
            list_disk.append(
                HardDisk(i[1], i[2], i[3], PartitionDatabase.selectByIdDisk(i[0])))
        return list_disk
