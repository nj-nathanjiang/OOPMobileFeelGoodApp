import sqlite3


class DataBase:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS "
            "book ("
            "id INTEGER PRIMARY KEY,"
            " title text,"
            " author text,"
            " year integer,"
            " rating integer"
            ")")
        self.conn.commit()

    def insert(self, title, author, year, rating):
        self.cur.execute(
            "INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
            (title, author, year, rating)
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", rating=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR rating=?",
                         (title, author, year, rating))
        rows = self.cur.fetchall()
        return rows

    def delete(self, arg_id):
        self.cur.execute("DELETE FROM book WHERE id=?", (arg_id,))
        self.conn.commit()

    def update(self, arg_id, title, author, year, rating):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, rating=? WHERE id=?", (title, author, year, rating, arg_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
