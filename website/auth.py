from flask import Blueprint, render_template
# This has so much routs here, has URL, 

auth = Blueprint('auth', __name__) # Recc: call the same name

# We now create more routs: login, logout, sign up:
@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("signUp.html")