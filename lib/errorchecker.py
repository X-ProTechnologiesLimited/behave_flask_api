# errorchecker.py

from flask import jsonify

def data_conflict(data_type, data):
    message = {
        'status': 409,
        'message': f'{data_type}: {data} Already Exists'
    }
    resp = jsonify(message)
    resp.status_code = 409
    return resp

def data_not_found(data_type, data):
    message = {
        'status': 404,
        'message': f'No data found for {data_type}: {data}'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


def data_not_found_country(country_name):
    message = {
        'status' : 404,
        'message' : 'Country:' + country_name + ' Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

def data_not_found_city_country(country_name):
    message = {
        'status' : 404,
        'message' : 'No city found for :' + country_name
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

def data_not_found_city(city_name):
    message = {
        'status' : 404,
        'message' : 'City:' + city_name + ' Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


def data_not_found_capital(capital):
    message = {
        'status' : 404,
        'message' : 'Country for Capital: ' + capital + ' Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp



def data_not_found_continent(continent):
    message = {
        'status' : 404,
        'message' : 'No Countries For Continent: ' + continent + ' Found in Database'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


def int_serv_error_bad_param(param):
    message = {
        'status' : 500,
        'message' : 'Invalid Parameter:' + param + ' Sent'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


def param_mismatch_error():
    message = {
        'status' : 500,
        'message' : 'Invalid Request Body'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp

def invalid_entry(entry_type):
    message = {
        'status': 500,
        'message': f'{entry_type} Mismatch'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp

def no_countries():
    message = {
        'status' : 404,
        'message' : 'No Countries In Database'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


def data_not_found_string(search_string):
    message = {
        'status' : 404,
        'message' : 'No Country found with search criteria: ' + search_string
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp