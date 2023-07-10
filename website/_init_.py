from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oisfjsdoigjfdgk' # encrypt cookie data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

    #register blueprints in init
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # URL prefix goes in front of whatever is in route
    app.register_blueprint(auth, url_prefix='/')

    return app