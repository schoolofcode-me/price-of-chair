from flask import Blueprint, request, render_template

__author__ = 'jslvtr'

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return 'This is the Alerts Index'


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def create_alert():
    if request.method == 'POST':
        # Deal with what happens when the user has submitted the form
        # to create an alert
        pass

    # What happens if it's a GET request
    return render_template("alerts/new_alert.jinja2")  # Send the user an error if their login was invalid


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    return alert_id
