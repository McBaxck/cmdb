from database import Database

class RouteDatabase():

    def create(self) -> None:
        return
    
    def update(self) -> None:
        return
    
    def delete(self) -> None:
        return

    def selectByIpDestination(string):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label
    
    def selectByMasqueReseau(string):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label

    def selectByIpPasserelle(string):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label
    
    def selectByIpInterface(string):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label

    def selectByInterfaceReseau(InterfaceReseau):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label