# updatecountry.py

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

updatecountry = Blueprint('updatecountry', __name__)

logger = logging.getLogger('updatecountry')

@updatecountry.route('/update/<country_name>/data/<param>', methods=['POST'])
def update_country(country_name, param):
    data = json.loads(request.data)
    try:
        field_value = data[param]
    except:
        logger.error('Json Body Not Correct')
        return errorchecker.param_mismatch_error()
    country = Country.query.filter_by(
        country_name=country_name).first()  # if this returns a country_name, then the country already exists in database

    if not country:  # if a country is not found, return a data_not_found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    # update existing country data.
    if param == 'capital':
        country = Country.query.filter_by(country_name=country_name).update(dict(capital=field_value))
    elif param == 'continent':
        country = Country.query.filter_by(country_name=country_name).update(dict(continent=field_value))
    elif param == 'subregion':
        country = Country.query.filter_by(country_name=country_name).update(dict(subregion=field_value))
    elif param == 'population':
        country = Country.query.filter_by(country_name=country_name).update(dict(population=field_value))
    elif param == 'currency':
        country = Country.query.filter_by(country_name=country_name).update(dict(currency=field_value))
    elif param == 'code':
        country = Country.query.filter_by(country_name=country_name).update(dict(code=field_value))
    else:
        logger.error('Invalid Update Parameter: ' + param + ' Used')
        return errorchecker.int_serv_error_bad_param(param)

    # add the new user to the database
    db.session.commit()
    message = {
        'status' : 201,
        'message' : 'Country Updated Successfully'
    }
    resp = jsonify(message)
    resp.status_code = 201
    logger.info('Country: ' + country_name + ' Updated Successfully')
    return resp

