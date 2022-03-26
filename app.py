from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['MONGO_DBNAME'] = 'Homework2'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Homework2'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']
    return render_template('Login.html')


@app.route('/login', methods = ['POST'])
def login():
    users = mongo.db.users
    login_users = users.find_one({'name' : request.form['uname']})
    if login_users:
        if request.form['psw'] == login_users['password']:
            session['username'] = request.form['uname']
            return redirect(url_for('index'))
        return render_template('Login.html',error="Invalid Username/Password")
    return render_template('Login.html',error="Invalid Username/Password Combination")

    return render_template("Login.html")

@app.route('/signup', methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            if request.form['psw'] == request.form['cpsw']:
                hashpass = request.form['psw']
                users.insert_one( {'name' : request.form['username'], 'password' : hashpass,
                'FirstName' : request.form['fname'], 'SecondName' : request.form['ffname'],
                'ThirdName' : request.form['tname'], 'Birthday' : request.form['birthday'],
                'FOI' : request.form['field'], 'Gender' : request.form['gender']} )
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            return render_template('SignUp.html',error="Please Enter Same password")
        return render_template('SignUp.html',error="That Username Exists")
    
    return render_template('SignUp.html')

if __name__ == "__main__":
    app.run(host = "localhost",port =5000,debug = True)