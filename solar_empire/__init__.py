#!/usr/bin/python3

from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy
from flask.config import Config
#from flask_migrate import Migrate
#if requirements not installed, get them, necessary for non-install migrations
HTTP_HOST          = "gamebiscuits"
ADMIN_NAME         = 'moop'
ADMIN_PASSWORD     = "password"
ADMIN_EMAIL        = "game_admin" + "@" + HTTP_HOST
DATABASE           = "solar_empire-python"

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database     = SQLAlchemy(solar_empire_server)
#migrate     = Migrate(solar_empire_server, database)

import solar_empire.inc.configuration_options
from solar_empire.inc.configuration_options import *

from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
#from solar_empire.models.social_models import *
#from solar_empire.models.storekeeper_models import *
#from solar_empire.models.resource_models import *
#from solar_empire.models.equipment_models import *
#from solar_empire.models.system_models import *

admin     = User(username=ADMIN_NAME, user_id = 1, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest     = User(username='guest',    user_id = 2, email='test@game.net' , password_hash = 'password')
adminship = UserShip(ship_id=1, ship_name='admin ship', ship_type=1)
guestship = UserShip(ship_id=2, ship_name='guest ship', ship_type=2)  
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.commit()

    
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