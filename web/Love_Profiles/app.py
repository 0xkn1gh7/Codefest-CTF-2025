from flask import Flask, render_template, redirect, url_for, request, render_template_string
import sqlite3
from data import init_db
import threading
import time


app = Flask(__name__)
app.secret_key = 'thisissupposedtobesecure'

@app.route('/')
def home():
    with sqlite3.connect('profile.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return render_template('home.html', users=users)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    with sqlite3.connect('profile.db') as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            fName = request.form['fName']
            lName = request.form['lName']
            age = int(request.form['age'])
            description = request.form['description']
            gender = request.form['gender']
            cursor.execute('INSERT INTO users (firstName, lastName, age, description, gender) VALUES (?, ?, ?, ?, ?)',
                            (fName, lName, age, description, gender))
            conn.commit()
            return redirect(url_for('success', name=fName))
    return render_template('profile.html')

@app.route('/success')
def success():
    name = request.args.get('name', 'NAME')
    template = f"<h2>Congratulations {name}! Your profile has been successfully added!</h2> View profiles <a href={url_for('home')}>here</a>"
    return render_template_string(template)

if __name__ == '__main__':
    init_db()
    app.run(host = '0.0.0.0', port=5000)
