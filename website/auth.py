from flask import Blueprint, render_template, request, flash
# This has so much routs here, has URL, 

auth = Blueprint('auth', __name__) # Recc: call the same name

# We now create more routs: login, logout, sign up:
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
    # Now we wanna check if the information is valid or not:
    if len(email) < 4:
        flash('Email must be greater than 4 characters.', category='error')
    elif len(firstName) < 2:
        flash('First name must be greter than 1 characters.', category='error')
    elif len(password1) != len(password2):
        flash('Passwords don\'t match', category='error')
    elif len(password1) < 7: 
        flash('Password should be at least 7 characters', category='error')
        # The data is right and we can enter it to our database. 
    else: 
        flash('Accounts created!', category='success')


    return render_template("sign_up.html")


