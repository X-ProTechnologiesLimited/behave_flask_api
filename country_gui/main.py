# main.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import jsonify, send_from_directory
import json
from json2html import *
from bson.json_util import dumps
import requests
from .nocache import nocache
import os
from . import response
import urllib.parse

api_host = os.environ['COUNTRY_API_HOST']
api_port = os.environ['COUNTRY_API_PORT']
api_url = f'http://{api_host}:{api_port}'
main = Blueprint('main', __name__)
UPLOAD_DIRECTORY = 'templates'


@main.route("/files/<path:path>")
@nocache
def get_file(path):
    """Download a supporing file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@main.route('/')
@nocache
def index():
    return render_template('index.html')


@main.route('/ui_add_country', methods=['GET', 'POST'])
@nocache
def ui_add_country():
    if request.method == 'POST':
        new_country_add_body = {}
        new_country_add_body['currency'] = {}
        url = f"{api_url}/add_country/{request.form.get('Country')}"
        new_country_add_body['country_name'] = request.form.get('Country')
        new_country_add_body['capital'] = request.form.get('Capital')
        new_country_add_body['continent'] = request.form.get('Continent')
        new_country_add_body['subregion'] = request.form.get('Subregion')
        new_country_add_body['currency'] = request.form.get('Currency')
        new_country_add_body['code'] = request.form.get('Code')
        new_country_add_body['population'] = \
            int(request.form.get('Population'))
        new_country_add_request_body = json.dumps(new_country_add_body)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_new_country = requests.post(url=url, data=new_country_add_request_body, headers=headers)

        if response_new_country.status_code == 409:
            return render_template('error_409_conflict.html')
        else:
            data_new_country = response_new_country.json()
            json_data = dumps(data_new_country)
            return response.asset_retrieve(json_data)
    return render_template('add_new_country.html')


@main.route('/ui_add_city', methods=['GET', 'POST'])
@nocache
def ui_add_city():
    if request.method == 'POST':
        new_city_add_body = {}
        url = f"{api_url}/add_city/{request.form.get('City')}"
        new_city_add_body['city_name'] = request.form.get('City')
        new_city_add_body['latitude'] = request.form.get('Latitude')
        new_city_add_body['longitude'] = request.form.get('Longitude')
        new_city_add_body['country'] = request.form.get('Country')
        new_city_add_body['country_code'] = request.form.get('Country_Code')
        new_city_add_body['city_population'] = \
            int(request.form.get('Population'))
        new_city_add_request_body = json.dumps(new_city_add_body)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_new_city = requests.post(url=url, data=new_city_add_request_body, headers=headers)

        if response_new_city.status_code == 409:
            return render_template('error_409_conflict.html')
        else:
            data_new_city = response_new_city.json()
            json_data = dumps(data_new_city)
            return response.asset_retrieve(json_data)
    return render_template('add_new_city.html')

@main.route('/ui_view_<resource>_details/<resource_name>')
@nocache
def ui_view_resource_details(resource, resource_name):
    url = f'{api_url}/get_{resource}/{resource_name}'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    if response_list.status_code == 404:
        return render_template('error_404.html')
    else:
        data_list = response_list.json()
        json_data = dumps(data_list)

        return response.asset_retrieve_details(json_data, resource_name)


@main.route('/ui_view_<resource_name>_resources')
def ui_view_all_resource(resource_name):
    url = f'{api_url}/get_{resource_name}/resources/all'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_search_<resource>', methods=['GET', 'POST'])
def ui_search(resource):
    if request.method == 'POST':
        if resource == 'capital':
            url = f"{api_url}/get_country/capital/{request.form.get('Keyword')}"
        else:
            url = f"{api_url}/search/{resource}/qs={request.form.get('Keyword')}"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_list = requests.get(url=url, headers=headers)
        if response_list.status_code == 404:
            return render_template('error_404.html')
        else:
            data_list = response_list.json()
            json_data = dumps(data_list)
            return response.asset_retrieve(json_data)
    return render_template('resource_template.html', title=f'Search {resource}', action=f'/ui_search_{resource}')


@main.route('/ui_view_specific_<resource>', methods=['GET', 'POST'])
def ui_view_specific(resource):
    if request.method == 'POST':
        url = f"{api_url}/get_{resource}/{request.form.get('Keyword')}"
        resource_name_uncoded = urllib.parse.unquote_plus(request.form.get('Keyword'))
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_list = requests.get(url=url, headers=headers)
        if response_list.status_code == 404:
            return render_template('error_404.html')
        else:
            data_list = response_list.json()
            json_data = dumps(data_list)
            return response.asset_retrieve_details(json_data, resource_name_uncoded)
    return render_template('resource_template.html', title=f'View {resource}', action=f'/ui_view_specific_{resource}')



@main.route('/ui_view_member_<resource>/<resource_name>')
def ui_view_member(resource, resource_name):
    url = f"{api_url}/get_members/{resource}/{resource_name}"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    if response_list.status_code == 404:
        return render_template('error_404.html')
    else:
        data_list = response_list.json()
        json_data = dumps(data_list)

        return response.asset_retrieve_details(json_data, resource_name)

@main.route('/ui_delete_<resource_name>', methods=['GET', 'POST'])
def ui_delete_resource(resource_name):
    if request.method == 'POST':
        url = f"{api_url}/delete/{resource_name}/{request.form.get('Keyword')}"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_list = requests.delete(url=url, headers=headers)
        if response_list.status_code == 404:
            return render_template('error_404.html')
        else:
            data_list = response_list.json()
            json_data = dumps(data_list)
            return response.asset_retrieve(json_data)
    return render_template('resource_template.html', title=f'Delete {resource_name}', action=f'/ui_delete_{resource_name}')


@main.route('/ui_filter_<resource_name>', methods=['GET', 'POST'])
def ui_filter_resource(resource_name):
    if request.method == 'POST':
        url = f"{api_url}/get_members/{resource_name}/{request.form.get('Keyword')}"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_list = requests.get(url=url, headers=headers)
        if response_list.status_code == 404:
            return render_template('error_404.html')
        else:
            data_list = response_list.json()
            json_data = dumps(data_list)
            return response.asset_retrieve(json_data)
    return render_template('resource_template.html', title=f'Filter {resource_name}', action=f'/ui_filter_{resource_name}')


@main.route('/ui_update_<resource>', methods=['GET', 'POST'])
@nocache
def ui_update_resource(resource):
    if request.method == 'POST':
        if resource == 'country':
            update_item = request.form.get('country')
        elif resource == 'city':
            update_item = request.form.get('city')
        else:
            return render_template('error_404.html')
        url = f"{api_url}/update_{resource}/{update_item}/data/{request.form.get('field_name')}"
        field_name = request.form.get('field_name')
        country_update_body = {}
        field_value = request.form.get('field_value')
        country_update_body[field_name] = field_value
        country_update_request_body = json.dumps(country_update_body)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_update = requests.post(url=url, data=country_update_request_body, headers=headers)
        data_update = response_update.json()
        json_data = dumps(data_update)
        return response.asset_retrieve(json_data)
    if resource == 'country':
        return render_template('update_country.html')
    elif resource == 'city':
        return render_template('update_city.html')
    else:
        return render_template('error_404.html')


@main.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return 'Appliation shutting down...'