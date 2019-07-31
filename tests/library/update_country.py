# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
import json


class Update_Country(object):

    update_country_body = {}

    def __init__(self):
        self.response_json_map = None
        self.update_country_body = {}
        self.update_country_body['currency'] = {}


    @classmethod
    def add_country(self, country):
        self.country = country

    def add_param(self, param):
        self.param = param

    def add_value(self, value):
        self.value = value

    def add_type(self, type):
        self.type = type

    def update_country(self):
        self.url = 'http://localhost:5000/update/' + self.country + '/data/' + self.param
        if self.param == 'population':
            self.update_country_body[self.param] = int(self.value)
        elif self.param == 'currency':
            self.url = 'http://localhost:5000/update/' + self.country + '/' + self.param
            self.update_country_body[self.param]['name'] = self.value
            self.update_country_body[self.param]['type'] = self.type
        else:
            self.update_country_body[self.param] = self.value
        update_country_request_body = json.dumps(self.update_country_body)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_update_country = requests.post(url=self.url, data=update_country_request_body, headers=headers)
        self.data_update_country = response_update_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_update_country.status_code

    def country_success_map(self):
        self.response_json_map['message'] = self.data_update_country['message']
        self.response_json_map['status'] = self.data_update_country['status']
