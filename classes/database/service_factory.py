from database import Database
from dataclasses import dataclass


@dataclass
class ServiceFactory:
    database: Database
    serverDatabase: ServerDatabase
    disqueDurDatabase: DisqueDurDatabase
    interfaceReseauDatabase: InterfaceReseauDatabase
    securiteDatabase: SecuriteDatabase
    ipTableRulesDatabase: IpTableRulesDatabase
    routeDatabase: RouteDatabase
    partitionDatabase: PartitionDatabase

    @staticmethod
    def getDatabase():
        if database == null:
            database = Database()
        return database

    @staticmethod
    def getServerDatabase():
        if serverDatabase == null:
            serverDatabase = ServerDatabase()
        return serverDatabase

    @staticmethod
    def getDisqueDurDatabase():
        if disqueDurDatabase == null:
            disqueDurDatabase = DisqueDurDatabase()
        return disqueDurDatabase

    @staticmethod
    def getInterfaceReseauDatabase():
        if interfaceReseauDatabase == null:
            interfaceReseauDatabase = InterfaceReseauDatabase()
        return interfaceReseauDatabase

    @staticmethod
    def getSecuriteDatabase():
        if securiteDatabase == null:
            securiteDatabase = SecuriteDatabase()
        return securiteDatabase

    @staticmethod
    def getIpTableRulesDatabase():
        if ipTableRulesDatabase == null:
            ipTableRulesDatabase = IpTableRulesDatabase()
        return ipTableRulesDatabase

    @staticmethod
    def getRouteDatabase():
        if routeDatabase == null:
            routeDatabase = RouteDatabase()
        return routeDatabase

    @staticmethod
    def getPartitionDatabase():
        if partitionDatabase == null:
            partitionDatabase = PartitionDatabase()
        return partitionDatabase
