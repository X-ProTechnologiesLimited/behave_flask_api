from flask import Blueprint, jsonify, render_template
from os import path
from json2html import *
import json, re, lxml
from bs4 import BeautifulSoup

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

    with open("templates/response.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        re_url = re.compile(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')

        for tag in soup.find_all(text=True):
            tags = []
            url = False

            for t in re_url.split(tag.string):
                if re_url.match(t):
                    a = soup.new_tag("a", href=t, target='_blank')
                    a.string = t
                    tags.append(a)
                    url = True
                else:
                    tags.append(t)

            if url:
                for t in tags:
                    tag.insert_before(t)
                tag.extract()

        with open("templates/response.html", "w") as outf:
            outf.write(str(soup))

    return render_template('response.html')