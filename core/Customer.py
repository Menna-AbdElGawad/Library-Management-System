from database.DBConnection import Connection
from core.Borrow import BorrowModel
from datetime import datetime
import sys

class CustomerFeatures(Connection) :
    def __init__(self):
        super().__init__()

    def search_book(self) :
        title = input(("Please Enter Book Title:"))

        self.cursor.execute(
                """
                select b.book_id, b.title, b.isbn, b.language, b.no_of_copies, b.no_of_pages, b.released_year, c.category_id 
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
            Book ID: {book[0]}\n
            Title: {book[1]}\n
            ISBN: {book[2]}\n
            Language: {book[3]}\n
            Number of Copies: {book[4]}\n
            Number of Pages: {book[5]}\n
            Released Year: {book[6]}\n
            """
            )
            
            return book
        else :
            print("Book is not Found in the Database.")
            return None
        
    def borrow_books(self, customer_id) :
        title = input(("Please Enter Book Title:"))
        issue_date = input("Please Enter issue date (YYYY-MM-DD): ")
        due_date = input("Please Enter due date (YYYY-MM-DD): ")

        self.cursor.execute(
            """
            select book_id, title, no_of_copies 
            from Book 
            where title = %s
            """, (title,)
        )

        book = self.cursor.fetchone()

        if book and book[2] > 0:
            book_id = book[0]

            self.cursor.execute(
                """
                update Book 
                set no_of_copies = no_of_copies - 1 
                where book_id = %s
                """, (book_id,)
            )

            self.cursor.execute(
                """
                insert into Borrow (customer_id, book_id, issue_date, due_date)
                values (%s, %s, %s, %s)
                """, (customer_id, book_id, issue_date, due_date,)
            )

            self.conn.commit()
            print("Book is borrowed Successfully!")

        else :
            print("Book not available or out of stock.")
            return None

    def return_book(self, customer_id):
        title = input("Please Enter Book Title: ")
        return_date = input("Please Enter return date (YYYY-MM-DD): ")
        return_date = datetime.strptime(return_date, "%Y-%m-%d").date()

        self.cursor.execute(
            """
            select b.book_id, br.due_date, br.issued_id
            from Book b
            join Borrow br
            on b.book_id = br.book_id 
            where br.customer_id = %s and b.title = %s and br.return_date is null
            """, (customer_id, title,)
        )

        borrowed = self.cursor.fetchone()

        if borrowed:
            book_id, due_date, issue_id = borrowed
            due_date = datetime.strptime(str(due_date), "%Y-%m-%d").date()

            self.cursor.execute(
                """
                update Borrow 
                set return_date = %s, status = 'Returned'
                where issued_id = %s
                """, (return_date, issue_id,)
            )

            self.cursor.execute(
                """
                update Book
                set no_of_copies = no_of_copies + 1
                where book_id = %s
                """, (book_id,)
            )

            if return_date > due_date:
                BorrowModel().calculate_fees(issue_id, return_date, due_date)

            self.conn.commit()
            print("Book is returned Successfully!")

        else:
            print("No active borrow record found for this book.")

        
    def list_book(self) :
        self.cursor.execute(
            """
            select b.book_id, b.title, b.isbn, b.language, b.no_of_copies, b.no_of_pages, b.released_year, c.category_id 
            from Book b
            join Category c
            on b.category_id = c.category_id
            """
        )

        books = self.cursor.fetchall()

        print("\n===== Books' Details =====")
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
            print("===================================================")

    def customer_menu(self, customer_id) :
        while True:
            print("\n===== Customer's Menu =====")
            print("================")
            print("1. Search books") 
            print("2. Borrow books") 
            print("3. Return books") 
            print("4. List available books") 
            print("0. Exit")

            choice = int(input("Please Enter you choice:"))
            
            if choice == 0:
                print("GoodBye:)")
                sys.exit()
            
            elif choice == 1:
                self.search_book()
            
            elif choice == 2:
                self.borrow_books(customer_id)

            elif choice == 3:
                self.return_book(customer_id)

            elif choice == 4:
                self.list_book()

            else:
                print("Invalid choice, please try again.")