import sqlite3
import csv
import random

def init_db():
    with sqlite3.connect('profile.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS users''')
        cursor.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            firstName TEXT NOT NULL,
                            lastName TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            description TEXT NOT NULL,
                            gender TEXT NOT NULL)''')
        conn.commit()
    fill_fake_data()
    
def fill_fake_data():
    with open('static/data/description.txt', 'r') as f:
        description = f.read().strip().split('\n')
    with sqlite3.connect('profile.db') as conn:
        cursor = conn.cursor()
        # Add users
        with open('static/data/users.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor.execute('INSERT INTO users (firstName, lastName, age, description, gender) VALUES (?, ?, ?, ?, ?)',
                               (row[0], row[1], int(row[2]), random.choice(description), row[3]))