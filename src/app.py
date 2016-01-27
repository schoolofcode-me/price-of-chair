from flask import Flask, render_template
from src.common.database import Database

__author__ = 'jslvtr'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.jinja2')

from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
