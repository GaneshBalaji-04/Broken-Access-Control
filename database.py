import sqlite3

def new_user(name,username,password,email):
    conn = sqlite3.connect('Broken-Access-Control/databases/databases/users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT,username TEXT, password TEXT, email TEXT)')
    cursor.execute(f'INSERT INTO users VALUES({username},{password})')
    cursor.commit()

def check_user(username,password):
    conn = sqlite3.connect('Broken-Access-Control/databases/databases/users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT username,password FROM users WHERE username={username} and password={password}")
    result=cursor.fetchall()
    if result==[]:
        return False
    else:
        return True