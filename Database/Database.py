import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_tables(conn, script_sql):
    try:
        c = conn.cursor()
        c.execute(script_sql)
    except Error as e:
        print(e)

def create_server(conn, task):
    try:
        c = conn.cursor()
        sql = '''INSERT INTO Serveur(id_serveur,label,hostname,serveur_type,cpu,gpu)VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_disque_dur(conn,task):
    try:
        c=conn.cursor()
        sql = '''INSERT INTO Disque_Dur(id_disque_dur,label,espace_libre,format_disque,id_serveur) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        c.commit
    except Error as e:
        print(e)

def create_partition_dd(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO Partition_DD(id_partition,label,espace_libre,espace_utilise,id_disque_dur) VALUES (?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_interface_reseau(conn,task):
    try:
        c= conn.cursor()
        sql = '''INSERT INTO Interface_reseau(id_interface_reseau,ip_source,port,ip_passerelle,id_serveur) VALUES (?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_interface_Reseau_Route(conn,task):
    try:
        c=conn.cursor()
        sql='''INSERT INTO Interface_Reseau_Route(id_route,ip_destination,maque_reseau,ip_interface,ttl,id_interface_reseau) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_securite(conn,task):
    try:
        c= conn.cursor()
        sql='''INSERT INTO Securite(id_securite,ip_firewall) VALUES (?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_serveur_securite(conn,task):
    try:
        c=conn.cursor()
        sql='''INSERT INTO serveur_securite(id_serveur,id_securite) VALUES (?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_iptables_rules(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO IPTable_Rules(id_iptable_rules,ip_destination,port,protocole,iptable_policy,id_securite) VALUES (?,?,?,?,?,?);'''
        c.execute(sql,task)
        conn.commit()
    except Error as e:
        print(e)

def create_iptables_rules_option(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO IPTable_Rules_Option(id_iptable_rules_option,iptable_option) VALUES (?,?)'''
        c.execute(conn,task)
        conn.commit()
    except Error as e:
        print(e)

def create_iptable_rules_iptable_rules_option(conn,task):
    try:
        c = conn.cursor()
        sql='''INSERT INTO iptable_options(id_iptable_rules,id_iptable_rules_option) VALUES(?,?)'''
        c.execute(conn,task)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == '__main__' :
    conn = create_connection(r'./Db_serveur.db')
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
                                        id_interface_firewall INTEGER,
                                        ip_source TEXT NOT NULL,
                                        port INTEGER NOT NULL,
                                        ip_passerelle TEXT NOT NULL,
                                        id_serveur INTEGER NOT NULL,
                                        PRIMARY KEY(id_interface_firewall),
                                        FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur)
                                        );"""

    sql_create_table_Interface_Reseau_Route = """CREATE TABLE Interface_Reseau_Route(
                                id_route INTEGER,
                                ip_destination TEXT NOT NULL,
                                masque_reseau TEXT NOT NULL,
                                ip_interface TEXT NOT NULL,
                                ttl INTEGER,
                                id_interface_firewall INTEGER NOT NULL,
                                PRIMARY KEY(id_route),
                                FOREIGN KEY(id_interface_firewall) REFERENCES Interface_Reseau(id_interface_firewall)
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