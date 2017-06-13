from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    return render_template('welcome.html', title="Welcome!")

@app.route("/")
def index():
    return render_template('signup.html', title="User Signup")

app.run()
