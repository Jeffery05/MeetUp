from flask import Blueprint, render_template

views = Blueprint('views', __name__) # define blueprint for our application

@views.route('/') #decorator: whenever you go to the / URL, whatever in hom() will run
def home():
    return render_template("home.html")