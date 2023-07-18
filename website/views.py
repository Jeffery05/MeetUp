from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__) # define blueprint for our application

@views.route('/') #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def home():
    return render_template("home.html")