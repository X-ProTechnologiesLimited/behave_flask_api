# main.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
import json
from json2html import *
from bson.json_util import dumps
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ui_add_country')
def ui_add_country():
    return render_template('add_new_country.html')

@main.route('/ui_add_country', methods=['POST'])
def ui_add_country_post():
    response_json_map = None
    new_country_add_body = {}
    new_country_add_body['currency'] = {}
    url = 'http://host.docker.internal:5000/add_country/' + request.form.get('Country')
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

    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Add Response\" class=\"table table-striped\"" "border=2")

    with open('templates/response_added_country.html', 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('response_added_country.html')

@main.route('/ui_view_country')
def ui_view_country():
    url = 'http://host.docker.internal:5000/get_country/name'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_country_list = requests.get(url=url, headers=headers)
    data_country_list = response_country_list.json()
    json_data = dumps(data_country_list)
    output = json2html.convert(json=json_data, table_attributes="id=\"Country List\" class=\"table table-striped\"" "border=2")

    with open('templates/added_country.html', 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('added_country.html')


@main.route('/ui_view_continents')
def ui_view_continent():
    url = 'http://host.docker.internal:5000/get_continent/name'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_continent_list = requests.get(url=url, headers=headers)
    data_continent_list = response_continent_list.json()
    json_data = dumps(data_continent_list)
    output = json2html.convert(json=json_data, table_attributes="id=\"Continent List\" class=\"table table-striped\"" "border=2")

    with open('templates/added_continents.html', 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('added_continents.html')


@main.route('/ui_search')
def ui_search_country():
    return render_template('search.html')

@main.route('/ui_search', methods=['POST'])
def search_country_post():
    url = 'http://host.docker.internal:5000/search/country/qs=' + request.form.get('Keyword')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_continent_list = requests.get(url=url, headers=headers)
    data_continent_list = response_continent_list.json()
    json_data = dumps(data_continent_list)
    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Search List\" class=\"table table-striped\"" "border=2")

    with open('templates/search_response.html', 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('search_response.html')


@main.route('/ui_view_specific_country')
def ui_view_spec_country():
    return render_template('view_specific.html')

@main.route('/ui_view_specific_country', methods=['POST'])
def ui_view_spec_country_post():
    url = 'http://host.docker.internal:5000/get_country/' + request.form.get('Country')
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response_list = requests.get(url=url, headers=headers)
    data_list = response_list.json()
    json_data = dumps(data_list)
    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Country Details\" class=\"table table-striped\"" "border=2")

    with open('templates/country_details.html', 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('country_details.html')
