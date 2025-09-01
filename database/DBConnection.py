import mysql.connector

# Step 1 : Connect to MySQL
class Connection :
    def __init__(self):
        self.conn = mysql.connector.connect (
            host = "127.0.0.1" ,
            user = "root",
            password = "Mm.261005",
            database = "LibrarySystem"
        )

        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn
    
    def get_cursor(self):
        return self.cursor
    
    def close_conn(self):
        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()
