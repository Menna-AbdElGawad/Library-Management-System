import mysql.connector
from database.Models import User

class User :
    def __init__(self):
        
        self.conn = mysql.connector.connect (
            host = "127.0.0.1" ,
            user = "root",
            password = "Mm.261005",
            database = "LibrarySystem"
        )

        self.cursor = self.conn.cursor()
        self.category_map = dict()

    def specialize(self) :