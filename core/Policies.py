from database.DBConnection import Connection

class Policies(Connection):
    def __init__(self):
        super().__init__()

    def show_policies(self):
        print("\n===== Library Policies =====")
        self.cursor.execute(
            """
            select policy_type, policy_text
            from Policies
            """
        )

        rows = self.cursor.fetchall()

        if rows:
            for row in rows:
                print(f"\n{row[0]} Policy:\n- {row[1]}")
        else:
            print("No Policies found in the system.")

        print("\n==============================\n")