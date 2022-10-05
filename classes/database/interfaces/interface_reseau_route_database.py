from database import Database


class InterfaceReseauRoute():

    def create(self, values) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO interface_reseau_route(id_interface_reseau_route, ip_destination, masque_reseau, ip_interface, ttl, id_interface_reseau) VALUES (?, ?, ?, ?, ?) """, (value))
        create = cursor.commit()
        return

    def update(self, id_route: int, ip_destination: str, masque_reseau: str, ip_interface: str, ttl: int, id_interface_reseau: int) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE interface_reseau_route SET label = ?, espace_libre = ?, espace_utilise = ?, id_disque_dur = ? WHERE id_partition = ? """,
                       (label, espace_libre, espace_utilise, id_disque_dur, id_partition))
        update = cursor.commit()
        return

    def delete(self, id_interface_reseau_route: int) -> None:
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ DELETE FROM interface_reseau_route WHERE id_interface_reseau_route = ? """, (id_interface_reseau_route))
        delete = cursor.commit()
        return

    def select_by_ip_destination(ip_destination: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE ip_destination = ? """, (ip_destination))
        ipDestination = cursor.fetchall()
        return ipDestination

    def select_by_masque_reseau(masque_reseau: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE masque_reseau = ? """, (masque_reseau))
        masqueReseau = cursor.fetchall()
        return masqueReseau

    def select_by_ip_interface(ip_interface: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE ip_interface = ? """, (ip_interface))
        ipInterface = cursor.fetchall()
        return ipInterface

    def select_by_interface_reseau(id_interface_reseau: int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE id_interface_reseau = ? """, (id_interface_reseau))
        interfaceReseau = cursor.fetchall()
        return interfaceReseau
