from flask import Blueprint

__author__ = 'jslvtr'


store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    return "This is the Store Index"


@store_blueprint.route('/store/<string:name>')
def store_page():
    pass
