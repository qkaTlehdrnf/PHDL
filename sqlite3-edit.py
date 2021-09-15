from sqlite3 import Error
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

database = "./database.db"
conn = create_connection(database)
c = conn.cursor()
c.execute('SELECT url_name FROM ph_items')
c.execute('delete from ph_items where new=1')
rows = c.fetchall()

for row in rows:
    print(row)