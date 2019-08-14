# addcountry.py

from flask import Blueprint, jsonify
from . import db
from flask import request
from .models import Country
import json
from . import errorchecker
import os
import logging
import logging.config
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

addcountry = Blueprint('addcountry', __name__)

logger = logging.getLogger('addcountry')

@addcountry.route('/add_country/<countryname>', methods=['POST'])
def add_country(countryname):
    data = json.loads(request.data)
    try:
        country_name = data['country_name']
        capital = data['capital']
        continent = data['continent']
        subregion = data['subregion']
        currency = data['currency']['name']
        type = data['currency']['type']
        population = data['population']

    except:
        return errorchecker.param_mismatch_error()

    if country_name != countryname:
        return errorchecker.invalid_country()

    country = Country.query.filter_by(
        country_name=country_name).first()  # if this returns a country_name, then the country already exists in database

    if country:  # if a country is found, return a data_conflict
        return errorchecker.data_conflict(country_name)

    # create new country data.
    new_country = Country(country_name=country_name, capital=capital, continent=continent, subregion=subregion,
                     currency=currency, type=type, population=population)

    # add the new user to the database
    db.session.add(new_country)
    db.session.commit()
    message = {
        'status' : 201,
        'message' : 'Country Added Successfully'
    }
    resp = jsonify(message)
    resp.status_code = 201
    logger.info('Country: ' + country_name + ' Added Successfully')
    return resp


@addcountry.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return 'Appliation shutting down...'