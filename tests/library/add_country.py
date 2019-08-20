# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
import json


class Add_Country(object):

    new_country_add_body = {}

    def __init__(self):
        self.response_json_map = None
        self.new_country_add_body = {}
        self.new_country_add_body['currency'] = {}
        self.bulk_country_add_body = {}
        self.bulk_country_add_body['currency'] = {}


    @classmethod
    def add_country(self, country):
        self.country = country

    def add_capital(self, capital):
        self.capital = capital

    def add_continent(self, continent):
        self.continent = continent

    def add_subregion(self, subregion):
        self.subregion = subregion

    def add_population(self, population):
        self.population = population

    def add_currency(self, currency, type):
        self.currency = currency
        self.type = type

    def new_country_add(self):
        self.url = 'http://localhost:5000/add_country/' + self.country
        self.new_country_add_body['country_name'] = self.country
        self.new_country_add_body['capital'] = self.capital
        self.new_country_add_body['continent'] = self.continent
        self.new_country_add_body['subregion'] = self.subregion
        self.new_country_add_body['currency']['name'] = self.currency
        self.new_country_add_body['currency']['type'] = self.type
        self.new_country_add_body['population'] = int(self.population)
        new_country_add_request_body = json.dumps(self.new_country_add_body)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_new_country = requests.post(url=self.url, data=new_country_add_request_body, headers=headers)
        self.data_new_country = response_new_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_new_country.status_code

    def country_success_map(self):
        self.response_json_map['message'] = self.data_new_country['message']
        self.response_json_map['status'] = self.data_new_country['status']


    def bulk_country_add(self, limit):
        n = 1
        while n <= limit:
            i = str(n)
            self.url = 'http://localhost:5000/add_country/' + self.continent + '_country_' + i
            self.bulk_country_add_body['country_name'] = self.continent + '_country_' + i
            self.bulk_country_add_body['capital'] = 'country_' + i + '_capital'
            self.bulk_country_add_body['continent'] = self.continent
            self.bulk_country_add_body['subregion'] = 'country_' + i + '_subregion'
            self.bulk_country_add_body['currency']['name'] = 'country_' + i + '_curr_name'
            self.bulk_country_add_body['currency']['type'] = 'country_' + i + '_curr_type'
            self.bulk_country_add_body  ['population'] = 500000
            new_country_add_request_body = json.dumps(self.bulk_country_add_body)
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            response_new_country = requests.post(url=self.url, data=new_country_add_request_body, headers=headers)
            self.data_new_country = response_new_country.json()
            self.response_json_map = {}
            self.response_json_map['http_response_code'] = response_new_country.status_code
            n += 1
