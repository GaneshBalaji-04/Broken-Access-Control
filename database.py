import sqlite3

def new_user(name,username,password,email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT,username TEXT, password TEXT, email TEXT)')
    cursor.execute('INSERT INTO users (name, username, password, email) VALUES (?, ?, ?, ?)', (name, username, password, email))
    conn.commit()

def check_user(username,password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username=? AND password=?", (username, password))
    result=cursor.fetchall()
    if result==[]:
        return False
    else:
        return True