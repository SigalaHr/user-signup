from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def valid_username_password(username):
    valid = False
    if len(username) >= 3 and len(username) <= 20:
        valid = True
        for char in username:
            if char is not " ":
                valid = True
            else:
                valid = False
                break
    else:
        valid = False
    return valid

def password_match(password, verify_password):
    return password == verify_password

def valid_email(email):
    valid = False
    if len(email) >= 3 and len(email) <= 20:
        valid = True
        for char in email:
            if char is not " ":
                valid = True
                if "@" in email and "." in email:
                    valid = True
                else:
                    valid = False
            else:
                valid = False
                break
    else:
        valid = False
    if email == "":
        valid = True
    return valid

@app.route("/")
def index():
    return render_template('signup.html', title="User Signup")

@app.route("/", methods=['POST'])
def validate_everything():
    valid = False
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    password_match_error = ""
    email_error = ""

    if not valid_username_password(username):
        username_error = "Please enter a valid username"
        username = ""
    else:
        username = username
    if not valid_username_password(password):
        password_error = "Please enter a valid password"
        password = ""
    if not password_match(password, verify_password):
        password_match_error = "Passwords do not match"
        verify_password = ""
        password = ""
    else:
        password = ""
        verify_password = ""
    if not valid_email(email):
        email_error = "Please enter a valid email"
        email = ""
    else:
        email = email
    
    if not username_error and not password_error and not password_match_error and not email_error:
        return render_template('welcome.html', title="Welcome!", username=username
        )

    else:
        return render_template('signup.html', title="User Signup",
            username_error=username_error,
            password_error=password_error,
            password_match_error=password_match_error,
            email_error=email_error,
            username=username,
            password=password,
            verify_password=verify_password,
            email=email)

app.run()
