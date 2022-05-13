# addresource.py

from flask import Blueprint
from . import db
from flask import request
from .models import Country, Citydata
import json
from . import errorchecker, response
import os
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))
addresource = Blueprint('addresource', __name__)
logger = logging.getLogger('addresource')


@addresource.route('/add_country/<countryname>', methods=['POST'])
def add_country(countryname):
    data = json.loads(request.data)
    try:
        country_name = data['country_name']
        capital = data['capital']
        continent = data['continent']
        subregion = data['subregion']
        currency = data['currency']
        code = data['code']
        population = data['population']
    except KeyError:
        return errorchecker.param_mismatch_error()
    if country_name != countryname:
        return errorchecker.invalid_entry('Country Name')
    country = Country.query.filter_by(
        country_name=country_name).first()
    if country:  # if a country is found, return a data_conflict
        return errorchecker.data_conflict('Country', country_name)
    # create new country data.
    new_country = Country(country_name=country_name, capital=capital,
                          continent=continent, subregion=subregion,
                          currency=currency, code=code,
                          population=population, order_number=0)
    # add the new user to the database
    db.session.add(new_country)
    db.session.commit()
    logger.info('Country: ' + country_name + ' Added Successfully')
    return response.success_message('add', 'Country', countryname)


@addresource.route('/add_city/<cityname>', methods=['POST'])
def add_city(cityname):
    data = json.loads(request.data)
    try:
        city_name = data['city_name']
        latitude = data['latitude']
        longitude = data['longitude']
        country = data['country']
        country_code = data['country_code']
        city_population = data['city_population']
    except KeyError:
        return errorchecker.param_mismatch_error()
    if city_name != cityname:
        return errorchecker.invalid_entry('City Name')
    city = Citydata.query.filter_by(
        city_name=city_name).first()
    if city:  # if a country is found, return a data_conflict
        return errorchecker.data_conflict('City', city_name)
    # create new country data.
    new_city = Citydata(city_name=city_name, latitude=latitude,
                        longitude=longitude, country=country,
                        country_code=country_code, city_population=city_population)
    # add the new user to the database
    db.session.add(new_city)
    db.session.commit()
    logger.info('City: ' + city_name + ' Added Successfully')
    return response.success_message('add', 'city', city_name)
