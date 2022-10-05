from classes.database.database import Database


class PartitionDatabase():

    def create(self, values) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ INSERT INTO partition_dd(ud_partition, label, espace_libre, espace_utilise, id_disque_dur) VALUES (?, ?, ?, ?, ?) """, (value))
        create = cursor.commit()
        return

    def update(self, id_partition, label, espace_libre, espace_utilise, id_disque_dur) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE partition_dd SET label = ?, espace_libre = ?, espace_utilise = ?, id_disque_dur = ? WHERE id_partition = ? """,
                       (label, espace_libre, espace_utilise, id_disque_dur, id_partition))
        update = cursor.commit()
        return

    def delete(self, id_partition) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ DELETE FROM partition_dd WHERE id_partition = ? """, (id_partition))
        delete = cursor.commit()
        return

    def selectByLabel(label):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE label = ? """, (label))
        label = cursor.fetchall()
        return label

    def selectByEspaceLibreBetween(min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE espaceLibre > ? AND espaceLibre < ? """, (min, max))
        espaceLibreBetween = cursor.fetchall()
        return espaceLibreBetween

    def selectByEspaceUtiliseBetween(min, max):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE espaceUtilise > ? AND espaceUtilise < ? """, (min, max))
        espaceUtiliseBetween = cursor.fetchall()
        return espaceUtiliseBetween

    def selectByDisqueDur(disqueDur):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM partition_dd WHERE disqueDur = ? """, (disqueDur))
        disqueDur = cursor.fetchall()
        return disqueDur
