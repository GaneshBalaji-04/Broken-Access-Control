from flask import *
import bcrypt
import database


app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register",methods=['POST','GET'])
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
    return render_template('regsuccess.html')

@app.route("/login",methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/performlogin',methods=['POST','GET'])
def login_performed():
    username=request.form['username']
    password=bcrypt.hashpw(request.form['password'].encode(),salt)
    if database.check_user(username,password):
        return """
        <meta http-equiv="refresh" content="5; url=/user">
        <h2>You have been successfully logged in... You are redirected...<h2>
        """
    else:
        return """
        <meta http-equiv="refresh" content="3; url=/login">
        <h2>Your username or password is incorrect..<h2>
        <h2>You are redirected back to login page...</h2>
        """
    
    
if __name__ == "__main__":
    app.run(debug=True)