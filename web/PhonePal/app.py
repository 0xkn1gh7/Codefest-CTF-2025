from flask import Flask, request, session, flash, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import time
import uuid
from data import init_db
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecuresecret'

@app.before_request
def load_session():
    session_id = session.get('session_id')
    if session_id:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM sessions WHERE session_id = ?', (session_id,))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
            else:
                session.pop('user_id', None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        with sqlite3.connect('data.db') as conn:
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
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user and check_password_hash(user[2], password):
                session_id = str(uuid.uuid4())
                session['session_id'] = session_id
                cursor.execute('INSERT INTO sessions (session_id, user_id) VALUES (?, ?)', (session_id, user[0]))
                conn.commit()
                cursor.execute('INSERT INTO balance (user_id, money) VALUES (?, ?)', (user[0], 10000))
                conn.commit()
                cursor.execute('INSERT INTO cash (user_id, money) VALUES (?, ?)', (user[0], 1000))
                conn.commit()
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password.')
    return render_template('login.html', session=session)

@app.route('/logout')
def logout():
    session_id = session.get('session_id')
    if session_id:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sessions WHERE session_id = ?', (session_id,))
            conn.commit()
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/', methods=["GET", "POST"])
def home():
    if 'user_id' not in session:
        flash('You need to log in first.')
        return redirect(url_for('login'))
    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        error = None
        if request.method == 'POST':
            cursor.execute('SELECT money FROM balance WHERE user_id = ?', (session['user_id'],))
            balance = cursor.fetchone()['money']
            amount = int(request.form['amount'])
            if amount <= balance:
                time.sleep(1)
                cursor.execute('SELECT money FROM cash WHERE user_id = ?', (session['user_id'],))
                cash = cursor.fetchone()['money']
                cash += amount
                balance -= amount
                cursor.execute('UPDATE balance SET money = ? WHERE user_id = ?',
                            (balance, session['user_id']))
                cursor.execute('UPDATE cash SET money = ? WHERE user_id = ?',
                            (cash, session['user_id']))
            else:
                error = "Not enough balance!"
            conn.commit()
        cursor.execute('SELECT money FROM balance WHERE user_id = ?', (session['user_id'],))
        balance = cursor.fetchone()['money']
        cursor.execute('SELECT money FROM cash WHERE user_id = ?', (session['user_id'],))
        cash = cursor.fetchone()['money']
        if cash >= 18000:
            FLAG = open('/flag.txt', 'r').read().strip()
            flash(FLAG)
        else:
            flash("Special token is given to members with Wallet Balance of ₹18000 or more")
    return render_template('home.html', balance=balance, cash=cash, session=session, error=error)

if __name__ == "__main__":
    init_db()
    app.run(host = '0.0.0.0', port=5000)
