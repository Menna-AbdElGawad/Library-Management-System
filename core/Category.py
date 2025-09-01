from database.DBConnection import Connection
from database.Models import Category

class Categories(Connection) :
    def __init__(self):
        super().__init__()

    def get_categories(self):
        self.cursor.execute(
            """
            select category_id, category_name
            from Category
            """
        )

        categories = self.cursor.fetchall()

        print("\n===== Categories =====")

        for categorie in categories:
            print(
                f"""
                Category ID: {categorie[0]}\n
                Category Name: {categorie[1]}\n
                """
            )