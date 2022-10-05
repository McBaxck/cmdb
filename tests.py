from msilib.schema import RadioButton
import sys
sys.path.append("./")
from classes.server.server import Server
from classes.server.stockage.dd import HardDisk
from classes.server.stockage.partition import Partition
from classes.server.stockage.raid import RAID
from classes.database.stockage.hard_disk_database import DisqueDurDatabase
from classes.database.stockage.partition_database import PartitionDatabase
from classes.database.server.server_database import ServerDatabase

dd_db = DisqueDurDatabase()
partition_db = PartitionDatabase()
serveur_db = ServerDatabase()

dd_recup = dd_db.selectById(1)

raid = RAID.RAID_5
part1 = Partition("sda1",10,15)
dd = HardDisk("Disque Dur 1",10,15,[part1])
serv = Server("serveur 1 ",15,20,"cg","losthost",[dd],[],[],[raid])

