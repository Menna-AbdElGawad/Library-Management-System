class Book :
    def __init__(self, bookId, title, ISBN, no_of_copies, language, no_of_pages, releasedYear, publisher=None, authors=None, category=None):
        self.bookId = bookId
        self.title = title
        self.ISBN = ISBN
        self.no_of_copies = no_of_copies
        self.language = language
        self.no_of_pages = no_of_pages
        self.releasedYear = releasedYear
        self.publisher = publisher      
        self.authors = authors or []    
        self.category = category        


    def __str__(self):
        return f"""Book Title: {self.title}\n
                ISBN: {self.ISBN}\n
                Number of Copies: {self.no_of_copies}\n
                Language: {self.language}\n
                Number of Pages: {self.no_of_pages}\n
                Released Year: {self.releasedYear}
                """


class Branch :
    def __init__(self, branchId, branchName, location):
        self.branchId = branchId
        self.branchName = branchName
        self.location = location

    def __str__(self):
        return f"""Branch Name: {self.branchName}\n
                Location: {self.location}\n
                """

class Category :
    def __init__(self, categoryId, categoryName):
        self.categoryId = categoryId
        self.categoryname = categoryName

    def __str__(self):
        return f"Category Name: {self.categoryname}"

class User :
    def __init__(self, user_id, first_name, last_name, username, password, email, phone_no, role):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.phone_no = phone_no
        self.role = role


class Employee(User) :    
    def __init__(self, user_id, first_name, last_name, username, password, email, phone_no, role, employee_id):
        super().__init__(user_id, first_name, last_name, username, password, email, phone_no, role)
        self.employee_id = employee_id

class Admin(User) :    
    def __init__(self, user_id, first_name, last_name, username, password, email, phone_no, role, admin_id):
        super().__init__(user_id, first_name, last_name, username, password, email, phone_no, role)
        self.admin_id = admin_id

class Customer(User) :
    def __init__(self, user_id, first_name, last_name, username, password, email, phone_no, role, customer_id, address):
        super().__init__(user_id, first_name, last_name, username, password, email, phone_no, role,)
        self.customer_id = customer_id
        self.address = address

class Publisher :
    def __init__(self, publisherId, publisherName):
        self.publisherId = publisherId
        self.publisherName = publisherName

    def __str__(self):
        return f"Publisher Name: {self.publisherName}"


class Author :
    def __init__(self, authorId, authorName):
        self.authorId = authorId
        self.authorName = authorName

    def __str__(self):
        return f"Author Name: {self.authorName}"


class Borrow:
    def __init__(self, issue_id, issue_date, due_date, return_date, status, customer, book):
        self.issue_id = issue_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status
        self.customer = customer   
        self.book = book           
