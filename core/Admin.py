from database.DBConnection import Connection
from database.Models import Admin

class AdminFeatures(Connection):
    def __init__(self):
        super().__init__()
    
    def add_emp(self):
        first_name = input("Enter Employee's First Name: ")
        last_name = input("Enter Employee's Last Name: ")
        username = input("Enter Employee's Username: ")
        password = input("Enter Employee's Password (not less than 6 characters): ")
        email = input("Enter Employee's Email in a right format (ex: name@example.com): ")
        phone_no = input("Enter Employee's Phone Number (ex: +201234567890): ")
        role = "Employee"
        
        if not phone_no.startswith("+201") or len(phone_no) != 13:
            print("Invalid Phone Number, please try again.")
            return
        
        if not email.endswith("@gmail.com"):
            print("Invalid Email Format, please try with a valid format.")
            return

        self.cursor.execute("SELECT email FROM User WHERE email = %s", (email,))
        if self.cursor.fetchone():
            print("Email already exists, please try another Email.")
            return 
        
        self.cursor.execute(
            """
            insert into User (first_name, last_name, username, password, email, phone_no, role)
            values (%s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, username, password, email, phone_no, role,)
        )

        user_id = self.cursor.lastrowid

        self.cursor.execute(
            "INSERT INTO Employee (employee_id) VALUES (%s)", (user_id,)
        )

        self.conn.commit()
        print("\n")
        print(f"{first_name} {last_name} added successfully!!")
        print("\n")


    def remove_emp(self):
        first_name = input("Enter Employee's First Name: ")
        last_name = input("Enter Employee's Last Name: ")

        self.cursor.execute(
            """
            select user_id
            from User
            where first_name = %s and last_name = %s and role = 'Employee'
            """, (first_name, last_name,)
        )

        emp = self.cursor.fetchone()

        if emp:
            employee_id = emp[0]
            self.cursor.execute(
                """
                delete from Employee
                where employee_id = %s
                """, (employee_id,)
            )

            self.cursor.execute(
                """
                delete from User
                where user_id = %s
                """, (employee_id,)
            )

            self.conn.commit()
            print("\n")
            print(f"{first_name} {last_name} removed successfully!!")
            print("\n")
        else:
            print("Employee not found.")

    def remove_customer(self):
        first_name = input("Enter Customer's First Name: ")
        last_name = input("Enter Customer's Last Name: ")

        self.cursor.execute(
            """
            select user_id
            from User
            where first_name = %s and last_name = %s and role = 'Customer'
            """, (first_name, last_name,)
        )

        emp = self.cursor.fetchone()

        if emp:
            customer_id = emp[0]
            self.cursor.execute(
                """
                delete from Customer
                where customer_id = %s
                """, (customer_id,)
            )

            self.cursor.execute(
                """
                delete from User
                where user_id = %s
                """, (customer_id,)
            )

            self.conn.commit()
            print("\n")
            print(f"{first_name} {last_name} removed successfully!!")
            print("\n")
        else:
            print("Customer not found.")

    def edit_emp(self):
        emp_id = int(input("Enter Employee ID to edit: "))

        print("\nWhat do you want to edit?")
        print("============================")
        print("1. First Name")
        print("2. Last Name")
        print("3. Username")
        print("4. Password")
        print("5. Email")
        print("6. Phone Number")
        print("0. Cancel")

        choice = int(input("Enter your choice: "))

        fields = {
            1: "first_name",
            2: "last_name",
            3: "username",
            4: "password",
            5: "email",
            6: "phone_no"
        }

        if choice == 0:
            print("Cancelled editing.")
    

        if choice in fields:
            new_value = input(f"Enter new {fields[choice]}: ")
            self.cursor.execute(
                f"update User set {fields[choice]} = %s where user_id = %s and role = 'Employee'",
                (new_value, emp_id)
            )
            self.conn.commit()
            print(f"{fields[choice]} updated successfully!")
        else:
            print("Invalid choice, please try again.")

    def edit_customer(self):
        customer_id = int(input("Enter Customer ID to edit: "))

        print("\nWhat do you want to edit?")
        print("============================")
        print("1. First Name")
        print("2. Last Name")
        print("3. Username")
        print("4. Password")
        print("5. Email")
        print("6. Phone Number")
        print("0. Cancel")

        choice = int(input("Enter your choice: "))

        fields = {
            1: "first_name",
            2: "last_name",
            3: "username",
            4: "password",
            5: "email",
            6: "phone_no"
        }

        if choice == 0:
            print("Cancelled editing.")
            return

        if choice in fields:
            new_value = input(f"Enter new {fields[choice]}: ")
            self.cursor.execute(
                f"update User set {fields[choice]} = %s where user_id = %s and role = 'Cuatomer'",
                (new_value, customer_id)
            )
            self.conn.commit()
            print(f"{fields[choice]} updated successfully!")
        else:
            print("Invalid choice, please try again.")

    def admin_menu(self, admin_id):
        while True:
            print("\n===== Admins' Menu =====")
            print("\n========================")
            print("1. Add Employee")
            print("2. Remove Employee")
            print("3. Remove Customer")
            print("4. Edit Employee")
            print("5. Edit Customer")
            print("0. Exit")

            choice = int(input("Please Enter you choice: "))

            if choice == 0:
                print("GoodBye:)")
                break

            elif choice == 1:
                self.add_emp()

            elif choice == 2:
                self.remove_emp()

            elif choice == 3:
                self.remove_customer()

            elif choice == 4:
                self.edit_emp()

            elif choice == 5:
                self.edit_customer()

            else:
                print("Invalid choice, please try again.")