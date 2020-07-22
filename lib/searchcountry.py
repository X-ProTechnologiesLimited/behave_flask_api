# search_country.py

from flask import Blueprint
from .models import Country
from . import errorchecker
from bson.json_util import dumps
import os
import logging
import logging.config
import urllib.parse
UI_HREF = os.environ['UI_HREF_URL']
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
            'Name': country.country_name,
            'Continent': country.continent
        })

    country_data['Total'] = Country.query.filter(Country.country_name.like(search)).count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.data_not_found_string(country_name)

    json_data = dumps(country_data)
    return json_data


@searchcountry.route('/search/country/qs=<country_name>')
def search_country_names_starting(country_name):
    country_name_uncoded = urllib.parse.unquote_plus(country_name)
    logger.info('Search Country with Keyword starting: ' + country_name_uncoded)
    country_data = {}
    country_data['countries'] = []
    search = "{}%".format(country_name_uncoded)
    for country in Country.query.filter(Country.country_name.like(search)).all():
        country_data['countries'].append({
            'Name' : '<a href="' + UI_HREF + '/ui_view_country_details/'
                     + urllib.parse.quote(country.country_name) + '">' + country.country_name + '</a>',
            'Continent' : '<a href="https://en.wikipedia.org/wiki/'
                                                      + urllib.parse.quote(country.continent)
                                                      + '">' + country.continent + '</a>',
        })

    country_data['Total'] = Country.query.filter(Country.country_name.like(search)).count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.data_not_found_string(country_name)

    json_data = dumps(country_data)
    return json_data