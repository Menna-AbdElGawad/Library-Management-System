from database.DBConnection import Connection
from database.Models import Publisher

class Publishers(Connection) :
    def __init__(self):
        super().__init__()

    def get_publisher(self):
        self.cursor.execute(
            """
            select publisher_id, publisher_name
            from Publisher 
            """
        )

        publishers = self.cursor.fetchall()

        print("\n===== Publishers' Details =====")
        for publisher in publishers :
            print(
                f"""
                Publisher ID: {publisher[0]}\n
                Publisher Name: {publisher[1]}\n
                """
            )