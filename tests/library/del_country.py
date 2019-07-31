# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
import json


class Del_Country(object):

    def __init__(self):
        self.response_json_map = None


    @classmethod
    def set_country(self, country):
        self.country = country

    def del_country(self):
        self.url = 'http://localhost:5000/delete/' + self.country
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response_del_country = requests.post(url=self.url, headers=headers)
        self.data_del_country = response_del_country.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = response_del_country.status_code

    def country_del_map(self):
        self.response_json_map['message'] = self.data_del_country['message']
        self.response_json_map['status'] = self.data_del_country['status']
