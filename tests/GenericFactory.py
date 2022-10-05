from xmlrpc.client import Server
from classes.server.config.interface_reseau import InterfaceReseau
from classes.server.config.interface_reseau_route import InterfaceReseauRoute
from classes.server.config.ip_table_rules import IpTableRules
from classes.server.config.policy import Policy
from classes.server.config.route import Route
from classes.server.config.securite import Securite

from classes.server.stockage.dd import HardDisk
from classes.server.stockage.partition import Partition
from classes.server.stockage.raid import RAID

from classes.server.types.phy import PhysicMachine
from classes.server.types.vm import VirtualMachine
from classes.server.server import Server


class GenericFactory:
    def testAll():
        pass
