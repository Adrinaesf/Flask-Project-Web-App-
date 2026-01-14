"""
Purpose: 
    1. We wnat to store different database models, we make this class:

    2. We crete classes for teh ojects like User, Notes, and more. 

    3. We give the info we want to save for each object. 
        Ex: User: Name, email, ID, ...
        Ex: Note: Text, date, and more
    
    4. How to asccosiate different notes data to different users?ie. what if a user have multiply notes, how should they connect with one another.
        - Main Concept: Foreign Key vs Primary Key
        - Foreign key: A column in your database that  references a column of another database. 
        So in this instance, for every: 
        - single note: store the ID
    
    5. We also want that all users to find all of their notes. 
    This is example of one to many
        - we have one to one
        - we have many to one
        - for more info read ducumentation. 
    Ex: 
    User_table:
        id	        email
        1	        a@x.com

    Note_table: 
        id	        text	    user_id
        5	        "hi"	       1
        6	        "hey"	       1

    User class: 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    Notes class:
    notes = db.relationship('Note') 
    --> This gives all the notes (id = 5,6) to user_id=1

"""


from . import db
## Give objects for flask login:
from flask_login import userMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Length of text <= 10000
    text = db.Column(db.String(10000))

    # store the date + timezone 
    # --> needs the sqlalchemy.sql library
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # -----------------------------------------
    # Connecting the data(Note) and the User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # This user_id, will always save the id of the user
    # Inputs: we need db.Integer + db.ForeignKey('user.field'), which in this case it is the id. 


class User(db.Model, db.UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # email length <= 150 char long + unique 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')









