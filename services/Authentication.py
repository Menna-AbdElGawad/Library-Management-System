import mysql.connector
from core.Employee import Employee
from core.Customer import Customer

class Authentication :

    def __init__(self):
        
        self.conn = mysql.connector.connect (
            host = "127.0.0.1" ,
            user = "root",
            password = "Mm.261005",
            database = "LibrarySystem"
        )

        self.cursor = self.conn.cursor()
        self.category_map = dict()

    def login(self, username, password) :
        self.cursor.execute(
            """
            select username, password, first_name, last_name, role from User where username = %s and password = %s

            """ , (username, password,)
        )

        is_exist = self.cursor.fetchone()

        if is_exist and is_exist[0] == username and is_exist[1] == password :
            print(f"Logged in {is_exist[2]} {is_exist[3]} Successfully!!")

            if is_exist[4] == 'Employee' :
                emp = Employee()
                emp.employee_menu()
            else :
                customer = Customer()
                customer.customer_menu()
            
        else :
            print("Logging in Failed, Please try again.")

    def close_conn(self) :
        self.cursor.close()
        self.conn.close()