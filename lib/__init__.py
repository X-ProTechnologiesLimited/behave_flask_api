# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

    db.init_app(app)

    # blueprint for non-auth parts of app
    from .errorchecker import errorchecker as errorchecker_blueprint
    app.register_blueprint(errorchecker_blueprint)

    # blueprint for non-auth parts of app
    from .addcountry import addcountry as addcountry_blueprint
    app.register_blueprint(addcountry_blueprint)

    # blueprint for non-auth parts of app
    from .getcountry import getcountry as getcountry_blueprint
    app.register_blueprint(getcountry_blueprint)

    # blueprint for non-auth parts of app
    from .deletecountry import deletecountry as deletecountry_blueprint
    app.register_blueprint(deletecountry_blueprint)

    # blueprint for non-auth parts of app
    from .updatecountry import updatecountry as updatecountry_blueprint
    app.register_blueprint(updatecountry_blueprint)

    # blueprint for non-auth parts of app
    from .deletecontinent import deletecontinent as deletecontinent_blueprint
    app.register_blueprint(deletecontinent_blueprint)

    # blueprint for non-auth parts of app
    from .searchcountry import searchcountry as searchcountry_blueprint
    app.register_blueprint(searchcountry_blueprint)

    return app