# deleteresource.py

from flask import Blueprint
from . import db
from .models import Country, Citydata
from . import errorchecker, response
import os
import logging
import logging.config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.config.fileConfig(os.path.join(BASE_DIR, 'utils', 'logger.conf'))
deleteresource = Blueprint('deleteresource', __name__)
logger = logging.getLogger('deleteresource')


@deleteresource.route('/delete/<resource>/<resource_name>', methods=['DELETE'])
def delete_resource(resource, resource_name):
    if resource == 'continent':
        country_data = {}
        country_data['total'] = Country.query.filter_by(continent=resource_name).count()
        if country_data['total'] == 0:  # If no countries found in the continent
            logger.warning('No Countries Found For Continent: ' + resource_name)
            return errorchecker.data_not_found(resource, resource_name)

        for country in Country.query.filter_by(continent=resource_name).all():
            country_name = country.country_name
            country_entry = Country.query.filter_by(country_name=country_name).first()
            db.session.delete(country_entry)
            db.session.commit()

        logger.info('Continent: ' + resource_name + ' Deleted Successfully')
        return response.success_message('delete', resource, resource_name)

    elif resource == 'country':
        resource_data = Country.query.filter_by(country_name=resource_name).first()
        if not resource_data:  # if a country not found, return a data_not_found
            logger.error('Country: ' + resource_name + ' Not Found in Database')
            return errorchecker.data_not_found(resource, resource_name)
        db.session.delete(resource_data)
        db.session.commit()
        logger.info('Country: ' + resource_name + ' Deleted Successfully')
        return response.success_message('delete', resource, resource_name)
    elif resource == 'city':
        resource_data = Citydata.query.filter_by(city_name=resource_name).first()
        if not resource_data:  # if a country not found, return a data_not_found
            logger.error('Country: ' + resource_name + ' Not Found in Database')
            return errorchecker.data_not_found(resource, resource_name)
        db.session.delete(resource_data)
        db.session.commit()
        logger.info('City: ' + resource_name + ' Deleted Successfully')
        return response.success_message('delete', resource, resource_name)
