from database import Database

class InterfaceReseauRoute():

    def create(self, values) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO interface_reseau_route(id_interface_reseau_route, ip_destination, masque_reseau, ip_interface, ttl, id_interface_reseau) VALUES (?, ?, ?, ?, ?) """, (value))
        create = cursor.commit()
        return
    
    def update(self, id_partition, label, espace_libre, espace_utilise, id_disque_dur) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE partition_dd SET label = ?, espace_libre = ?, espace_utilise = ?, id_disque_dur = ? WHERE id_partition = ? """, (label, espace_libre, espace_utilise, id_disque_dur, id_partition))
        update = cursor.commit()
        return
    
    def delete(self, id_interface_reseau_route) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" DELETE FROM partition_dd WHERE id_partition = ? """, (id_interface_reseau_route))
        delete = cursor.commit()
        return

    def selectByIpDestination(ipDestination):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = ? """, (ipDestination))
        ipDestination = cursor.fetchall()
        return ipDestination
    
    def selectByMasqueReseau(masqueReseau):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = ? """, (masqueReseau))
        masqueReseau = cursor.fetchall()
        return masqueReseau

    def selectByIpPasserelle(ipPasserelle):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = ? """, (ipPasserelle))
        ipPasserelle = cursor.fetchall()
        return ipPasserelle
    
    def selectByIpInterface(ipInterface):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = ? """, (ipInterface))
        ipInterface = cursor.fetchall()
        return ipInterface

    def selectByInterfaceReseau(interfaceReseau):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" SELECT * FROM partition_dd WHERE label = ? """, (interfaceReseau))
        interfaceReseau = cursor.fetchall()
        return interfaceReseau