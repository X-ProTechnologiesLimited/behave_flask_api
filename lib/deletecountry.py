# deletecountry.py

from flask import Blueprint, jsonify
from . import db
from .models import Country
from . import errorchecker
import os
import logging
import logging.config
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

deletecountry = Blueprint('deletecountry', __name__)

logger = logging.getLogger('deletecountry')

@deletecountry.route('/delete/<country_name>', methods=['DELETE'])
def delete_country(country_name):
    country = Country.query.filter_by(
        country_name=country_name).first()  # if this returns a country_name, then the country already exists in database

    if not country:  # if a country not found, return a data_not_found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    db.session.delete(country)
    db.session.commit()
    message = {
        'status': 201,
        'message': 'Country Deleted Successfully'
    }
    resp = jsonify(message)
    resp.status_code = 201
    logger.info('Country: ' + country_name + ' Deleted Successfully')
    return resp
