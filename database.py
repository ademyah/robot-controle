import sqlite3
from contextlib import closing

def create_connection():
    conn = sqlite3.connect('users.db', timeout=10)  # Ajoutez un timeout pour éviter les deadlocks
    return conn

def create_table():
    with closing(create_connection()) as conn, conn, closing(conn.cursor()) as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                firstname TEXT,
                lastname TEXT,
                email TEXT UNIQUE,
                password TEXT,
                cin TEXT
            )
        ''')
        conn.commit()

def add_user(firstname, lastname, email, password, cin):
    with closing(create_connection()) as conn, conn, closing(conn.cursor()) as cursor:
        cursor.execute('''
            INSERT INTO users (firstname, lastname, email, password, cin)
            VALUES (?, ?, ?, ?, ?)
        ''', (firstname, lastname, email, password, cin))
        conn.commit()

def check_login_credentials(email, password):
    with closing(create_connection()) as conn, conn, closing(conn.cursor()) as cursor:
        cursor.execute('''
            SELECT * FROM users WHERE email = ? AND password = ?
        ''', (email, password))
        user = cursor.fetchone()
    return user is not None