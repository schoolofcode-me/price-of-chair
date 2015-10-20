from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.users.errors import UserException
from src.models.users.user import User

__author__ = 'jslvtr'


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login')
def login_user():
    pass


@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
