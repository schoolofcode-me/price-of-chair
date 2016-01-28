from flask import Blueprint, render_template

__author__ = 'jslvtr'


store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    return render_template('stores/store_index.jinja2')


@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():
    return "This is the create store page."


@store_blueprint.route('/<string:name>')
def store_page():
    pass