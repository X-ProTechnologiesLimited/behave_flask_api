# search_country.py

from flask import Blueprint
from .models import Citydata
from . import errorchecker
from bson.json_util import dumps
import os
import logging
import logging.config
import urllib.parse
UI_HREF = os.environ['UI_HREF_URL']
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

searchcity = Blueprint('searchcity', __name__)

logger = logging.getLogger('searchcity')

@searchcity.route('/search/city/q=<city_name>')
def search_city_names(city_name):
    logger.info('Search City with Keyword: ' + city_name)
    city_data = {}
    city_data['cities'] = []
    search = "%{}%".format(city_name)
    for city in Citydata.query.filter(Citydata.city_name.like(search)).all():
        city_data['cities'].append({
            'Name': city.city_name,
            'Country': city.country
        })

    city_data['Total'] = Citydata.query.filter(Citydata.city_name.like(search)).count()

    if city_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Cities Found in Database')
        return errorchecker.data_not_found_city(city_name)

    json_data = dumps(city_data)
    return json_data


@searchcity.route('/search/city/qs=<city_name>')
def search_city_names_starting(city_name):
    city_name_uncoded = urllib.parse.unquote_plus(city_name)
    logger.info('Search City with Keyword starting: ' + city_name_uncoded)
    city_data = {}
    city_data['cities'] = []
    search = "{}%".format(city_name_uncoded)
    for city in Citydata.query.filter(Citydata.city_name.like(search)).all():
        city_data['cities'].append({
            'Name' : '<a href="' + UI_HREF + '/ui_view_city_details/'
                     + urllib.parse.quote(city.city_name) + '">' + city.city_name + '</a>',
            'Country' : '<a href="' + UI_HREF + '/ui_view_country_details/' + urllib.parse.quote(city.country) + '">' + city.country + '</a>',
        })

    city_data['Total'] = Citydata.query.filter(Citydata.city_name.like(search)).count()

    if city_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Cities Found in Database')
        return errorchecker.data_not_found_city(city_name)

    json_data = dumps(city_data)
    return json_data