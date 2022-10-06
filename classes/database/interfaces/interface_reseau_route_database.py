from classes.database.interfaces.interface_database import IDatabase
from classes.server.config.interface_reseau_route import InterfaceReseauRoute
from classes.database.database import Database


class InterfaceReseauRouteDatabase(IDatabase):

    def create(self, interfaceReseauRoute: InterfaceReseauRoute, idParent: int) -> None:
        db: Database = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO interface_reseau_route(id_interface_reseau_route, ip_destination, masque_reseau, ip_interface, ttl, id_interface_reseau) VALUES (?, ?, ?, ?, ?) """, (1, interfaceReseauRoute.ipDestination, interfaceReseauRoute.masqueReseau,interfaceReseauRoute.ipInterface, interfaceReseauRoute.ttl, idParent))
        con.commit()
        con.close()
        return

    def update(self, interfaceReseauRoute: InterfaceReseauRoute) -> None:
        db: Database = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE interface_reseau_route SET ip_destination = ?, masque_reseau = ?, ip_interface = ?, ttl = ? WHERE id_interface_reseau_route = ? """,
                       (interfaceReseauRoute.ipDestination, interfaceReseauRoute.masqueReseau, interfaceReseauRoute.ipInterface, interfaceReseauRoute.ttl, interfaceReseauRoute.id))
        con.commit()
        con.close()
        return

    def delete(self, id_interface_reseau_route: int) -> None:
        db: Database = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ DELETE FROM interface_reseau_route WHERE id_interface_reseau_route = ? """, (id_interface_reseau_route))
        delete = cursor.commit()
        con.close()
        return

    def selectAll(self):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""
        SELECT * FROM interface_reseau_route
        """)
        rs = cursor.fetchall()
        return rs

    def selectById(self, id: int):
        pass

    def selectLastId(self):
        pass

    def select_by_ip_destination(ip_destination: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE ip_destination = ? """, (ip_destination))
        ipDestination = cursor.fetchall()
        con.close()
        return ipDestination

    def select_by_masque_reseau(masque_reseau: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE masque_reseau = ? """, (masque_reseau))
        masqueReseau = cursor.fetchall()
        con.close()
        return masqueReseau

    def select_by_ip_interface(ip_interface: str):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE ip_interface = ? """, (ip_interface))
        ipInterface = cursor.fetchall()
        con.close()
        return ipInterface

    def select_by_interface_reseau(id_interface_reseau: int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(
            """ SELECT * FROM interface_reseau_route WHERE id_interface_reseau = ? """, (id_interface_reseau))
        interfaceReseau = cursor.fetchall()
        con.close()
        return interfaceReseau
