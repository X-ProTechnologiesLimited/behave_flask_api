# search_country.py

from flask import Blueprint
from .models import Country
from . import errorchecker
from bson.json_util import dumps
import os
import logging
import logging.config
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

searchcountry = Blueprint('searchcountry', __name__)

logger = logging.getLogger('searchcountry')

@searchcountry.route('/search/country/q=<country_name>')
def search_country_names(country_name):
    logger.info('Search Country with Keyword: ' + country_name)
    country_data = {}
    country_data['countries'] = []
    search = "%{}%".format(country_name)
    for country in Country.query.filter(Country.country_name.like(search)).all():
        country_data['countries'].append({
            'name': country.country_name,
            'continent': country.continent
        })

    country_data['total'] = Country.query.filter(Country.country_name.like(search)).count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.data_not_found_string(country_name)

    json_data = dumps(country_data, sort_keys=True, indent=4)
    return json_data


@searchcountry.route('/search/country/qs=<country_name>')
def search_country_names_starting(country_name):
    logger.info('Search Country with Keyword starting: ' + country_name)
    country_data = {}
    country_data['countries'] = []
    search = "{}%".format(country_name)
    for country in Country.query.filter(Country.country_name.like(search)).all():
        country_data['countries'].append({
            'name': country.country_name,
            'continent': country.continent
        })

    country_data['total'] = Country.query.filter(Country.country_name.like(search)).count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.data_not_found_string(country_name)

    json_data = dumps(country_data, sort_keys=True)
    return json_data