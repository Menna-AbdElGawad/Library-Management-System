import mysql.connector

books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "is_borrowed": False, "category": "Programming"},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "is_borrowed": False, "category": "Algorithms"},
    {"title": "Design Patterns", "author": "Erich Gamma", "is_borrowed": True, "category": "Software Engineering"},
    {"title": "Database System Concepts", "author": "Abraham Silberschatz", "is_borrowed": False, "category": "Databases"},
    {"title": "Artificial Intelligence", "author": "Stuart Russell", "is_borrowed": True, "category": "AI"}
]


# Step 1 : Connect to MySQL

conn = mysql.connector.connect (
    host = "127.0.0.1" ,
    user = "root",
    password = "Mm.261005",
    database = "LibraryManagementSystem2"
)

# Step 2 : Initialize Cursor

cursor = conn.cursor()

category_map = {}

# Step 3 : Insert data into Category Table

for book in books :
    category = book["category"]

    cursor.execute("insert into Category (category) values(%s)" , 
                   (category,))
    
    conn.commit()
    category_map[category] = cursor.lastrowid

# Step 4 : Insert data into Books

for book in books :
    category_id = category_map[book["category"]]

    cursor.execute(

        """
        insert into Book(title, author, is_borrowed, category_id)
        values (%s, %s, %s, %s)
        """, ((book['title'], book["author"], book['is_borrowed'], 
               category_id)))

    conn.commit()


print("Data is inserted into DB.")

cursor.close()
conn.close()

