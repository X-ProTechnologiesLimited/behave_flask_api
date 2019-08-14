# deletecontinent.py

from flask import Blueprint, jsonify
from . import db
from .models import Country
from . import errorchecker
import os
import logging
import logging.config
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

deletecontinent = Blueprint('deletecontinent', __name__)

logger = logging.getLogger('deletecontinent')

@deletecontinent.route('/delete/continent/<continent>', methods=['DELETE'])
def delete_continent(continent):
    country_data = {}
    country_data['total'] = Country.query.filter_by(continent=continent).count()
    if country_data['total'] == 0:  # If no countries found in the continent
        logger.warning('No Countries Found For Continent: ' + continent)
        return errorchecker.data_not_found_continent(continent)

    for country in Country.query.filter_by(continent=continent).all():
        country_name = country.country_name
        country_entry = Country.query.filter_by(country_name=country_name).first()  # if this returns a country_name, then the country already exists in database
        db.session.delete(country_entry)
        db.session.commit()

    message = {
    'status': 201,
    'message': 'All countries for continent: ' + continent +  ' Deleted Successfully'
    }
    resp = jsonify(message)
    resp.status_code = 201
    logger.info('All countries for Continent: ' + continent + ' Deleted Successfully')
    return resp
