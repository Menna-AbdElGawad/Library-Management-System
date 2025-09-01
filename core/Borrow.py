from database.DBConnection import Connection
from database.Models import Borrow
from datetime import datetime
class BorrowModel(Connection) :
    def __init__(self):
        super().__init__()

    def calculate_fees(self, issue_id, return_date, due_date):
        return_date = datetime.strptime(return_date, "%Y-%m-%d").date()
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

   
        delay_days = (return_date - due_date).days

        if delay_days > 0:
            fees = delay_days * 5
            print(f"You have fees: {fees} EGP.")

            self.cursor.execute(
                """
                update Borrow
                set fees = %s
                where issue_id = %s
                """, (fees, issue_id,)
            )

            self.conn.commit()
            return True
        else:
            print("No fees, returned on time.")
            return False

        
    def get_borrowed_books(self):
        self.cursor.execute(
            """
            select b.issue_date, b.due_date, b.return_date, b.status, c.customer_id, d.book_id
            from Borrow b
            join Customer c
            on b.customer_id = c.customer_id 
            join Book d
            on b.book_id = d.book_id
            """
        )

        borrows = self.cursor.fetchall()

        print("\n===== Borrowed Books =====")
        for borrow in borrows :
            print(
                f"""
                Issue Date: {borrow[0]}
                Due Date: {borrow[1]}
                Return Date: {borrow[2]}
                Status: {borrow[3]}
                Customer ID: {borrow[4]}
                Book ID: {borrow[5]}
                """
            )