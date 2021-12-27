import sqlite3


class DataBase:

    def __init__(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS "
            "book ("
            "id INTEGER PRIMARY KEY,"
            " title text,"
            " author text,"
            " year integer,"
            " rating integer"
            ")")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, rating):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
            (title, author, year, rating)
        )
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title="", author="", year="", rating=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR rating=?",
                    (title, author, year, rating))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, arg_id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (arg_id,))
        conn.commit()
        conn.close()

    def update(self, arg_id, title, author, year, rating):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, rating=? WHERE id=?", (title, author, year, rating, arg_id))
        conn.commit()
        conn.close()


database = DataBase()
