import sqlite3
from sqlite3 import Error

# Script d'initialisation de la base de données

#Fonction de création de connection à la bdd SQLite
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

#Fonction de création de table dans la bdd
#@params :
#   conn : connecteur à la bdd
#   script_sql : script de la création de la table
def create_tables(conn, script_sql):
    try:
        c = conn.cursor()
        c.execute(script_sql)
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table serveur
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du serveur à ajouter 
def create_server(conn, task):
    try:
        c = conn.cursor()
        sql = '''INSERT INTO Serveur(id_serveur,label,hostname,serveur_type,cpu,gpu)VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table disque_dur
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du disque_dur à ajouter
def create_disque_dur(conn,task):
    try:
        c=conn.cursor()
        sql = '''INSERT INTO Disque_Dur(id_disque_dur,label,espace_libre,espace_utilise,format_disque,id_serveur) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit
    except Error as e:
        print(e)


#Fonctin de création d'un serveur dans la table disque_dur
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du disque_dur à ajouter
def create_partition_dd(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO Partition_DD(id_partition,label,espace_libre,espace_utilise,id_disque_dur) VALUES (?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table interface_reseau
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du interface_reseau à ajouter
def create_interface_reseau(conn,task):
    try:
        c= conn.cursor()
        sql = '''INSERT INTO Interface_Reseau(id_interface_reseau,ip_source,port,ip_passerelle,id_serveur) VALUES (?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table interface_reseau
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du interface_reseau à ajouter
def create_interface_Reseau_Route(conn,task):
    try:
        c=conn.cursor()
        sql='''INSERT INTO Interface_Reseau_Route(id_route,ip_destination,masque_reseau,ip_interface,ttl,id_interface_reseau) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table securite
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du securite à ajouter
def create_securite(conn,task):
    try:
        c= conn.cursor()
        sql='''INSERT INTO Securite(id_securite,ip_firewall) VALUES (?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table serveur_securite
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du serveur_securite à ajouter
def create_serveur_securite(conn,task):
    try:
        c=conn.cursor()
        sql='''INSERT INTO serveur_securite(id_serveur,id_securite) VALUES (?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table iptables_rules
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du iptables_rules à ajouter
def create_iptables_rules(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO IPTable_Rules(id_iptable_rules,ip_destination,port,protocole,iptable_policy,id_securite) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table iptables_rules_option
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du iptables_rules_option à ajouter
def create_iptables_rules_option(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO IPTable_Rules_Option(id_iptables_rules_option,iptable_option) VALUES (?,?)'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table iptable_rules_iptable_rules_option
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du iptable_rules_iptable_rules_option à ajouter
def create_iptable_rules_iptable_rules_option(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO iptable_options(id_iptable_rules,id_iptables_rules_option) VALUES(?,?)'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table create_raid
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du create_raid à ajouter
def create_raid(conn,task):
    try:
        c = conn.cursor()
        sql = '''INSERT INTO RAID(id_raid,label) VALUES (?,?)'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Fonctin de création d'un serveur dans la table serveur_raid
#@params :
#   conn : connecteur à la bdd
#   task:  Valeur des paramètres du serveur_raid à ajouter
def create_serveur_raid(conn,task):
    try:
        c = conn.cursor()
        sql = '''INSERT INTO serveur_raid(id_serveur,id_raid) VALUES (?,?)'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

#Main
if __name__ == '__main__' :
    # Création de la connection à la bdd
    conn = create_connection(r'./Db_serveur.db')


    #Script de création des différentes tables 
    sql_create_table_Serveur = """  CREATE TABLE Serveur(
                                    id_serveur INTEGER,
                                    label TEXT NOT NULL,
                                    hostname TEXT NOT NULL,
                                    serveur_type TEXT NOT NULL,
                                    cpu TEXT NOT NULL,
                                    gpu TEXT NOT NULL,
                                    PRIMARY KEY(id_serveur)
                                );"""
    sql_create_table_dd = """   CREATE TABLE Disque_Dur(
                                id_disque_dur INTEGER,
                                label TEXT NOT NULL,
                                espace_libre INTEGER NOT NULL,
                                espace_utilise INTEGER NOT NULL,
                                format_disque TEXT NOT NULL,
                                id_serveur INTEGER NOT NULL,
                                PRIMARY KEY(id_disque_dur),
                                FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur)
                                );
                        """
    sql_create_table_partition_dd = """CREATE TABLE Partition_DD(
                                        id_partition INTEGER,
                                        label TEXT NOT NULL,
                                        espace_libre INTEGER NOT NULL,
                                        espace_utilise INTEGER NOT NULL,
                                        id_disque_dur INTEGER NOT NULL,
                                        PRIMARY KEY(id_partition),
                                        FOREIGN KEY(id_disque_dur) REFERENCES Disque_Dur(id_disque_dur)
                                        );
                                    """
    sql_create_table_secu = """CREATE TABLE Securite(
                                id_securite INTEGER,
                                ip_firewall TEXT NOT NULL,
                                PRIMARY KEY(id_securite)
                                );
                            """
    sql_create_table_IpTablesRules = """CREATE TABLE IPTable_Rules(
                                        id_iptable_rules INTEGER,
                                        ip_destination TEXT NOT NULL,
                                        port INTEGER NOT NULL,
                                        protocole TEXT NOT NULL,
                                        iptable_policy TEXT NOT NULL,
                                        id_securite INTEGER NOT NULL,
                                        PRIMARY KEY(id_iptable_rules),
                                        FOREIGN KEY(id_securite) REFERENCES Securite(id_securite)
                                        );
                                        """
    sql_create_table_IpTablesRules_Options = """CREATE TABLE IPTable_Rules_Option(
                                                id_iptables_rules_option INTEGER,
                                                iptable_option TEXT NOT NULL,
                                                PRIMARY KEY(id_iptables_rules_option)
                                                );
                                                """
    sql_create_table_interface_reseau="""CREATE TABLE Interface_Reseau(
                                        id_interface_reseau INTEGER,
                                        ip_source TEXT NOT NULL,
                                        port INTEGER NOT NULL,
                                        ip_passerelle TEXT NOT NULL,
                                        id_serveur INTEGER NOT NULL,
                                        PRIMARY KEY(id_interface_reseau),
                                        FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur)
                                        );"""

    sql_create_table_Interface_Reseau_Route = """CREATE TABLE Interface_Reseau_Route(
                                id_route INTEGER,
                                ip_destination TEXT NOT NULL,
                                masque_reseau TEXT NOT NULL,
                                ip_interface TEXT NOT NULL,
                                ttl INTEGER,
                                id_interface_reseau INTEGER NOT NULL,
                                PRIMARY KEY(id_route),
                                FOREIGN KEY(id_interface_reseau) REFERENCES Interface_Reseau(id_interface_reseau)
                                );
                            """
    sql_create_table_raid = """CREATE TABLE RAID(
                                id_raid INTEGER,
                                label TEXT NOT NULL,
                                PRIMARY KEY(id_raid)
                                );
                            """
    sql_create_table_iptable_options= """CREATE TABLE iptable_options(
                                        id_iptable_rules INTEGER,
                                        id_iptables_rules_option INTEGER,
                                        PRIMARY KEY(id_iptable_rules, id_iptables_rules_option),
                                        FOREIGN KEY(id_iptable_rules) REFERENCES IPTable_Rules(id_iptable_rules),
                                        FOREIGN KEY(id_iptables_rules_option) REFERENCES IPTable_Rules_Option(id_iptables_rules_option)
                                        );
                                        """
    sql_create_table_serveur_secuite = """  CREATE TABLE serveur_securite(
                                            id_serveur INTEGER,
                                            id_securite INTEGER,
                                            PRIMARY KEY(id_serveur, id_securite),
                                            FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur),
                                            FOREIGN KEY(id_securite) REFERENCES Securite(id_securite)
                                            );
                                        """
    sql_create_table_serveur_raid = """CREATE TABLE serveur_raid(
                                        id_serveur INTEGER,
                                        id_raid INTEGER,
                                        PRIMARY KEY(id_serveur, id_raid),
                                        FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur),
                                        FOREIGN KEY(id_raid) REFERENCES RAID(id_raid)
                                        );
                                    """

    #Création des tables et des données dans les tables (cf. documentation -> fichier jeu de données)
    if conn is not None:
        create_tables(conn,sql_create_table_Serveur)
        create_tables(conn,sql_create_table_dd)
        create_tables(conn,sql_create_table_partition_dd)
        create_tables(conn,sql_create_table_secu)
        create_tables(conn,sql_create_table_IpTablesRules)
        create_tables(conn,sql_create_table_IpTablesRules_Options)
        create_tables(conn,sql_create_table_interface_reseau)
        create_tables(conn,sql_create_table_Interface_Reseau_Route)
        create_tables(conn,sql_create_table_raid)
        create_tables(conn,sql_create_table_iptable_options)
        create_tables(conn,sql_create_table_serveur_secuite)
        create_tables(conn,sql_create_table_serveur_raid)
        create_server(conn,(1,'serveur1','serveur1.local','VM',16,8))
        create_server(conn,(2,'serveur2','serveur2.local','VM',10,7))
        create_server(conn,(3,'serveur3','serveur3.physique',"Physique",32,25))
        create_disque_dur(conn,(1,'DD1',200,120,'HDD',1))
        create_disque_dur(conn,(2,'DD2',100,400,'SSD',1))
        create_disque_dur(conn,(3,'DD3',400,100,'SSD',2))
        create_disque_dur(conn,(4,'DD4',150,300,'HDD',2))
        create_disque_dur(conn,(5,'DD5',245,120,'SSD',3))
        create_partition_dd(conn,(1,'sda1',100,60,1))
        create_partition_dd(conn,(2,'sda2',100,60,1))
        create_partition_dd(conn,(3,'sda1',70,250,2))
        create_partition_dd(conn,(4,'sda2',30,150,2))
        create_partition_dd(conn,(5,'sda1',25,50,3))
        create_partition_dd(conn,(6,'sda2',150,25,3))
        create_partition_dd(conn,(7,'sda3',125,25,3))
        create_partition_dd(conn,(8,'sda1',50,20,4))
        create_partition_dd(conn,(9,'sda2',75,110,4))
        create_partition_dd(conn,(10,'sda1',75,170,4))
        create_partition_dd(conn,(11,'sda1',245,120,5))
        create_interface_reseau(conn,(1,'192.168.0.1',80,'10.0.0.2',1))
        create_interface_reseau(conn,(2,'192.168.0.2',20,'10.0.0.2',1))
        create_interface_reseau(conn,(3,'192.168.0.3',120,'10.0.0.2',2))
        create_interface_reseau(conn,(4,'192.168.0.4',213,'10.0.0.16',3))
        create_interface_reseau(conn,(5,'192.168.0.5',120,'10.0.0.15',3))
        create_interface_Reseau_Route(conn,(1,'192.168.0.1','255.255.255.0','192.168.0.2',255,1))
        create_interface_Reseau_Route(conn,(2,'192.168.0.1','255.255.255.0','192.168.0.2',120,1))
        create_interface_Reseau_Route(conn,(3,'192.168.0.1','255.255.255.0','192.168.0.2',255,2))
        create_interface_Reseau_Route(conn,(4,'192.168.0.2','255.255.255.0','192.168.0.1',60,2))
        create_interface_Reseau_Route(conn,(5,'192.168.0.2','255.255.255.0','192.168.0.1',60,2))
        create_interface_Reseau_Route(conn,(6,'192.168.0.3','255.255.255.0','192.168.0.3',120,3))
        create_interface_Reseau_Route(conn,(7,'192.168.0.2','255.255.255.0','192.168.0.2',120,3))
        create_interface_Reseau_Route(conn,(8,'192.168.0.2','255.255.255.0','192.168.0.3',255,4))
        create_interface_Reseau_Route(conn,(9,'192.168.0.2','255.255.255.0','192.168.0.1',120,5))
        create_interface_Reseau_Route(conn,(10,'192.168.0.3','255.255.255.0','192.168.0.1',255,5))
        create_securite(conn,(1,'10.0.0.2'))
        create_securite(conn,(2,'192.168.0.7'))
        create_securite(conn,(3,'192.68.25.1'))
        create_securite(conn,(4,'192.168.2.18'))
        create_securite(conn,(5,'192.168.2.17'))
        create_securite(conn,(6,'192.168.2.30'))
        create_securite(conn,(7,'10.0.0.3'))
        create_securite(conn,(8,'10.0.0.4'))
        create_securite(conn,(9,'10.0.0.5'))
        create_serveur_securite(conn,(1,1))
        create_serveur_securite(conn,(1,3))
        create_serveur_securite(conn,(1,4))
        create_serveur_securite(conn,(1,6))
        create_serveur_securite(conn,(1,9))
        create_serveur_securite(conn,(2,2))
        create_serveur_securite(conn,(2,1))
        create_serveur_securite(conn,(2,4))
        create_serveur_securite(conn,(2,5))
        create_serveur_securite(conn,(2,8))
        create_serveur_securite(conn,(2,7))
        create_serveur_securite(conn,(3,2))
        create_serveur_securite(conn,(3,5))
        create_serveur_securite(conn,(3,6))
        create_serveur_securite(conn,(3,9))
        create_serveur_securite(conn,(3,8))
        create_serveur_securite(conn,(3,3))
        create_serveur_securite(conn,(3,1))
        create_iptables_rules(conn,(1,'192.168.0.1',80,'http','DENIED',1))
        create_iptables_rules(conn,(2,'192.168.0.1',20,'tcp','ALLOWED',2))
        create_iptables_rules(conn,(3,'192.168.0.1',3000,'udp','ALLOWED',3))
        create_iptables_rules(conn,(4,'192.168.0.1',120,'udp','DENIED',4))
        create_iptables_rules(conn,(5,'192.168.0.2',80,'http','ALLOWED',5))
        create_iptables_rules(conn,(6,'192.168.0.3',80,'http','ACCEPT',6))
        create_iptables_rules(conn,(7,'192.168.0.3',120,'udp','DENIED',7))
        create_iptables_rules(conn,(8,'192.168.0.3',130,'udp','LOG',8))
        create_iptables_rules(conn,(9,'192.168.0.3',30001,'tcp','ACCEPT',9))
        create_iptables_rules(conn,(10,'192.168.0.3',30002,'tcp','DENIED',2))
        create_iptables_rules(conn,(11,'192.168.0.3',18,'udp','ACCEPT',4))
        create_iptables_rules(conn,(12,'192.168.0.4',120,'http','DROP',6))
        create_iptables_rules(conn,(13,'192.168.0.5',16,'http','DENIED',8))
        create_iptables_rules(conn,(14,'192.168.0.6',152,'udp','LOG',7))
        create_iptables_rules(conn,(15,'192.168.0.6',184,'tcp','ACCEPT',9))
        create_iptables_rules_option(conn,(1,'--'))
        create_iptables_rules_option(conn,(2,'ok'))
        create_iptables_rules_option(conn,(3,'ko'))
        create_iptable_rules_iptable_rules_option(conn,(1,1))
        create_iptable_rules_iptable_rules_option(conn,(1,3))
        create_iptable_rules_iptable_rules_option(conn,(1,2))
        create_iptable_rules_iptable_rules_option(conn,(2,2))
        create_iptable_rules_iptable_rules_option(conn,(2,1))
        create_iptable_rules_iptable_rules_option(conn,(2,3))
        create_iptable_rules_iptable_rules_option(conn,(3,2))
        create_iptable_rules_iptable_rules_option(conn,(3,1))
        create_iptable_rules_iptable_rules_option(conn,(4,1))
        create_iptable_rules_iptable_rules_option(conn,(5,1))
        create_iptable_rules_iptable_rules_option(conn,(6,1))
        create_iptable_rules_iptable_rules_option(conn,(7,1))
        create_iptable_rules_iptable_rules_option(conn,(8,3))
        create_iptable_rules_iptable_rules_option(conn,(9,3))
        create_iptable_rules_iptable_rules_option(conn,(10,3))
        create_iptable_rules_iptable_rules_option(conn,(11,3))
        create_iptable_rules_iptable_rules_option(conn,(12,2))
        create_iptable_rules_iptable_rules_option(conn,(13,2))
        create_iptable_rules_iptable_rules_option(conn,(14,2))
        create_iptable_rules_iptable_rules_option(conn,(15,1))
        create_raid(conn,(1,'RAID-0'))
        create_raid(conn,(2,'RAID-1'))
        create_raid(conn,(3,'RAID-2'))
        create_raid(conn,(4,'RAID-5'))
        create_raid(conn,(5,'RAID-6'))
        create_serveur_raid(conn,(1,1))
        create_serveur_raid(conn,(1,4))
        create_serveur_raid(conn,(1,2))
        create_serveur_raid(conn,(1,5))
        create_serveur_raid(conn,(2,1))
        create_serveur_raid(conn,(2,5))
        create_serveur_raid(conn,(2,4))
        create_serveur_raid(conn,(2,3))
        create_serveur_raid(conn,(3,1))
        create_serveur_raid(conn,(3,2))