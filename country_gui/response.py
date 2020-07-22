from flask import Blueprint, jsonify, render_template
from os import path
from json2html import *
from w3lib.html import replace_entities

response = Blueprint('response', __name__)
basepath = path.dirname(__file__)
html_outfile = path.abspath(path.join(basepath, "templates", "response.html"))

def asset_retrieve(json_data):
    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Error\" class=\"table\"" "border=2")
    output_escaped = replace_entities(output)
    with open(html_outfile, 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write('<div class="container">')
        outf.write(output_escaped)
        outf.write('{% endblock %}')

    return render_template('response.html')


def asset_retrieve_details(json_data, country_name):
    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Error\" class=\"table\"" "border=2")
    output_escaped = replace_entities(output)
    with open(html_outfile, 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write('<div class="container">')
        outf.write(output_escaped)
        outf.write('<iframe src="https://en.wikipedia.org/wiki/')
        outf.write(country_name + '" width="100%" height="500">')
        outf.write('<p>Your browser does not support iframes.</p>')
        outf.write('</iframe>')
        outf.write('{% endblock %}')

    return render_template('response.html')