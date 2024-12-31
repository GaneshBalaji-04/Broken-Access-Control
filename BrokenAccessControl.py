from flask import *
import bcrypt
import database

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/submit")
def submit():
    name=request.form['name']
    username=request.form['username']
    salt=bcrypt.gensalt()
    password=bcrypt.hasspw(request.form['password'],salt)
    email=request.form['email']
    database.new_user(name,username,password,email)
    return "<h2>The registration is complete<h2>"
    
