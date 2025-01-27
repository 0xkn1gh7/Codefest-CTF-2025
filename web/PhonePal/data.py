import sqlite3

def init_db():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS users''')
        cursor.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        cursor.execute('''DROP TABLE IF EXISTS balance''')
        cursor.execute('''CREATE TABLE balance (
                            user_id INTEGER PRIMARY KEY NOT NULL,
                            money INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id))''')
        cursor.execute('''DROP TABLE IF EXISTS cash''')
        cursor.execute('''CREATE TABLE cash (
                            user_id INTEGER PRIMARY KEY NOT NULL,
                            money INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id))''')
        cursor.execute('''DROP TABLE IF EXISTS sessions''')
        cursor.execute('''CREATE TABLE sessions (
                            session_id TEXT PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id))''')
        conn.commit()