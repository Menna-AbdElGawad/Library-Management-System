from database.DBConnection import Connection
from database.Models import Author

class Authors(Connection) :
    def __init__(self):
        super().__init__()

    def get_author(self):
        self.cursor.execute(
            """
            select author_id, author_name
            from Author 
            """
        )

        authors = self.cursor.fetchall()

        print("\n===== Authors' Details =====")

        for author in authors :
            print(
                f"""
                Author ID: {author[0]}\n
                Author Name: {author[1]}\n
                """
            )