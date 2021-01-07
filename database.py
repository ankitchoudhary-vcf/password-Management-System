import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT

def create_table():
    connection = sqlite3.connect("passworddata.db")

    connection.execute("CREATE TABLE USERS(WEBSITE TEXT NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT)")
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_table()