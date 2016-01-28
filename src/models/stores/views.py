import json

from flask import Blueprint, render_template, request

from src.models.stores.store import Store

__author__ = 'jslvtr'


store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    stores = Store.all()
    return render_template('stores/store_index.jinja2', stores=stores)


@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():
    # name, url_prefix, tag_name, query
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name, query).save_to_mongo()

    # What happens if it's a GET request
    return render_template("stores/new_store.jinja2")


@store_blueprint.route('/<string:name>')
def store_page():
    pass