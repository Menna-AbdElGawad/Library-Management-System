import mysql.connector

# Step 1 : Connect to MySQL

conn = mysql.connector.connect (
    host = "127.0.0.1" ,
    user = "root",
    password = "Mm.261005",
    database = "LibrarySystem"
)

# Step 2 : Initialize Cursor

cursor = conn.cursor()

cursor.execute("SELECT * FROM Branch")
for row in cursor.fetchall():
    print(row)

print("Connection Done!")

cursor.close()
conn.close()

