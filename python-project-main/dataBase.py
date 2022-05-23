
import sqlite3


class db:
    def __init__(self,dbName):
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.dbName = dbName
    def closeConnection(self):
        self.conn.commit()
        self.conn.close()
    def execute(self,sqlCommand):
        self.cursor.execute(sqlCommand)
        self.closeConnection()
        self.__init__(self.dbName)

query = db("project.db")
create_doctors = """CREATE TABLE IF NOT EXISTS DOCTORS(username text,password int)"""
query.execute(create_doctors)