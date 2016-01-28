from flask import Blueprint

__author__ = 'jslvtr'


alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return 'This is the Alerts Index'


@alert_blueprint.route('/new', methods=['POST'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    return alert_id
