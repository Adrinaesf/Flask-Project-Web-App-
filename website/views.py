# We will crete teh first routs, like login page, home-page, 

# First we start with flask:
from flask import Blueprint, render_template
# This has so much routs here, has URL, 

views = Blueprint('views', __name__) # Recc: call the same name

@views.route('/')
def home():
    # This function will run when we go hit the route
    return render_template("home.html")