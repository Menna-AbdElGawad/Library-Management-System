import mysql.connector
from database.Models import Customer

class Customer :
    def __init__(self):
        
        self.conn = mysql.connector.connect (
            host = "127.0.0.1" ,
            user = "root",
            password = "Mm.261005",
            database = "LibrarySystem"
        )

        self.cursor = self.conn.cursor()
        self.category_map = dict()

    def search_book(self) :
        title = input(("Please Enter Book Title:"))

        self.cursor.execute(
                """
                select b.title, b.isbn, b.language, b.no_copies, b.no_pages, b.released_year, c.category_id 
                from Book b
                join Category c
                on b.category_id = c.category_id
                where title = %s
                """ , (title,)
            )

        book = self.cursor.fetchone()

        if book:
            print(
                f"""
                    Title: {book[0]}\n
                    ISBN: {book[1]}\n
                    Language: {book[2]}\n
                    Number of Copies: {book[3]}\n
                    Number of Pages: {book[3]}\n
                    Released Year: {book[3]}\n
                  """
            )
            
            return book
        else :
            print("Book is not Found in the Database.")
            return None
        
    # We need to edit it to the new database
    def borrow_books(self) :
        title = input(("Please Enter Book Title:"))

        self.cursor.execute("select title, is_borrowed from Book where title = %s", (title,))
        borrowed = self.cursor.fetchone()

        if borrowed and borrowed[1] == 0:
            self.cursor.execute("update Book set is_borrowed = %s where title = %s", (True, title,))
            print("Book is borrowed Successfully!")
            self.conn.commit()

        else :
            print("Book is already borrowed or not Found.")
            return None

    # We need to edit it to the new database
    def return_book(self) :
        title = input(("Please Enter Book Title:"))

        self.cursor.execute("select title, is_borrowed from Book where title = %s", (title,))
        borrowed = self.cursor.fetchone()

        if borrowed and borrowed[1] == 1 :
            self.cursor.execute("update Book set is_borrowed = %s where title = %s", (False, title,))
            print("Book is returned Successfully!")
            self.conn.commit()
        else :
            print("Book is not Found.")
            return None
        
    def list_book(self) :
        self.cursor.execute(
            """
            select b.title, b.isbn, b.language, b.no_copies, b.no_pages, b.released_year, c.category_id 
            from Book b
            join Category c
            on b.category_id = c.category_id
            """
        )

        books = self.cursor.fetchall()

        for book in books :
            print(
                f"""
                    ID: {book[0]}\n
                    Title: {book[1]}\n
                    ISBN: {book[2]}\n
                    Language: {book[3]}\n
                    Number of Copies: {book[4]}\n
                    Number of Pages: {book[5]}\n
                    Released Year: {book[6]}\n
                """
            )

    def customer_menu(self) :
        print("Customer's Menu:")
        print("================")
        print("1. Search books") # Done
        print("2. Borrow books") # Loading
        print("3. Return books") # Loading
        print("4. List available books") # Done
        print("0. Exit")

        while True:
            choice = int(input("Please Enter you choice:"))
            
            if choice == 0:
                print("GoodBye:)")
                break
            
            elif choice == 1:
                self.search_book()
            
            elif choice == 2:
                self.borrow_books()

            elif choice == 3:
                self.return_book()

            elif choice == 4:
                self.list_book()

            else:
                print("Invalid choice, please try again.")

    def close_conn(self) :
        self.cursor.close()
        self.conn.close()
        