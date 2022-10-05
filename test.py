from classes.database.interfaces.interface_reseau_database import InterfaceReseauDatabase
from classes.database.interfaces.interface_reseau_route_database import InterfaceReseauRouteDatabase
from classes.server.config.interface_reseau_route import InterfaceReseauRoute

if __name__ == '__main__' :
    print("test")
    db = InterfaceReseauRouteDatabase()
    rs = db.selectAll()
    #print(rs)

    db2 = InterfaceReseauDatabase()
    rs = db.selectAll()
    print(rs)

def createInDb():
    db = InterfaceReseauRouteDatabase()
    irr = InterfaceReseauRoute()
    irr.ipDestination = "127.0.0.1"
    irr.ipInterface = "127.0.0.1"
    irr.masqueReseau = "255.255.255.0"
    irr.ttl = 255
    db.create(irr)