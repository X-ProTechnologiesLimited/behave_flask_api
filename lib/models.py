# models.py

from . import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    country_name = db.Column(db.String(100), unique=True)
    capital = db.Column(db.String(100))
    continent = db.Column(db.String(100))
    subregion = db.Column(db.String(100))
    currency = db.Column(db.String(100))
    code = db.Column(db.String(100))
    population = db.Column(db.Integer)
    order_number = db.Column(db.Integer)


class Citydata(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    city_name = db.Column(db.String(100), unique=True)
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    country = db.Column(db.String(100))
    country_code = db.Column(db.String(100))
    city_population = db.Column(db.Integer)
