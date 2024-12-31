from flask import *

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_world():
    return render_template('forms.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    name=request.form['name']
    return render_template('hi.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
