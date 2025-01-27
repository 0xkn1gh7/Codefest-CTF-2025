import sqlite3
import csv
from werkzeug.security import generate_password_hash
import random

def init_db():
    with sqlite3.connect('news_app.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS users''')
        cursor.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        cursor.execute('''DROP TABLE IF EXISTS articles''')
        cursor.execute('''CREATE TABLE articles (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL)''')
        cursor.execute('''DROP TABLE IF EXISTS comments''')
        cursor.execute('''CREATE TABLE comments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            article_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            comment TEXT NOT NULL,
                            FOREIGN KEY(article_id) REFERENCES articles(id),
                            FOREIGN KEY(user_id) REFERENCES users(id))''')
        cursor.execute('''DROP TABLE IF EXISTS sessions''')
        cursor.execute('''CREATE TABLE sessions (
                            session_id TEXT PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id))''')
        conn.commit()
    fill_fake_data()
    
def fill_fake_data():
    with sqlite3.connect('news_app.db') as conn:
        cursor = conn.cursor()
        # Add users
        with open('static/data/users.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                               (row[0], generate_password_hash(row[1])))
        # Add articles
        with open('static/data/articles.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor.execute('INSERT INTO articles (title, content) VALUES (?, ?)',
                               (row[0], row[1]))
        # Add comments
        with open('static/data/comments.txt', 'r') as f:
            comments = f.read().strip().split('\n')
            for comment in comments:
                cursor.execute('INSERT INTO comments (article_id, user_id, comment) VALUES (?, ?, ?)',
                               (random.randint(1, 5), random.randint(2, 30), comment))