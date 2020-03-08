#!/usr/bin/python3
import pip
import datetime
import solar_empire.configuration_options
from solar_empire.configuration_options import *
from solar_empire.models import *
:TODO
## require a hacking tool to alter a POST parameter to access an AI
## AI invader CLAN "network"
## have a field that you modify and use burpsuite
## to change things and you get sent to a "control panel"
### Make a new route in flask and dont advertise it but hide it "in the source"
## allowing you to command the enemy... enemy armies are limited
#if requirements not installed, get them, necessary for non-install migrations
def import_or_install(package):
    for each in package:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])       

#get all the things!
import_or_install(things_this_app_needs)

from flask import Flask, render_template, Response, Request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)

import solar_empire.models

migrate     = Migrate(solar_empire_server, database)

admin       = User(username=ADMIN_NAME, email=ADMIN_EMAIL , password = ADMIN_PASSWORD)
guest       = User(username='guest', email='test@gamebiscuits.fightbiscuits.firewall-gateway.net' , password = 'password')

database.create_all()
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