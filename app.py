from flask import Flask
from flask login import LoginManager
from application.database import db

import datetime

app = None

login_manager = LoginManager()

def create_app():
app = Flask(_name
app. debug = True
app. config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iescpdata.db'

db.init_app(app)

my_login_manager = LoginManager()
my_login_manager.init_app(app)

from application.models import User, Admin, Sponsor, Event, Registration, Payment, Feedback