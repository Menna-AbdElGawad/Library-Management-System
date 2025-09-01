from database.DBConnection import Connection
from database.Models import Book

class Books(Connection) :
    def __init__(self):
        super().__init__()


    def is_available(self):
        return self.no_of_copies > 0
    
    def is_borrowed(self) :
        if self.no_of_copies > 0:
            self.no_of_copies -= 1
            return True
        return False

    def get_all_books(self):
        self.cursor.execute(
            """
            select b.title, b.isbn, b.language, b.no_copies, b.no_pages, b.released_year, c.category_id 
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
                    Book ID: {book[0]}\n
                    Title: {book[1]}\n
                    ISBN: {book[2]}\n
                    Language: {book[3]}\n
                    Number of Copies: {book[4]}\n
                    Number of Pages: {book[5]}\n
                    Released Year: {book[6]}\n
                    Category ID: {book[7]}\n
                """
            )
