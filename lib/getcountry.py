# getcountry.py

from flask import Blueprint
from .models import Country
from . import errorchecker
from bson.json_util import dumps
import os
import logging
import logging.config
import urllib.parse

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))

getcountry = Blueprint('getcountry', __name__)

logger = logging.getLogger('getcountry')

@getcountry.route('/get_country/<country_name>')
def get_country(country_name):
    country_name_uncoded = urllib.parse.unquote_plus(country_name)
    logger.info('Get Country Request For: ' + country_name_uncoded)
    country_data = {}
    country_data['countries'] = {}
    country_data['countries']['currency'] = {}
    country = Country.query.filter_by(country_name=country_name_uncoded).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name_uncoded + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name_uncoded)


    country_data['countries']['country_name'] = country.country_name
    country_data['countries']['capital'] = country.capital
    country_data['countries']['continent'] = country.continent
    country_data['countries']['subregion'] = country.subregion
    country_data['countries']['currency']['name'] = country.currency
    country_data['countries']['currency']['type'] = country.type
    country_data['countries']['population'] = country.population
    country_data['total'] = Country.query.filter_by(country_name=country_name_uncoded).count()

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_country/continent/<continent>')
def get_country_continent(continent):
    continent_name_uncoded = urllib.parse.unquote_plus(continent)
    logger.info('Get Country Request For Continent: ' + continent_name_uncoded)
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.filter_by(continent=continent_name_uncoded).all():
        country_data['countries'].append({
            'country_name': country.country_name,
            'capital': country.capital,
            'continent': country.continent,
            'subregion': country.subregion,
            'currency': {
                'type': country.currency,
                'name': country.type,
            },
            'population': country.population,
        })

    country_data['total'] = Country.query.filter_by(continent=continent_name_uncoded).count()
    if country_data['total'] == 0: # If no countries found in the continent
        logger.warning('No Countries Found For Continent: ' + continent_name_uncoded)
        return errorchecker.data_not_found_continent(continent_name_uncoded)

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_country/capital/<capital>')
def get_country_capital(capital):
    capital_name_uncoded = urllib.parse.unquote_plus(capital)
    logger.info('Get Country Request For Capital: ' + capital_name_uncoded)
    country_data = {}
    country_data['countries'] = {}
    country_data['countries']['currency'] = {}
    country = Country.query.filter_by(capital=capital_name_uncoded).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country for Capital: ' + capital_name_uncoded + ' Not Found in Database')
        return errorchecker.data_not_found_capital(capital_name_uncoded)


    country_data['countries']['country_name'] = country.country_name
    country_data['countries']['capital'] = country.capital
    country_data['countries']['continent'] = country.continent
    country_data['countries']['subregion'] = country.subregion
    country_data['countries']['currency']['name'] = country.currency
    country_data['countries']['currency']['type'] = country.type
    country_data['countries']['population'] = country.population
    country_data['total'] = Country.query.filter_by(capital=capital_name_uncoded).count()

    json_data = dumps(country_data, sort_keys=True)
    return json_data




@getcountry.route('/get_countries')
def get_countries():
    logger.info('Get All Countries')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.all():
        country_data['countries'].append({
            'country_name': country.country_name,
            'capital': country.capital,
            'continent': country.continent,
            'subregion': country.subregion,
            'currency': {
                'type': country.currency,
                'name': country.type,
            },
            'population': country.population,
        })

    country_data['total'] = Country.query.count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_country/name')
def get_country_names():
    logger.info('Get All Country Names in Database')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.all():
        country_data['countries'].append({
            'name': country.country_name,
            'ref': country.country_href
        })

    country_data['total'] = Country.query.count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_country/continent/<continent>/name')
def get_country_names_continent(continent):
    logger.info('Get All Country Names for a Continent')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.filter_by(continent=continent).all():
        country_data['countries'].append({
            'name': country.country_name,
            'ref': country.country_href
        })

    country_data['total'] = Country.query.filter_by(continent=continent).count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data, sort_keys=True)
    return json_data



@getcountry.route('/get_country/<country_name>/currency')
def get_currency(country_name):
    logger.info('Get Currency Request For: ' + country_name)
    country_data = {}
    country_data['currency'] = {}
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    country_data['currency']['name'] = country.currency
    country_data['currency']['type'] = country.type

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_country/<country_name>/capital')
def get_capital(country_name):
    logger.info('Get Currency Request For: ' + country_name)
    country_data = {}
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    country_data['capital'] = country.capital

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_continent/name')
def get_continent_list():
    logger.info('Get All Continents in the Database')
    country_data = {}
    country_data['continents'] = []
    for country in Country.query.with_entities(Country.continent, Country.continent_href).distinct():
        country_data['continents'].append({
            'name': country.continent,
            'ref': country.continent_href
        })

    country_data['total'] = Country.query.with_entities(Country.continent).distinct().count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Continents Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data, sort_keys=True)
    return json_data