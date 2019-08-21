# models.py

from flask_login import UserMixin
from . import db

class Country(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    country_name = db.Column(db.String(100), unique=True)
    capital = db.Column(db.String(100))
    continent = db.Column(db.String(100))
    subregion = db.Column(db.String(100))
    currency = db.Column(db.String(100))
    type = db.Column(db.String(100))
    population = db.Column(db.Integer)
    country_href = db.Column(db.String(500))
    continent_href = db.Column(db.String(500))