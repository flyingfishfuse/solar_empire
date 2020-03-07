#!/usr/bin/python3

import os
import pip
import datetime

VERSION            = 'Generic SE 2.9.1 - MODIFIED:Python Language Conversion -  Version : 0.01'
DATABASE_HOST      = "localhost"
DATABASE           = "solar_empire-python"
DATABASE_USER      = "moop"
DATABASE_PASSWORD  = "password"

SERVER_NAME        = "Solar Empire: 2020 - Python Edition"
SERVER_ADDRESS     = ('localhost', 4443)
HTTP_HOST          = "gamebiscuits"
SERVER_HOST        = "fightbiscuits"
DOMAIN             = "firewall-gateway.net"
GAME_DIR           = "/solar_empire/"
URL_FULL           = "https://" + HTTP_HOST + SERVER_HOST + DOMAIN + GAME_DIR

SEND_AUTH_MAIL     = True
SESSION_TIME_LIMIT = 3600

ADMIN_NAME = "Emperor of Sol"
ADMIN_EMAIL = "game_admin" + "@" + HTTP_HOST + SERVER_HOST + DOMAIN
ADMIN_USER_ID = 1
OWNER_ID = 1

basedir = os.path.abspath(os.path.dirname(__file__))
things_this_app_needs = ['flask' , "flask-sqlalchemy"]

def import_or_install(package):
    for each in package:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])       

#get all the things!
import_or_install(things_this_app_needs)

from flask import Flask, render_template, Response, Request
from solar_empire.models import User
import solar_empire.common

solar_empire_server = Flask(__name__ , template_folder="templates" )

from flask_sqlalchemy import SQLAlchemy
from flask.config import Config
from flask_migrate import Migrate

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
solar_empire_server.config.from_object(Config)

database    = SQLAlchemy(solar_empire_server)
migrate     = Migrate(solar_empire_server, database)

database.create_all()
admin       = User(username=ADMIN_NAME, email=ADMIN_EMAIL , password = ADMIN_PASSWORD)
guest       = User(username='guest', email='test@gamebiscuits.fightbiscuits.firewall-gateway.net' , password = 'password')
database.session.add(admin)
database.session.add(guest)
database.session.commit()

@solar_empire_server.route('/', methods=['GET', 'POST'])
@solar_empire_server.route('/login', methods=['GET', 'POST'])
@solar_empire_server.route('/user', methods=['GET', 'POST'])
@solar_empire_server.route('/diary', methods=['GET', 'POST'])
@solar_empire_server.route('/location', methods=['GET', 'POST'])
@solar_empire_server.route('/news', methods=['GET', 'POST'])
@solar_empire_server.route('/politics', methods=['GET', 'POST'])
@solar_empire_server.route('/message', methods=['GET', 'POST'])
@solar_empire_server.route('/mpage', methods=['GET', 'POST'])
@solar_empire_server.route('/clan', methods=['GET', 'POST'])
@solar_empire_server.route('/forum', methods=['GET', 'POST'])
@solar_empire_server.route('/player_stat', methods=['GET', 'POST'])
@solar_empire_server.route('/help', methods=['GET', 'POST'])
@solar_empire_server.route('/options', methods=['GET', 'POST'])
@solar_empire_server.route('/developer', methods=['GET', 'POST'])
@solar_empire_server.route('/game_info', methods=['GET', 'POST'])
@solar_empire_server.route('/clan_forum', methods=['GET', 'POST'])
@solar_empire_server.route('/logout', methods=['GET', 'POST'])
@solar_empire_server.route('/logout', methods=['GET', 'POST'])
@solar_empire_server.route('/logout', methods=['GET', 'POST'])
@solar_empire_server.route('/logout', methods=['GET', 'POST'])

def index():
    return render_template('index.html')

def login_form():
    return render_template('login.html')

def game_page():
    return render_template('game_page.html')

def bilkos_blackmarket_shop():
    return render_template('bilkos.html')


if __name__ == '__main__':
    solar_empire_server.run()