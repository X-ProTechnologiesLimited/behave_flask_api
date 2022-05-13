# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # Specifying the database file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    db.init_app(app)

    # blueprint for non-auth parts of app
    from .util import util as util_blueprint
    app.register_blueprint(util_blueprint)

    # blueprint for non-auth parts of app
    from .addresource import addresource as addresource_blueprint
    app.register_blueprint(addresource_blueprint)

    # blueprint for non-auth parts of app
    from .getcountry import getcountry as getcountry_blueprint
    app.register_blueprint(getcountry_blueprint)

    # blueprint for non-auth parts of app
    from .deleteresource import deleteresource as deleteresource_blueprint
    app.register_blueprint(deleteresource_blueprint)

    # blueprint for non-auth parts of app
    from .updatecountry import updatecountry as updatecountry_blueprint
    app.register_blueprint(updatecountry_blueprint)

    # blueprint for non-auth parts of app
    from .searchcountry import searchcountry as searchcountry_blueprint
    app.register_blueprint(searchcountry_blueprint)

    # blueprint for non-auth parts of app
    from .getcity import getcity as getcity_blueprint
    app.register_blueprint(getcity_blueprint)

    # blueprint for non-auth parts of app
    from .searchcity import searchcity as searchcity_blueprint
    app.register_blueprint(searchcity_blueprint)

    return app
