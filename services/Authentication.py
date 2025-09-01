from database.DBConnection import Connection
from core.Employee import EmployeeFeatures
from core.Customer import CustomerFeatures
from core.Admin import AdminFeatures

class Authentication(Connection) :
    def __init__(self):
        super().__init__()      

    def signup(self):
        while True:
            print("\n===== SignUp Menu =====\n")
            print("==========================")
            first_name = input("Please Enter your First name: ")
            last_name = input("Please Enter your Last name: ")
            username = input("Enter your Username: ")
            password = input("Enter your Password (not less than 6 characters): ")
            email = input("Enter your Email in a right format (ex: name@example.com):")
            phone_no = input("Enter Employee's Phone Number (ex: +201234567890): ")
            address = input("Please Enter your Address: ")
            role = "Customer"

            if len(password) <= 6:
                print("Too small password, it must be not less than 6 characters. please try.")
                continue

            if not phone_no.startswith("+201") or len(phone_no) != 13:
                print("Invalid Phone Number, please try again.")
                continue
        
            if not email.endswith("@gmail.com"):
                print("Invalid Email Format, please try with a valid format.")
                continue

            self.cursor.execute("SELECT email FROM User WHERE email = %s", (email,))
            if self.cursor.fetchone():
                print("Email already exists, please try another Email.")
                continue 
            
            self.cursor.execute(
                """
                insert into User (first_name, last_name, username, password, email, phone_no, role)
                values (%s, %s, %s, %s, %s, %s, %s)
                """, (first_name, last_name, username, password, email, phone_no, role,)
            )

            user_id = self.cursor.lastrowid

            self.cursor.execute(
                "INSERT INTO Customer (customer_id) VALUES (%s)", (user_id,)
            )

            self.conn.commit()
            print("\n")
            print(f"{first_name} {last_name} added successfully!!")
            print("\n")

    def login(self) :
        while True:
            print("\n===== Login Menu =====\n")
            username = input("Please Enter your Username (or type 'exit' to quit): ")
            if username.lower() == "exit":
                print("GoodBye!")
                break

            password = input("Please Enter your Password: ")

            self.cursor.execute(
                """
                select user_id, username, password, first_name, last_name, email, phone_no, role 
                from User 
                where lower(username) = lower(%s) and password = %s
                """ , (username, password,)
            )

            is_exist = self.cursor.fetchone()

            if is_exist and is_exist[2] == password:
                print(f"Logged in {is_exist[3]} {is_exist[4]} Successfully!!")

                if is_exist[7] == 'Employee' :
                    self.cursor.execute(
                        "select employee_id from Employee where employee_id = %s",
                        (is_exist[0],)
                    )

                    emp_id = self.cursor.fetchone()
                    emp_id = emp_id[0] if emp_id else None

                    emp = EmployeeFeatures(
                        user_id=is_exist[0],
                        first_name=is_exist[3],
                        last_name=is_exist[4],
                        username=is_exist[1],
                        password=is_exist[2],
                        email=is_exist[5],
                        phone_no=is_exist[6],
                        role=is_exist[7],
                        employee_id=None  
                    )

                    emp.employee_menu()

                elif is_exist[7] == 'Admin':
                    admin = AdminFeatures()
                    admin_id = is_exist[0]   
                    admin.admin_menu(admin_id)
                    
                else :
                    customer = CustomerFeatures()
                    customer_id = is_exist[0]   
                    customer.customer_menu(customer_id)
                
            else :
                print("Logging in Failed, Please try again.")