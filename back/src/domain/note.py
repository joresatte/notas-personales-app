from encodings import search_function
import sqlite3


class Note:
    def __init__(self, id, user_id, title, text, id_cat):
        self.id = id
        self.title = title
        self.text = text
        self.user_id = user_id
        self.id_cat = id_cat

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'user_id': self.user_id,
            'id_cat': self.id_cat
        }


class NotesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists notes (
                id varchar NOT NULL PRIMARY KEY,
                title varchar,
                text varchar,
                user_id varchar,
                id_cat varchar
            )

        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        notes_list = []
        sql = """select * from notes"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        for item in data:
            one_note = Note(
                id=item["id"], title=item["title"], text=item["text"], user_id=item["user_id"], id_cat=item["id_cat"]
            )
            notes_list.append(one_note)

        return notes_list

    def get_by_id(self, note_id):

        sql = """SELECT * FROM notes WHERE id= :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": note_id})

        data = cursor.fetchone()
        one_note = Note(id=data["id"], title=data["title"],
                        text=data["text"], user_id=data["user_id"], id_cat=data["id_cat"])
        return one_note

    def search_by_user_id(self, user_id):

        sql = """SELECT * FROM notes WHERE user_id= :user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})
        data = cursor.fetchall()
        notes = []
        for item in data:
            note = Note(**item)
            notes.append(note)
        return notes

    def insert_data_note(self, note):
        sql = """insert into notes (id, title, text, user_id, id_cat) values (
            :id, :title, :text, :user_id, :id_cat
        ) """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            note.to_dict(),

        )
        conn.commit()

    # metodo save() cambiado de nombre

    def modify_data_note_by_id(self, modified_note):

        sql = """ UPDATE notes
                    SET title = :title, text= :text, user_id = :user_id, id_cat = :id_cat
                    WHERE id = :id; """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, modified_note.to_dict()
        )
        conn.commit()

    def note_deleted_by_id(self, note_deleted):
        sql = """ DELETE FROM notes
                    WHERE notes.id = :id """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": note_deleted}
        )
        conn.commit()
        cursor.close()
