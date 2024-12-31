from flask import *
import bcrypt
import database

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register",methods=['POST'])
def register():
    return render_template('register.html')

@app.route("/submit",methods=['POST'])
def submit():
    global salt
    name=request.form['name']
    username=request.form['username']
    salt=bcrypt.gensalt()
    password=bcrypt.hashpw(request.form['password'].encode(),salt)
    email=request.form['email']
    database.new_user(name,username,password,email)
    return "<h2>The registration is complete<h2>"

@app.route("/login",methods=['POST'])
def login():
    username=request.form['username']
    password=bcrypt.hashpw(request.form['password'].encode(),salt)
    database.check_user(username,password)
    
if __name__ == "__main__":
    app.run()