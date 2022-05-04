import sqlite3


class Category:
    def __init__(self, id_cat, name):
        self.id_cat = id_cat
        self.name = name

    def to_dict(self):
        return {
            "id_cat": self.id_cat,
            "name": self.name
        }


class CategoryRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists categories (
                id_cat varchar PRIMARY KEY,
                name varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_categories(self):
        sql = """select * from categories"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        categories = [Category(**item) for item in data]

        return categories

    def save(self, category):
        sql = """insert into categories (id_cat, name) values (
            :id_cat, :name
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, category.to_dict())
        conn.commit()
