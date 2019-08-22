# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
import json
import os


class Get_Country(object):

    def __init__(self):
        self.response_json_map = None
        try:
            app_port = int(os.environ['FLASK_RUN_PORT'])
        except KeyError:
            app_port = 5000
        self.get_country_url = 'http://localhost:' + str(app_port) + '/get_country/'
        self.get_country_continent_url = 'http://localhost:' + str(app_port) + '/get_country/continent/'
        self.get_countries_url = 'http://localhost:' + str(app_port) + '/get_countries'


    @classmethod
    def set_country(self, country):
        self.country = country

    def set_continent(self, continent):
        self.continent = continent

    def set_capital(self, capital):
        self.capital = capital

    def get_single_country(self):
        self.url = self.get_country_url + self.country
        response_country = requests.get(url=self.url)
        self.get_single_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        try:
            self.response_json_map['total'] = self.get_single_country['total']
        except KeyError:
            self.response_json_map['status'] = self.get_single_country['status']

    def get_country_by_capital(self):
        self.url = self.get_country_url + 'capital/' + self.capital
        response_country = requests.get(url=self.url)
        self.get_single_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        try:
            self.response_json_map['total'] = self.get_single_country['total']
        except KeyError:
            self.response_json_map['status'] = self.get_single_country['status']

    def get_continent_country(self):
        self.url = self.get_country_continent_url + self.continent
        response_country = requests.get(url=self.url)
        self.get_continent_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        self.response_json_map['total'] = self.get_continent_country['total']

    def get_continent_country_list(self):
        self.url = self.get_country_continent_url + self.continent + '/name'
        response_country = requests.get(url=self.url)
        self.get_continent_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        self.response_json_map['total'] = self.get_continent_country['total']

    def get_all_countries(self):
        self.url = self.get_countries_url
        response_country = requests.get(url=self.url)
        self.get_all_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        self.response_json_map['total'] = self.get_all_country['total']

    def get_country_list(self):
        self.url = self.get_country_url + 'name'
        response_country = requests.get(url=self.url)
        self.get_all_country = response_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_country.status_code
        self.response_json_map['total'] = self.get_all_country['total']

    def single_country_base_map(self, key):
        for items in self.get_single_country['countries']:
            self.response_json_map[key] = self.get_single_country['countries'][key]

    def single_country_currency_map(self, key):
        for items in self.get_single_country['countries']['currency']:
            self.response_json_map[key] = self.get_single_country['countries']['currency'][key]
