# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
import json
import os

class Del_Country(object):

    def __init__(self):
        self.response_json_map = None
        try:
            app_port = int(os.environ['FLASK_RUN_PORT'])
        except KeyError:
            app_port = 5000
        self.delete_country_url = 'http://localhost:' + str(app_port) + '/delete/country/'
        self.delete_continent_url = 'http://localhost:' + str(app_port) + '/delete/continent/'


    @classmethod
    def set_country(self, country):
        self.country = country

    def set_continent(self, continent):
        self.continent = continent

    def del_country(self):
        self.url = self.delete_country_url + self.country
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_del_country = requests.delete(url=self.url, headers=headers)
        self.data_del_country = response_del_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_del_country.status_code

    def country_del_map(self):
        self.response_json_map['message'] = self.data_del_country['message']
        self.response_json_map['status'] = self.data_del_country['status']

    def del_continent(self, continent):
        self.url = self.delete_continent_url + continent
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_del_continent = requests.delete(url=self.url, headers=headers)
        self.data_del_continent = response_del_continent.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_del_continent.status_code

    def continent_del_map(self):
        self.response_json_map['message'] = self.data_del_continent['message']
        self.response_json_map['status'] = self.data_del_continent['status']

