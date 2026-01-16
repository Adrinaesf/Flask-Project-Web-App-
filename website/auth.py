from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# This has so much routs here, has URL, 

auth = Blueprint('auth', __name__) # Recc: call the same name

# We now create more routs: login, logout, sign up:
@auth.route('/login', methods=['GET', 'POST'])
def login():
    flash("DEBUG: route loaded", "success")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Filter the users by this email, adn give teh first result:
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('Incorrect password! try again.', category='error')
        else: 
            flash('User does not exist', category='error')



    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    flash("DEBUG: route loaded", "success")
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    

    # Now we wanna check if the information is valid or not:

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greter than 1 characters.', category='error')
        elif len(password1) != len(password2):
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7: 
            flash('Password should be at least 7 characters', category='error')
            # The data is right and we can enter it to our database. 
        else: 
            # Making a user:
            new_user = User(
                email=email,
                firstName=firstName,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()


            flash('Accounts created!', category='success')

            # Now redirect to the home_page
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")


