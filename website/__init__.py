# This helps to make the website as a package to import. 




# First thing to do: Create an app with flask:
from flask import Flask
def creat_app():
    # Initialuze app:
    app = Flask(__name__) 
    # Required for the privacy
    app.config['SECRET_KEY'] = 'cahvdhvaoidh lahdvilh'


    ## Regestering the routs: 
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
