import sqlite3

def get_db_connection():
    conn = sqlite3.connect('shadowfox.db')
    return conn
