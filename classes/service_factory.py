class ServiceFactory : 
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
            database = new Database()
        return database

    @staticmethod
    def getServerDatabase():
        if serverDatabase == null:
            serverDatabase = new ServerDatabase()
        return serverDatabase

    @staticmethod
    def getDisqueDurDatabase():
        if disqueDurDatabase == null:
            disqueDurDatabase = new DisqueDurDatabase()
        return disqueDurDatabase   

    @staticmethod
    def getInterfaceReseauDatabase():
        if interfaceReseauDatabase == null:
            interfaceReseauDatabase = new InterfaceReseauDatabase()
        return interfaceReseauDatabase
    
    @staticmethod
    def getSecuriteDatabase():
        if securiteDatabase == null:
            securiteDatabase = new SecuriteDatabase()
        return securiteDatabase

    @staticmethod
    def getIpTableRulesDatabase():
        if ipTableRulesDatabase == null:
            ipTableRulesDatabase = new IpTableRulesDatabase()
        return ipTableRulesDatabase

    @staticmethod
    def getRouteDatabase():
        if routeDatabase == null:
            routeDatabase = new RouteDatabase()
        return routeDatabase
    
    @staticmethod
    def getPartitionDatabase():
        if partitionDatabase == null:
            partitionDatabase = new PartitionDatabase()
        return partitionDatabase