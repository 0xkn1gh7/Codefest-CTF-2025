from flask import Flask, render_template, session, flash, redirect, url_for, request
import sqlite3
from data import init_db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import threading
import time
from crawler import crawl_pages

def start_crawler():
    time.sleep(10)
    while True:
        crawl_pages()
        time.sleep(60)


app = Flask(__name__, static_folder='static/public', static_url_path='')
app.secret_key = 'tQ5GKZAY9gtQ5GKZAY9g'
app.config['SESSION_COOKIE_HTTPONLY'] = False

@app.before_request
def load_session():
    session_id = session.get('session_id')
    if session_id:
        with sqlite3.connect('news_app.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM sessions WHERE session_id = ?', (session_id,))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
            else:
                session.pop('user_id', None)

@app.route('/')
def home():
    if 'user_id' not in session:
        flash('You need to log in first.')
        return redirect(url_for('login'))
    with sqlite3.connect('news_app.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
    return render_template('home.html', articles=articles, session=session)

@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def article(article_id):
    if 'user_id' not in session:
        flash('You need to log in first.')
        return redirect(url_for('login'))
    with sqlite3.connect('news_app.db') as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            if 'user_id' in session:
                comment = request.form['comment']
                cursor.execute('INSERT INTO comments (article_id, user_id, comment) VALUES (?, ?, ?)',
                               (article_id, session['user_id'], comment))
                conn.commit()
            else:
                flash('You need to log in to comment.')
                return redirect(url_for('login'))

        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        article = cursor.fetchone()
        cursor.execute('''SELECT comments.comment, users.username FROM comments 
                          JOIN users ON comments.user_id = users.id 
                          WHERE comments.article_id = ?''', (article_id,))
        comments = cursor.fetchall()
    return render_template('article.html', article=article, comments=comments)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        with sqlite3.connect('news_app.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                flash('Registration successful! Please log in.')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already exists.')
    return render_template('register.html', session=session)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('news_app.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user and check_password_hash(user[2], password):
                session_id = str(uuid.uuid4())
                session['session_id'] = session_id
                cursor.execute('INSERT INTO sessions (session_id, user_id) VALUES (?, ?)', (session_id, user[0]))
                conn.commit()
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password.')
    return render_template('login.html', session=session)

@app.route('/logout')
def logout():
    session_id = session.get('session_id')
    if session_id:
        with sqlite3.connect('news_app.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sessions WHERE session_id = ?', (session_id,))
            conn.commit()
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/secret')
def secret():
    if session['user_id'] != 1:
        flash('You need to be admin to view this.')
        return render_template('secret.html', session=session)
    FLAG = open('/flag.txt', 'r').read().strip()
    return render_template('secret.html', flag=FLAG, session=session)

if __name__ == '__main__':
    init_db()
    threading.Thread(target=start_crawler, daemon=True).start()
    app.run(host = '0.0.0.0', port=5000)
