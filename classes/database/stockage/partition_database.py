import sys
sys.path.append("./")
from classes.server.stockage.partition import Partition
from classes.database.database import Database


class PartitionDatabase():
    
    def create(self, values) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO partition_dd(ud_partition, label, espace_libre, espace_utilise, id_disque_dur) VALUES (?, ?, ?, ?, ?) """, (values))
        create = cursor.commit()
        cursor.close()
        return
    
    def update(self, id_partition, label, espace_libre, espace_utilise, id_disque_dur) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE partition_dd SET label = ?, espace_libre = ?, espace_utilise = ?, id_disque_dur = ? WHERE id_partition = ? """, (label, espace_libre, espace_utilise, id_disque_dur, id_partition))
        update = cursor.commit()
        cursor.close()
        return
    
    def delete(self, id_partition) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" DELETE FROM partition_dd WHERE id_partition = ? """, (id_partition))
        delete = cursor.commit()
        cursor.close()
        return

    def selectByLabel(label):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = '""" + label + """';""")
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        cursor.close()
        return liste_partition
    
    def selectByEspaceLibreBetween(min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE espace_libre > ? AND espace_libre < ? """, (min, max))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        cursor.close()
        return liste_partition

    def selectByEspaceUtiliseBetween(min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE espace_utilise >= ? AND espace_utilise <= ? """, (min, max))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        cursor.close()
        return liste_partition
    
    def selectById(id):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        print(id)
        cursor.execute("""SELECT * FROM partition_dd WHERE id_partition=?""", str(id))
        rs = cursor.fetchone()
        rs = Partition(rs[1], rs[2], rs[3])
        cursor.close()
        return rs

    def selectByIdDisk(id):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition_dd WHERE id_disque_dur=?""", str(id))
        rs = cursor.fetchall()
        liste_partition = []
        for i in rs:
            liste_partition.append(Partition(i[1], i[2], i[3]))
        cursor.close()
        return liste_partition