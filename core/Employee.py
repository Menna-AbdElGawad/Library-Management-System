import mysql.connector
from database.Models import Employee

class EmployeeFeatures :
    def __init__(self):
        
        self.conn = mysql.connector.connect (
            host = "127.0.0.1" ,
            user = "root",
            password = "Mm.261005",
            database = "LibrarySystem"
        )

        self.cursor = self.conn.cursor()
        self.category_map = dict()

    def add_book(self) :
        title = input(("Please Enter Book Title:"))
        isbn = input(("Please Enter Author:"))
        language = input("Please Enter Language of the book:")
        no_copies = int(input("Please Enter number of copies:"))
        no_pages = int(input("Please Enter number of pages:"))
        released_year = int(input("Please Enter Released Year:"))
        category = input(("Please Enter Category Type:"))

        self.cursor.execute("select category_id from Category where category = %s", (category,))
        result = self.cursor.fetchone()

        if result :
            category_id = result[0]
        else :
            self.cursor.execute("insert into Category (category) values (%s)", (category,))
            self.conn.commit()
            category_id = self.cursor.lastrowid


        self.cursor.execute(
            """
            insert into Book(title, isbn, language, no_copies, no_pages, released_year, category_id)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s))
            """, (title, isbn, language, no_copies, no_pages, released_year, 
                category_id)
        )

        self.conn.commit()

    def remove_book(self):
        title = input(("Please Enter Book Title:"))

        self.cursor.execute("select title from Book where title = %s", (title,))
        book = self.cursor.fetchone()

        if book :
            self.cursor.execute("delete from Book where title = %s", (title,))
            self.conn.commit()
            print("Book is removed Successfully!")

        else :
            print("Book is not Found in the Database.")
            return
        
    # def edit_book(self):

    # def issue_book(self):

    # def book_returns(self):

    def employee_menu(self) :
        print("Employee's Menu:")
        print("================")
        print("1. Add books") # Done
        print("2. Edit books") # Loading
        print("3. Remove books") # Done
        print("4. Issue books to customers") # Loading
        print("5. Handle book returns") # Loading
        print("0. Exit") # Done

        while True :
            choice = int(input("Please Enter your Choice:"))

            if choice == 0:
                print("GoodBye:)")
                break
            elif choice == 1:
                self.add_book()
            # elif choice == 2:   
            #     self.edit_book()
            elif choice == 3:
                self.remove_book()
            # elif choice == 4:
            #     self.issue_book()
            # elif choice == 5:
            #     self.book_returns()
            else:
                print("Invalid Choice, please try again.")

    def close_conn(self) :
        self.cursor.close()
        self.conn.close()