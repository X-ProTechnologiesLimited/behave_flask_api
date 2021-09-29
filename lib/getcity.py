# getcity.py

from flask import Blueprint
from .models import Citydata, Country
from . import errorchecker
from . import db
from bson.json_util import dumps
import os
import logging
import logging.config
import urllib.parse
UI_HREF = os.environ['UI_HREF_URL']

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

getcity = Blueprint('getcity', __name__)

logger = logging.getLogger('getcity')

def replace_url_to_link(value):
    # Replace url to link
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    # Replace email to mailto
    urls = re.compile(r"([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="mailto:\1">\1</a>', value)
    return value

@getcity.route('/get_city/<city_name>')
def get_city(city_name):
    city_name_uncoded = urllib.parse.unquote_plus(city_name)
    logger.info('Get City Request For: ' + city_name_uncoded)
    city_data = {}
    city_data['cities'] = {}
    city = Citydata.query.filter_by(city_name=city_name_uncoded).first()
    if not city:# if a country is not found, return data not found
        logger.error('City: ' + city_name_uncoded + ' Not Found in Database')
        return errorchecker.data_not_found_city(city_name_uncoded)

    city_data['cities']['Name'] = '<a href="https://en.wikipedia.org/wiki/'+ urllib.parse.quote(city.city_name)+ '">' + city.city_name + '</a>'
    city_data['cities']['Country'] = city.country
    city_data['cities']['Country_Code'] = city.country_code
    city_data['cities']['Population'] = city.city_population
    city_data['cities']['Latitude'] = city.latitude
    city_data['cities']['Longitude'] = city.longitude
    city_data['Total'] = Citydata.query.filter_by(city_name=city_name_uncoded).count()

    json_data = dumps(city_data)
    return json_data


@getcity.route('/get_members/country/<country_name>')
def get_city_country(country_name):
    country_name_uncoded = urllib.parse.unquote_plus(country_name)
    logger.info('Get List of Cities for Country: ' + country_name_uncoded)
    country_data = Country.query.filter_by(country_name=country_name_uncoded).first()
    if not country_data:
        return errorchecker.data_not_found_country(country_name)

    country_code = country_data.code
    city_data = {}
    city_data['cities'] = []

    for city in Citydata.query.filter_by(country_code=country_code).all():
        city_data['cities'].append({
            'Name': '<a href="https://en.wikipedia.org/wiki/'+ urllib.parse.quote(city.city_name)+ '">' + city.city_name + '</a>',
            'Country': city.country,
            'Country_Code': city.country_code,
            'Population': city.city_population,
            'Latitude': city.latitude,
            'Longitude': city.longitude,
        })

    city_data['Total'] = Citydata.query.filter_by(country_code=country_code).count()
    if city_data['Total'] == 0: # If no countries found in the continent
        logger.warning('No Cities Found For Country: ' + country_name_uncoded)
        return errorchecker.data_not_found_city_country(country_name_uncoded)

    json_data = dumps(city_data)
    return json_data