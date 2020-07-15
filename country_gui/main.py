# main.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
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
api_url = 'http://'+api_host+':'+api_port
main = Blueprint('main', __name__)

@main.route('/')
@nocache
def index():
    return render_template('index.html')

@main.route('/ui_add_country')
@nocache
def ui_add_country():
    return render_template('add_new_country.html')

@main.route('/ui_add_country', methods=['POST'])
@nocache
def ui_add_country_post():
    response_json_map = None
    new_country_add_body = {}
    new_country_add_body['currency'] = {}
    url = api_url + '/add_country/' + request.form.get('Country')
    new_country_add_body['country_name'] = request.form.get('Country')
    new_country_add_body['capital'] = request.form.get('Capital')
    new_country_add_body['continent'] = request.form.get('Continent')
    new_country_add_body['subregion'] = request.form.get('Subregion')
    new_country_add_body['currency']['name'] = request.form.get('Currency_Name')
    new_country_add_body['currency']['type'] = request.form.get('Currency_Type')
    new_country_add_body['population'] = int(request.form.get('Population'))
    new_country_add_request_body = json.dumps(new_country_add_body)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_new_country = requests.post(url=url, data=new_country_add_request_body, headers=headers)
    data_new_country = response_new_country.json()
    json_data = dumps(data_new_country)

    return response.asset_retrieve(json_data)


# @main.route('/ui_view_country')
# @nocache
# def ui_view_country():
#     url = api_url+'/get_country/name'
#     headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#     response_country_list = requests.get(url=url, headers=headers)
#     data_country_list = response_country_list.json()
#     json_data = dumps(data_country_list)
#
#     return response.asset_retrieve(json_data)

@main.route('/ui_view_country_details/<country_name>')
@nocache
def ui_view_country_details(country_name):
    url = api_url + '/get_country/' + country_name
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve_details(json_data, country_name)

@main.route('/ui_view_country_resources')
@nocache
def ui_view_country_resources():
    url = api_url+'/get_country/resources/all'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_country_list = requests.get(url=url, headers=headers)
    data_country_list = response_country_list.json()
    json_data = dumps(data_country_list)

    return response.asset_retrieve(json_data)



@main.route('/ui_view_continent_members/<continent_name>')
@nocache
def ui_view_continent_members(continent_name):
    url = api_url+'/get_members/continent/' + continent_name
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_continent_list = requests.get(url=url, headers=headers)
    data_continent_list = response_continent_list.json()
    json_data = dumps(data_continent_list)

    return response.asset_retrieve(json_data)



@main.route('/ui_search')
@nocache
def ui_search_country():
    return render_template('search.html')

@main.route('/ui_search', methods=['POST'])
@nocache
def search_country_post():
    url = api_url+'/search/country/qs=' + request.form.get('Keyword')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_continent_list = requests.get(url=url, headers=headers)
    data_continent_list = response_continent_list.json()
    json_data = dumps(data_continent_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_view_specific_country')
@nocache
def ui_view_spec_country():
    return render_template('view_specific.html')

@main.route('/ui_view_specific_country', methods=['POST'])
@nocache
def ui_view_spec_country_post():
    url = api_url+'/get_country/' + request.form.get('Country')
    country_name_uncoded = urllib.parse.unquote_plus(request.form.get('Country'))
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve_details(json_data, country_name_uncoded)


@main.route('/ui_delete_country')
@nocache
def ui_delete_country():
    return render_template('delete_country.html')

@main.route('/ui_delete_country', methods=['POST'])
@nocache
def ui_delete_country_delete():
    url = api_url+'/delete/' + request.form.get('Country')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.delete(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_delete_continent')
@nocache
def ui_delete_continent():
    return render_template('delete_continent.html')

@main.route('/ui_delete_continent', methods=['POST'])
@nocache
def ui_delete_continent_delete():
    url = api_url+'/delete/continent/' + request.form.get('Continent')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.delete(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_view_specific_continent')
@nocache
def ui_view_specific_continent():
    return render_template('view_specific_continent.html')

@main.route('/ui_view_specific_continent', methods=['POST'])
@nocache
def ui_view_specific_continent_post():
    url = api_url+'/get_members/continent/' + request.form.get('Continent')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_view_continent_resources')
@nocache
def ui_view_continent_resources():
    url = api_url+'/get_continent/resources'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_continent_list = requests.get(url=url, headers=headers)
    data_continent_list = response_continent_list.json()
    json_data = dumps(data_continent_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_search_by_capital')
@nocache
def ui_search_by_capital():
    return render_template('search_by_capital.html')

@main.route('/ui_search_by_capital', methods=['POST'])
@nocache
def ui_search_by_capital_post():
    url = api_url+'/get_country/capital/' + request.form.get('Capital')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)

    return response.asset_retrieve(json_data)


@main.route('/ui_update_country')
@nocache
def ui_update_country():
    return render_template('update_country.html')

@main.route('/ui_update_country', methods=['POST'])
@nocache
def ui_update_country_post():
    url = api_url+'/update/' + request.form.get('country_name') + '/data/' + request.form.get('field_name')
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


@main.route('/ui_update_currency')
@nocache
def ui_update_currency():
    return render_template('update_currency.html')

@main.route('/ui_update_currency', methods=['POST'])
@nocache
def ui_update_currency_post():
    url = api_url+'/update/' + request.form.get('country_name') + '/currency'
    country_currency_body = {}
    country_currency_body['currency'] = {}
    country_currency_body['currency']['name'] = request.form.get('currency_name')
    country_currency_body['currency']['type'] = request.form.get('currency_type')

    country_currency_request_body = json.dumps(country_currency_body)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_update = requests.post(url=url, data=country_currency_request_body, headers=headers)
    data_update = response_update.json()
    json_data = dumps(data_update)

    return response.asset_retrieve(json_data)

@main.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return 'Appliation shutting down...'