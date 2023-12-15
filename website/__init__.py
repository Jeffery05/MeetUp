from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oisfjsdoigjfdgk' # encrypt cookie data
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # tells them where to save database
db.init_app(app) 

#register blueprints in init
from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/') # URL prefix goes in front of whatever is in route
app.register_blueprint(auth, url_prefix='/')
"""
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            """

from .models import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))