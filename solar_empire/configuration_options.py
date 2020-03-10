import os
from flask.config import Config
import random
#software stuff
VERSION            = 'Generic SE 2.9.1 - MODIFIED:Python Language Conversion -  Version : 0.01'
basedir = os.path.abspath(os.path.dirname(__file__))
things_this_app_needs = ['flask' , "flask-sqlalchemy"]

#server stuff
SERVER_NAME        = "Solar Empire: 2020 - Python Edition"
SERVER_ADDRESS     = ('localhost', 4443)
HTTP_HOST          = "gamebiscuits"
SERVER_HOST        = "fightbiscuits"
DOMAIN             = "firewall-gateway.net"
GAME_DIR           = "/solar_empire/"
URL_FULL           = "https://" + HTTP_HOST + SERVER_HOST + DOMAIN + GAME_DIR
URL_SHORT          = "asdf"
SEND_AUTH_MAIL     = True
SESSION_TIME_LIMIT = 3600
#user stuff
ADMIN_NAME = "Emperor of Sol"
ADMIN_PASSWORD = "password"
ADMIN_EMAIL = "game_admin" + "@" + HTTP_HOST + SERVER_HOST + DOMAIN
ADMIN_USER_ID = 1
OWNER_ID = 1

#DB STUFF 
DATABASE_HOST      = "localhost"
DATABASE           = "solar_empire-python"
DATABASE_USER      = "moop"
DATABASE_PASSWORD  = "password"
USER_TABLE_NAME = "User"
DANGER_STRING= "you should NEVER see this string. Something errored HARD . TACOCAT"

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


#GameVars.sv_turns = 30
QUARK_DAMAGE = random.randint(400,1000)
SAFE_TURNS   = 60
MAX_USER_TURNS = 30