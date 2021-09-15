import sqlite3
database = r"C:\Users\programming\PycharmProjects\PornHub-downloader-python-master\database.db"


def how_many(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM ph_items")
    rows = c.fetchall()
    return len(rows)

print(how_many(database))