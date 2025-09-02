from database.DBConnection import Connection
from database.Models import Employee
import sys

class EmployeeFeatures(Connection, Employee) :
    def __init__(self, user_id, first_name, last_name, username, password, email, phone_no, role, employee_id):
        Connection.__init__(self) 
        Employee.__init__(self, user_id, first_name, last_name, username, password, email, phone_no, role, employee_id)
    
    def check_isbn(self, isbn):
        self.cursor.execute(

            """
            select isbn
            from Book
            """
        )

        books = self.cursor.fetchall()

        for book in books:
            if isbn == book[0]:
                print("ISBN is already exists!")
                return
            else:
                if len(isbn) == 10:
                    total = 0
                    for i in range(9):
                        if not isbn[i].isdigit():
                            return False
                        total += (10 - i) * int(isbn[i])

                    check = isbn[9]
                    if check == 'X':
                        total += 10
                    elif check.isdigit():
                        total += int(check)
                    else:
                        return False
                    return total % 11 == 0

                elif len(isbn) == 13:
                    if not isbn.isdigit():
                        return False
                    total = 0
                    for i in range(12):
                        n = int(isbn[i])
                        if i % 2 == 0:
                            total += n
                        else:
                            total += n * 3

                    check_digit = (10 - (total % 10)) % 10
                    return check_digit == int(isbn[12])

                else:
                    return False
        
    def add_book(self) :
        title = input(("Please Enter Book Title: "))
        isbn = input(("Please Enter ISBN: "))

        if not self.check_isbn(isbn):
            print("Invalid ISBN. Book not added.")
            return
    
        language = input("Please Enter Language of the book: ")
        no_copies = int(input("Please Enter number of copies: "))
        no_pages = int(input("Please Enter number of pages: "))
        released_year = int(input("Please Enter Released Year: "))
        category = input(("Please Enter Category Type: "))
        publisher = input(("Please Enter Publisher: "))
        author = input(("Please Enter Author: "))

        self.check_isbn(isbn)

        self.cursor.execute("select category_id from Category where category_name = %s", (category,))
        result = self.cursor.fetchone()

        if result :
            category_id = result[0]
        else :
            self.cursor.execute("insert into Category (category_name) values (%s)", (category,))
            self.conn.commit()
            category_id = self.cursor.lastrowid

        self.cursor.execute("select publisher_id from Publisher where publisher_name = %s", (publisher,))
        result = self.cursor.fetchone()

        if result :
            publisher_id = result[0]
        else :
            self.cursor.execute("insert into Publisher (publisher_name) values (%s)", (publisher,))
            self.conn.commit()
            publisher_id = self.cursor.lastrowid

        self.cursor.execute("select author_id from Author where author_name = %s", (author,))
        result = self.cursor.fetchone()

        if result :
            author_id = result[0]
        else :
            self.cursor.execute("insert into Author (author_name) values (%s)", (author,))
            self.conn.commit()
            author_id = self.cursor.lastrowid


        self.cursor.execute(
            """
            insert into Book(title, isbn, language, no_of_copies, no_of_pages, released_year, category_id, author_id, publisher_id)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (title, isbn, language, no_copies, no_pages, released_year, 
                category_id, author_id, publisher_id,)
        )
        
        book_id = self.cursor.lastrowid
        self.cursor.execute(
            "insert into BookAuthor (book_id, author_id) values (%s, %s)",
            (book_id, author_id)
        )

        self.conn.commit()
        print(f"Book {title} added Successfully!")

    def remove_book(self):
        title = input(("Please Enter Book Title: "))
        try:
            self.cursor.execute(
                """
                delete from BookAuthor
                where book_id = (
                    select book_id 
                    from Book
                    where title = %s
                )
                """ , (title,)
            )

            self.cursor.execute("select title from Book where title = %s", (title,)) 
            book = self.cursor.fetchone()

            if book :
                self.cursor.execute("delete from Book where title = %s", (title,))
                self.conn.commit()
                print("Book is removed Successfully!")

            else :
                print("Book is not Found in the Database.")
                return
            
        except Exception as e:
            print(f"Error while removing book {title}: ", e)
        
    def edit_book(self):
        while True:
            self.edit_menu()

            choice = int(input("Please Enter your choice: "))

            if choice == 0:
                print("Transfering you to the Main Page.")
                self.employee_menu()
                print("\n")
                break

            elif choice == 1:
                self.update_book_field("title", "Book Title")

            elif choice == 2:
                self.update_book_field("no_of_copies", "Number of Copies")

            elif choice == 3:
                self.update_book_field("language", "Language")

            elif choice == 4:
                self.update_book_field("no_of_pages", "Number of Pages")

            elif choice == 5:
                self.update_book_field("released_year", "Released Year")

            elif choice == 6:
                title = input("Please Enter the Book Title: ")
                self.update_publisher(title)

            elif choice == 7:
                title = input("Please Enter the Book Title: ")
                self.update_author(title)

            elif choice == 8:
                title = input("Please Enter the Book Title: ")
                self.update_category(title)

            else:
                print("Invalid Choice, please try again.\n")


    def update_book_field(self, field_name, field_label, table="Book"):
      
        title = input("Please Enter the Book Title: ")

        self.cursor.execute(
            f"SELECT title, {field_name} FROM {table} WHERE title = %s",
            (title,)
        )
        book = self.cursor.fetchone()

        if book:
            old_value = book[1]
            new_value = input(f"Please Enter the New {field_label}: ")

            self.cursor.execute(
                f"UPDATE {table} SET {field_name} = %s WHERE title = %s",
                (new_value, title)
            )
            self.conn.commit()

            print(f"{field_label} Updated successfully from {old_value} to {new_value}.\n")
        else:
            print("Book not found!\n")

    def update_publisher(self, title):
        new_publisher = input("Please Enter the new Publisher name: ")

        self.cursor.execute(
            """
            select publisher_id
            from Publisher
            where publisher_name = %s
            """, (new_publisher,)
        )

        result = self.cursor.fetchone()

        if result:
            publisher_id = result[0]
        else:
            self.cursor.execute(
                """
                insert into Publisher (publisher_name) 
                values (%s)
                """, (new_publisher,)
            )
            
            self.conn.commit()
            publisher_id = self.cursor.lastrowid

        self.cursor.execute(
            """
            update Book 
            set publisher_id = %s
            where title = %s
            """, (publisher_id, title,)
        )

        self.conn.commit()
        print(f"Publisher updated successfully for {title} → {new_publisher}")

    def update_author(self, title):
        new_author = input("Please Enter the new Author name: ")

        self.cursor.execute(
            """
            select author_id
            from Author
            where author_name = %s
            """, (new_author,)
        )

        result = self.cursor.fetchone()

        if result:
            author_id = result[0]
        else:
            self.cursor.execute(
                """
                insert into Author (author_name) 
                values (%s)
                """, (new_author,)
            )
            
            self.conn.commit()
            author_id = self.cursor.lastrowid

        self.cursor.execute(
            """
            update Book 
            set author_id = %s
            where title = %s
            """, (author_id, title,)
        )

        self.conn.commit()
        print(f"Author updated successfully for {title} → {new_author}")

    def update_category(self, title):
        new_category = input("Please Enter the new Category name: ")

        self.cursor.execute(
            """
            select category_id
            from Category
            where category_name = %s
            """, (new_category,)
        )

        result = self.cursor.fetchone()

        if result:
            category_id = result[0]
        else:
            self.cursor.execute(
                """
                insert into Category (category_name) 
                values (%s)
                """, (new_category,)
            )
            
            self.conn.commit()
            category_id = self.cursor.lastrowid

        self.cursor.execute(
            """
            update Book
            set category_id = %s
            where title = %s
            """, (category_id, title,)
        )

        self.conn.commit()
        print(f"Category updated successfully for {title} → {new_category}")

    def edit_menu(self) :
        print("What do you want to edit?")
        print("=========================")
        print("1. Book Title")
        print("2. Number of Copies")
        print("3. Language")
        print("4. Number of Pages")
        print("5. Released Year")
        print("6. Publisher")
        print("7. Author")
        print("8. Category")
        print("0. Return to Main Menu")
        print("=========================\n")

    def employee_menu(self) :
        while True :
            print("\n===== Employees' Menu =====")
            print("=============================")
            print("1. Add books") 
            print("2. Edit books") 
            print("3. Remove books") 
            print("0. Exit") 
            print("=============================\n")

            choice = int(input("Please Enter your Choice: "))

            if choice == 0:
                print("GoodBye:)")
                sys.exit()           
            elif choice == 1:
                self.add_book()
            elif choice == 2:   
                self.edit_book()
            elif choice == 3:
                self.remove_book()
            else:
                print("Invalid Choice, please try again.")

    def close_conn(self) :
        self.cursor.close()
        self.conn.close()