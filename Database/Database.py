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

if __name__ == '__main__' :
    conn = create_connection(r'./Db_serveur.db')
    sql_create_table_Serveur = """  CREATE TABLE Serveur(
                                    id_serveur INTEGER,
                                    label TEXT NOT NULL,
                                    hostname TEXT NOT NULL,
                                    type TEXT NOT NULL,
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
                                        policy TEXT NOT NULL,
                                        id_securite INTEGER NOT NULL,
                                        PRIMARY KEY(id_iptable_rules),
                                        FOREIGN KEY(id_securite) REFERENCES Securite(id_securite)
                                        );
                                        """
    sql_create_table_IpTablesRules_Options = """CREATE TABLE IPTable_Rules_Option(
                                                id_iptables_rules_option INTEGER,
                                                option TEXT NOT NULL,
                                                PRIMARY KEY(id_iptables_rules_option)
                                                );
                                                """
    sql_create_table_Route = """CREATE TABLE Route(
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
        create_tables(conn,sql_create_table_Route)
        create_tables(conn,sql_create_table_raid)
        create_tables(conn,sql_create_table_iptable_options)
        create_tables(conn,sql_create_table_serveur_secuite)
        create_tables(conn,sql_create_table_serveur_raid)