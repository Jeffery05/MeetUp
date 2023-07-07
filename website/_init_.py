from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oisfjsdoigjfdgk' # encrypt cookie data

    #register blueprints in init
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # URL prefix goes in front of whatever is in route
    app.register_blueprint(auth, url_prefix='/')

    return app