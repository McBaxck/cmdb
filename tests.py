from msilib.schema import RadioButton
import sys
sys.path.append("./")
from classes.server.server import Server
from classes.server.stockage.dd import HardDisk
from classes.server.stockage.partition import Partition
from classes.server.stockage.raid import RAID
from classes.database.service_factory import ServiceFactory


dd_recup = ServiceFactory.getDisqueDurDatabase().selectById(1)

raid = RAID.RAID_5
part1 = Partition("sda1",10,15)
dd = HardDisk("Disque Dur 1",15,15,[part1])
serv = Server("serveur 1 ",15,20,"cg","losthost",[dd],[],[],[raid])

#Test du getter label du disque dur
def test_label_dd():
    assert dd.label == "Disque Dur 1"

#Test du getter unsedMemory du disque dur
def test_unusedMemory():
    assert dd.goUnusedMemory == 15

#Test du getter usedMemory du disque dur
def test_goUsedMemory():
    assert dd.goUsedMemory == 15

#Test du getter Partition du disque dur
def test_partitions():
    assert dd.partitions.len() == 0

#Test du selectById de la classe DisqueDur_database dans la base de données
def test_selectById():
    assert (dd_recup.label == "Disque Dur 1" & dd_recup.goUnusedMemory == 15 & dd_recup.goUsedMermory == 15) 

