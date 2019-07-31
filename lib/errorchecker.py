# errorchecker.py

from flask import Blueprint, jsonify

errorchecker = Blueprint('errorchecker', __name__)

@errorchecker.errorhandler(409)
def data_conflict(country_name):
    message = {
        'status' : 409,
        'message' : 'Country:' + country_name + ' Already Exists'
    }
    resp = jsonify(message)
    resp.status_code = 409
    return resp

@errorchecker.errorhandler(404)
def data_not_found_country(country_name):
    message = {
        'status' : 404,
        'message' : 'Country:' + country_name + ' Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@errorchecker.errorhandler(404)
def data_not_found_continent(continent):
    message = {
        'status' : 404,
        'message' : 'No Countries For Continent: ' + continent + ' Found in Database'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@errorchecker.errorhandler(500)
def int_serv_error_bad_param(param):
    message = {
        'status' : 500,
        'message' : 'Invalid Parameter:' + param + ' Sent'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@errorchecker.errorhandler(500)
def param_mismatch_error():
    message = {
        'status' : 500,
        'message' : 'Invalid Request Body'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp

@errorchecker.errorhandler(500)
def invalid_country():
    message = {
        'status' : 500,
        'message' : 'Country Name Mismatch'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@errorchecker.errorhandler(404)
def no_countries():
    message = {
        'status' : 404,
        'message' : 'No Countries In Database'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp