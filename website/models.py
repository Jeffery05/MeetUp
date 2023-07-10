from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func

# database model: blueprint for how each object will look like
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # gets current date and time, store it as date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key links user to the note

# Note: the "User" class is referenced in sql in lowercase (i.e. "user")
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key = unique identifier to represent the object
    email = db.Column(db.String(150), unique = True) # no user can have the same email as someone else
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # tells SQL that whenever we create a note, add the note id into this user's notes relationship (creates a list of all the notes by the user)
            