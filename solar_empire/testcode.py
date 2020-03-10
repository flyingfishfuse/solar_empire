import os
from flask.config import Config
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy

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
URL_SHORT          = "asdf"
SEND_AUTH_MAIL     = True
SESSION_TIME_LIMIT = 3600
ADMIN_NAME = "Emperor of Sol"
ADMIN_PASSWORD = "password"
ADMIN_EMAIL = "game_admin" + "@" + HTTP_HOST + SERVER_HOST + DOMAIN
ADMIN_USER_ID = 1
OWNER_ID = 1
#basedir = os.path.abspath(os.path.dirname(__file__))
things_this_app_needs = ['flask' , "flask-sqlalchemy"]
MAX_USER_TURNS = 30
DANGER_STRING= "you should NEVER see this string. Something errored HARD . TACOCAT"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)

#without the flask migrate module, you need to instantiate
# databases with default values. That module wont be loaded 
# yet during the creation of a NEW game
class User(database.Model):
    user_id = database.Column(database.Integer, default = 0, primary_key = True)
    username = database.Column(database.String(64),  default = "tourist", index=True, unique=True)
    email = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128), default = DANGER_STRING)
    turns_run = database.Column(database.Integer, default = 0)
    cash = database.Column(database.Integer, default = 1000)
    
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.user_id , self.username)


class UserShip(User):
    ship_id = database.Column(database.String(128), primary_key = True)
    ship_name = database.Column(database.String(128))
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.ship_id , self.ship_name)


admin = User(username=ADMIN_NAME, user_id = 1, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest = User(username='guest',    user_id = 2, email='test@game.net' , password_hash = 'password')
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.commit()

def update_database(thing):
    database.session.add(thing)
    database.commit()


def user_by_id(id_of_user):
	return User.query.filter_by(user_id = id_of_user).first()



solar_empire_server.run()

