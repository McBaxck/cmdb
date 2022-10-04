from database import Database

class PartitionDatabase():

    def create(self) -> None:
        return
    
    def update(self) -> None:
        return
    
    def delete(self) -> None:
        return

    def selectByLabel(string):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE label = ?""", (value))
        label = cursor.fetchall()
        return label
    
    def selectByEspaceLibreBetween(int, int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE espaceLibre = ?""", (value))
        espaceLibre = cursor.fetchall()
        return espaceLibre

    def selectByEspaceUtiliseBetween(int, int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE espaceUtilise = ?""", (value))
        espaceUtilise = cursor.fetchall()
        return espaceUtilise
    
    def selectByDisqueDur(int):
        db = Database()
        con = db._open()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM partition WHERE disqueDur = ?""", (value))
        disqueDur = cursor.fetchall()
        return disqueDur