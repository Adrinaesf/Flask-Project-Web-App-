from flask import Blueprint
# This has so much routs here, has URL, 

auth = Blueprint('auth', __name__) # Recc: call the same name

# We now create more routs: login, logout, sign up:
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"