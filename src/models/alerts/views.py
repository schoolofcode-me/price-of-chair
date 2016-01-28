from flask import Blueprint, request, render_template, session

from src.models.alerts.alert import Alert
from src.models.items.item import Item
import src.models.users.decorators as user_decorators

__author__ = 'jslvtr'

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return 'This is the Alerts Index'


@alert_blueprint.route('/new', methods=['GET', 'POST'])
@user_decorators.requires_login
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = request.form['price_limit']

        item = Item(name, url)
        item.save_to_mongo()

        alert = Alert(session['email'], price_limit, item._id)
        alert.load_item_price()  # This already saves to MongoDB

    # What happens if it's a GET request
    return render_template("alerts/new_alert.jinja2")  # Send the user an error if their login was invalid


@alert_blueprint.route('/deactivate/<string:alert_id>')
@user_decorators.requires_login
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>')
@user_decorators.requires_login
def get_alert_page(alert_id):
    return alert_id
