#!/usr/bin/python3
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
import solar_empire.configuration_options
from solar_empire.configuration_options import *
from solar_empire.models import *

##DOTO: require a hacking tool to alter a POST parameter to access an AI
## AI invader CLAN "network"
## have a field that you modify and use burpsuite
## to change things and you get sent to a "control panel"
### Make a new route in flask and dont advertise it but hide it "in the source"
## allowing you to command the enemy... enemy armies are limited
#if requirements not installed, get them, necessary for non-install migrations

solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)
#migrate     = Migrate(solar_empire_server, database)
admin       = User(username=ADMIN_NAME, email=ADMIN_EMAIL , password = ADMIN_PASSWORD)
guest       = User(username='guest', email='test@gamebiscuits.fightbiscuits.firewall-gateway.net' , password = 'password')
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.commit()

from solar_empire.routes import *

########################################################################
## move to routes.py
########################################################################

########################################################################
## move to game_actions.py
########################################################################

########################################################################
## move to new_game_setup.py
########################################################################
########################################################################
## move to ... right here?
########################################################################

if __name__ == '__main__':
    solar_empire_server.run()