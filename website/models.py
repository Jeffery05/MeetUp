from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func


user_meetup = db.Table('user_meetup', 
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')), 
                       db.Column('meetup_id', db.Integer, db.ForeignKey('meetup.id')))

# Note: the "User" class is referenced in sql in lowercase (i.e. "user")
           
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key = unique identifier to represent the object
    email = db.Column(db.String(150), unique = True) # no user can have the same email as someone else
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    meetups = db.relationship('Meetup', secondary=user_meetup, backref="user") # tells SQL that whenever we create a note, add the note id into this user's notes relationship (creates a list of all the notes by the user)

# database model: blueprint for how each object will look like
class Meetup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # gets current date and time, store it as date
    date_meetup = db.Column(db.DateTime)
    title = db.Column(db.String(10000))
    location = db.Column(db.String(10000))
    description = db.Column(db.String(10000))
    invitations = db.Column(db.String(10000))
    confirmed = db.Column(db.String(10000))
    declined = db.Column(db.String(10000))
    owner = db.Column(db.Integer)
   