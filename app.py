from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def first():
    return render_template("Login.html")

@app.route('/signup')
def second():
    return render_template("SignUp.html")

if __name__ == "__main__":
    app.run(host = "localhost",port =5000,debug = True)