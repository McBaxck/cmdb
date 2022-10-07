from msilib.schema import RadioButton
import sys
sys.path.append("./")
from classes.server.server import Server
from classes.server.stockage.dd import HardDisk
from classes.server.stockage.partition import Partition
from classes.server.stockage.raid import RAID
from classes.database.service_factory import ServiceFactory
from classes.server.config.InterfaceReseauRoute import InterfaceReseauRoute


dd_recup = ServiceFactory.getDisqueDurDatabase().selectById(1)

raid = RAID.RAID_5
part1 = Partition("sda1",10,15)
dd = HardDisk("Disque Dur 1",15,15,[part1])
serv = Server("serveur 1 ",15,20,"cg","losthost",[dd],[],[],[raid])
interfaceReseauRoute = InterfaceReseauRoute(1,"192.168.0.1","255.255.255.0","192.168.0.2",1) 

#Test du getter label du disque dur
def test_label_dd():
    assert dd.label == "Disque Dur 1"

#Test du getter unsedMemory du disque dur
def test_unusedMemory():
    assert dd.goUnusedMemory == 15

    @property
    def goUnusedMemory(self) -> int:
        return self._goUnusedMemory


#Test du getter usedMemory du disque dur
def test_goUsedMemory():
    assert dd.goUsedMemory == 15

#Test du getter Partition du disque dur
def test_partitions():
    assert dd.partitions.len() == 0

#Test du selectById de la classe DisqueDur_database dans la base de données
def test_selectById():
    assert (dd_recup.label == "Disque Dur 1" & dd_recup.goUnusedMemory == 15 & dd_recup.goUsedMermory == 15) 

# Test du getter d'ID d'interfaceReseauRoute
def test_id():
    assert interfaceReseauRoute.id_interface_reseau_route == 1

# Test du getter d'Ip destination d'interfaceReseauRoute
def test_ipDestination():
    assert interfaceReseauRoute.ip_destination == "192.168.0.1"

# Test du getter de masque reseau d'interfaceReseauRoute
def test_masqueReseau():
    assert interfaceReseauRoute.masque_reseau == "255.255.255.0"

# Test du getter d'ip interface d'interfaceReseauRoute
def test_ipInterface():
    assert interfaceReseauRoute.ip_interface == "192.168.0.2"

# Test du getter de ttl d'interfaceReseauRoute
def test_ttl():
    assert interfaceReseauRoute.ttl == 1