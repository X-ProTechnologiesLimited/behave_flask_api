# response.py

from flask import jsonify


def success_message(operation, resource_type, resource_name):
    message = {
        'status': 201,
        'message': f'{resource_type}: {resource_name} is {operation}ed successfully'
    }
    resp = jsonify(message)
    resp.status_code = 201
    return resp
