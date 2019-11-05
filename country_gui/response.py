from flask import Blueprint, jsonify, render_template
from os import path
from json2html import *

response = Blueprint('response', __name__)
basepath = path.dirname(__file__)
html_outfile = path.abspath(path.join(basepath, "templates", "response.html"))

def asset_retrieve(json_data):
    output = json2html.convert(json=json_data,
                               table_attributes="id=\"Error\" class=\"table table-striped\"" "border=2")
    with open(html_outfile, 'w') as outf:
        outf.write('{% extends "base.html" %}')
        outf.write('{% block content %}')
        outf.write(output)
        outf.write('{% endblock %}')

    return render_template('response.html')