# getcountry.py

from flask import Blueprint
from .models import Country
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

getcountry = Blueprint('getcountry', __name__)

logger = logging.getLogger('getcountry')

def replace_url_to_link(value):
    # Replace url to link
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    # Replace email to mailto
    urls = re.compile(r"([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="mailto:\1">\1</a>', value)
    return value

@getcountry.route('/get_country/<country_name>')
def get_country(country_name):
    country_name_uncoded = urllib.parse.unquote_plus(country_name)
    logger.info('Get Country Request For: ' + country_name_uncoded)
    country_data = {}
    country_data['countries'] = {}
    country = Country.query.filter_by(country_name=country_name_uncoded).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name_uncoded + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name_uncoded)


    country_data['countries']['Name'] = country.country_name
    country_data['countries']['Capital'] = country.capital
    country_data['countries']['Continent'] = country.continent
    country_data['countries']['Subregion'] = country.subregion
    country_data['countries']['Currency'] = country.currency
    country_data['countries']['Code'] = country.code
    country_data['countries']['Population'] = country.population
    country_data['Total'] = Country.query.filter_by(country_name=country_name_uncoded).count()
    previous_order_number = country.order_number
    current_order_number = previous_order_number + 1
    order_update = Country.query.filter_by(country_name=country_name).update(dict(order_number=current_order_number))

    db.session.commit()

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_country/continent/<continent>')
def get_country_continent(continent):
    continent_name_uncoded = urllib.parse.unquote_plus(continent)
    logger.info('Get Country Request For Continent: ' + continent_name_uncoded)
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.filter_by(continent=continent_name_uncoded).order_by(Country.order_number.desc()).all():
        country_data['countries'].append({
            'Name': country.country_name,
            'Capital': country.capital,
            'Continent': country.continent,
            'Subregion': country.subregion,
            'Currency': country.currency,
            'Code': country.code,
            'Population': country.population,
        })

    country_data['Total'] = Country.query.filter_by(continent=continent_name_uncoded).count()
    if country_data['Total'] == 0: # If no countries found in the continent
        logger.warning('No Countries Found For Continent: ' + continent_name_uncoded)
        return errorchecker.data_not_found_continent(continent_name_uncoded)

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_country/capital/<capital>')
def get_country_capital(capital):
    capital_name_uncoded = urllib.parse.unquote_plus(capital)
    logger.info('Get Country Request For Capital: ' + capital_name_uncoded)
    search = "%{}%".format(capital_name_uncoded)
    country_data = {}
    country_data['countries'] = {}
    country = Country.query.filter(Country.capital.like(search)).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country for Capital: ' + capital_name_uncoded + ' Not Found in Database')
        return errorchecker.data_not_found_capital(capital_name_uncoded)


    country_data['countries']['Name'] = country.country_name
    country_data['countries']['Capital'] = country.capital
    country_data['countries']['Continent'] = country.continent
    country_data['countries']['Subregion'] = country.subregion
    country_data['countries']['Currency'] = country.currency
    country_data['countries']['Code'] = country.code
    country_data['countries']['Population'] = country.population
    country_data['Total'] = Country.query.filter_by(capital=country.capital).count()

    json_data = dumps(country_data)
    return json_data




@getcountry.route('/get_countries')
def get_countries():
    logger.info('Get All Countries')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.all():
        country_data['countries'].append({
            'Name': country.country_name,
            'Capital': country.capital,
            'Continent': country.continent,
            'Subregion': country.subregion,
            'Currency': country.currency,
            'Code': country.code,
            'Population': country.population,
        })

    country_data['Total'] = Country.query.count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_country/name')
def get_country_names():
    logger.info('Get All Country Names in Database')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.order_by(Country.order_number.desc()).all():
        country_data['countries'].append({
            'Name': country.country_name,
            'Capital': country.capital
        })

    country_data['Total'] = Country.query.count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_country/resources/all')
def get_country_resources():
    logger.info('Get All Country Resources in Database')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.order_by(Country.order_number.desc()).all():
        country_data['countries'].append({
            'Name' : '<a href="' + UI_HREF + '/ui_view_country_details/' +
                     urllib.parse.quote(country.country_name) +
                     '">' + country.country_name + '</a>',
            'Capital': '<a href="https://en.wikipedia.org/wiki/'
                                                      + urllib.parse.quote(country.capital)
                                                      + '">' + country.capital + '</a>'

        })

    country_data['Total'] = Country.query.count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data, ensure_ascii=False)
    return json_data


@getcountry.route('/get_country/continent/<continent>/name')
def get_country_names_continent(continent):
    logger.info('Get All Country Names for a Continent')
    country_data = {}
    country_data['countries'] = []
    for country in Country.query.filter_by(continent=continent).order_by(Country.order_number.desc()).all():
        country_data['countries'].append({
            'Name': country.country_name,
            'Capital': country.capital
        })

    country_data['Total'] = Country.query.filter_by(continent=continent).count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data

@getcountry.route('/get_members/continent/<continent>')
def get_continent_members(continent):
    logger.info('Get All Country Names for a Continent')
    country_data = {}
    country_data[continent] = []
    for country in Country.query.filter_by(continent=continent).order_by(Country.order_number.desc()).all():
        country_data[continent].append({
            'Name' : '<a href="' + UI_HREF + '/ui_view_country_details/'
                     + urllib.parse.quote(country.country_name) + '">' + country.country_name + '</a>',
            'Capital': '<a href="https://en.wikipedia.org/wiki/'
                                                      + urllib.parse.quote(country.capital)
                                                      + '">' + country.capital + '</a>'
        })

    country_data['Total'] = Country.query.filter_by(continent=continent).count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Countries Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data

@getcountry.route('/get_country/<country_name>/currency')
def get_currency(country_name):
    logger.info('Get Currency Request For: ' + country_name)
    country_data = {}
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    country_data['Currency'] = country.currency

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_country/<country_name>/capital')
def get_capital(country_name):
    logger.info('Get Country Request For: ' + country_name)
    country_data = {}
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:# if a country is not found, return data not found
        logger.error('Country: ' + country_name + ' Not Found in Database')
        return errorchecker.data_not_found_country(country_name)

    country_data['Capital'] = country.capital

    json_data = dumps(country_data, sort_keys=True)
    return json_data


@getcountry.route('/get_continent/name')
def get_continent_list():
    logger.info('Get All Continents in the Database')
    country_data = {}
    country_data['continents'] = []
    for country in Country.query.with_entities(Country.continent).distinct():
        member_countries = Country.query.filter_by(continent=country.continent).count()
        country_data['continents'].append({
            'Name': country.continent,
            'Member_Countries': member_countries
        })

    country_data['Total'] = Country.query.with_entities(Country.continent).distinct().count()

    if country_data['Total'] == 0:  # If no countries found in the continent
        logger.error('No Continents Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data


@getcountry.route('/get_continent/resources')
def get_continent_resources():
    logger.info('Get All Continent Resources in the Database')
    country_data = {}
    country_data['continents'] = []
    for country in Country.query.with_entities(Country.continent).distinct():
        member_countries = Country.query.filter_by(continent=country.continent).count()
        country_data['continents'].append({
            'Continent Name(Click for Wiki Details)': '<a href="https://en.wikipedia.org/wiki/'
                                                      + urllib.parse.quote(country.continent)
                                                      + '">' + country.continent + '</a>',
            'Member_countries' : '<a href="' + UI_HREF + '/ui_view_continent_members/'
                                 + urllib.parse.quote(country.continent) + '">' + str(member_countries) + '</a>'
        })

    country_data['total'] = Country.query.with_entities(Country.continent).distinct().count()

    if country_data['total'] == 0:  # If no countries found in the continent
        logger.error('No Continents Found in Database')
        return errorchecker.no_countries()

    json_data = dumps(country_data)
    return json_data
