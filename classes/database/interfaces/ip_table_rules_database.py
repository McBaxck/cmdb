from classes.database.interfaces.interface_database import IDatabase
from classes.server.config.ip_table_rules import IpTableRules
from database import Database

class IpTableRulesDatabase(IDatabase):

    def create(self, ipTableRules: IpTableRules) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" INSERT INTO IPTable_rules(id_iptable_rules, ip_destination, port, protocole, iptable_policy, id_securite) VALUES (?, ?, ?, ?, ?) """, (self.selectLastId()+1, ipTableRules.ip_destination, ipTableRules.port, ipTableRules.protocol, ipTableRules.idSecurite))
        cursor.execute()
        cursor.close()
        return
    
    def update(self, ipTableRules: IpTableRules) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" UPDATE iptable_rules SET ip_destination = ?, port = ?, protocole = ?, iptable_policy = ?, id_securite = ?) WHERE id_interface_reseau = ?""", (ipTableRules.ip_destination, ipTableRules.port, ipTableRules.protocol, ipTableRules.idSecurite, ipTableRules.id))
        cursor.execute()
        cursor.close()
        return
    
    def delete(self, ipTablesRules: IpTableRules) -> None:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute(""" DELETE FROM iptable_rules WHERE id_iptable_rules = ? """, (ipTablesRules.id))
        cursor.execute()
        cursor.close()
        return

    def selectLastId(self) -> int:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT ipr.id_iptable_rules FROM iptable_rules AS ipr ORDER BY ipr.id_iptable_rules DESC LIMIT 0,1""")
        rs = cursor.fetchone()
        cursor.close()
        return rs

    def selectAll(self):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules""")
        rs = cursor.fetchall()
        cursor.close()
        return rs

    def selectById(id: int) -> IpTableRules:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.id_iptable_rules = ?""", (id))
        rs = cursor.fetchone()
        cursor.close()
        return rs

    def selectByIpDestination(ipDestination: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.ip_destination = ?""", (ipDestination))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectByPort(port: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.port = ?""", (port))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectByProtocole(protocole: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.protocole = ?""", (protocole))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectByPolicy(ipTablePolicy: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.iptable_policy = ?""", (ipTablePolicy))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectByOption(option: str) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.id_iptable_rules IN (
            SELECT ipo.id_iptable_rules FROM iptable_options AS ipo WHERE ipo.id_iptables_rules_option IN (
                SELECT ipro.id_tables_rules_option FROM IPTable_Rules_Option AS ipro WHERE ipro.iptable.option = ?
            )
        )""", (option))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectByOptions(options: list) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.id_iptable_rules IN (
            SELECT ipo.id_iptable_rules FROM iptable_options AS ipo WHERE ipo.id_iptables_rules_option IN (
                SELECT ipro.id_tables_rules_option FROM IPTable_Rules_Option AS ipro WHERE ipro.iptable.option IN ?
            )
        )""", (options))
        rs = cursor.fetchall()
        cursor.close()
        return rs
    
    def selectBySecurite(idSecurite: int) -> list:
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM iptable_rules AS ipr WHERE ipr.id_securite = ?""", (idSecurite))
        rs = cursor.fetchall()
        cursor.close()
        return rs