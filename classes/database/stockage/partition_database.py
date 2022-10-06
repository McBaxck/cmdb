from classes.database.database import Database
from classes.server.stockage.partition import Partition
from typing import Any
import sys
sys.path.append("./")


class PartitionDatabase():

    def create(self, id_partition: int, label: str, espace_libre: int, espace_utilise: int, id_disque_dur: int) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ INSERT INTO partition_dd(id_partition, label, espace_libre, espace_utilise, id_disque_dur) VALUES (?, ?, ?, ?, ?) """,
            (id_partition, label, espace_libre, espace_utilise, id_disque_dur))
        con.commit()
        con.close()
        return 'OK'

    def update(self, id_partition, label, espace_libre, espace_utilise, id_disque_dur) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE partition_dd SET label = ?, espace_libre = ?, espace_utilise = ?, id_disque_dur = ? WHERE id_partition = ? """,
                       (label, espace_libre, espace_utilise, id_disque_dur, id_partition))
        con.commit()
        con.close()
        return 'OK UPDATE'

    def tailored_update(self, id_partition: int, field: str, value: Any) -> str:
        db = Database()
        conn = db._open()
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE partition_dd SET {field}=? WHERE id_partition=? ;""",
                       (str(value), id_partition))
        conn.commit()
        conn.close()
        return f'OK UPDATE FIELD {field} FOR PARTITION'

    def delete(self, id_partition) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ DELETE FROM partition_dd WHERE id_partition = ? """, (str(id_partition),))
        con.commit()
        con.close()
        return 'OK'

    def selectByLabel(self, label):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE label = '""" + label + """';""")
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        con.close()
        return liste_partition

    def selectByEspaceLibreBetween(self, min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE espace_libre > ? AND espace_libre < ? """, (min, max))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        con.close()
        return liste_partition

    def selectByEspaceUtiliseBetween(self, min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE espace_utilise >= ? AND espace_utilise <= ? """, (min, max))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        con.close()
        return liste_partition

    def selectById(self, id):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        print(id)
        cursor.execute(
            """SELECT * FROM partition_dd WHERE id_partition=?""", str(id))
        rs = cursor.fetchone()
        rs = Partition(rs[1], rs[2], rs[3])
        con.close()
        return [rs]

    def selectByIdDisk(self, id):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM partition_dd WHERE id_disque_dur=?""", str(id))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        con.close()
        return liste_partition

    def selectAll(self):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """SELECT * FROM partition_dd ;""")
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        con.close()
        return liste_partition
