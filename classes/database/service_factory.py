from classes.database.database import Database
from dataclasses import dataclass
from classes.database.interfaces.interface_reseau_route_database import InterfaceReseauRouteDatabase
from classes.database.interfaces.ip_table_rules_database import IpTableRulesDatabase
from classes.database.interfaces.interface_reseau_database import InterfaceReseauDatabase
from classes.database.securite_database import SecuriteDatabase
from classes.database.server.server_database import ServerDatabase
from classes.database.stockage.hard_disk_database import DisqueDurDatabase
from classes.database.stockage.partition_database import PartitionDatabase

"""_summary_
    Permet de mettre en oeuvre le design pattern singleton afin d'assurer l'unicité de l'instance des objets suivants définis
    afin d'éviter les collisions durant l'accès à la base de données
"""
@dataclass
class ServiceFactory:
    database: Database = None
    serverDatabase: ServerDatabase = None
    disqueDurDatabase: DisqueDurDatabase = None
    interfaceReseauDatabase: InterfaceReseauDatabase = None
    securiteDatabase: SecuriteDatabase = None
    ipTableRulesDatabase: IpTableRulesDatabase = None
    routeDatabase: InterfaceReseauRouteDatabase = None
    partitionDatabase: PartitionDatabase = None

    @staticmethod
    def getDatabase():
        if database == None:
            database = Database()
        return database

    @staticmethod
    def getServerDatabase():
        if serverDatabase == None:
            serverDatabase = ServerDatabase()
        return serverDatabase

    @staticmethod
    def getDisqueDurDatabase():
        if disqueDurDatabase == None:
            disqueDurDatabase = DisqueDurDatabase()
        return disqueDurDatabase

    @staticmethod
    def getInterfaceReseauDatabase():
        if interfaceReseauDatabase == None:
            interfaceReseauDatabase = InterfaceReseauDatabase()
        return interfaceReseauDatabase

    @staticmethod
    def getSecuriteDatabase():
        if securiteDatabase == None:
            securiteDatabase = SecuriteDatabase()
        return securiteDatabase

    @staticmethod
    def getIpTableRulesDatabase():
        if ipTableRulesDatabase == None:
            ipTableRulesDatabase = IpTableRulesDatabase()
        return ipTableRulesDatabase

    @staticmethod
    def getRouteDatabase():
        if routeDatabase == None:
            routeDatabase = InterfaceReseauRouteDatabase()
        return routeDatabase

    @staticmethod
    def getPartitionDatabase():
        if partitionDatabase == None:
            partitionDatabase = PartitionDatabase()
        return partitionDatabase
