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
solar_empire_server.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
solar_empire_server.config[SQLALCHEMY_TRACK_MODIFICATIONS] = True 

#solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)

#without the flask migrate module, you need to instantiate
# databases with default values. That module wont be loaded 
# yet during the creation of a NEW game
class User(database.Model):
    login_id        = database.Column(database.Integer,     default = 0, \
                                                            primary_key=True)
    user_id         = database.Column(database.Integer,     default = 0)
    username        = database.Column(database.String(64),  default = "tourist", \
                                                            index=True, \
                                                            unique=True)
    email           = database.Column(database.String(120), index=True, unique=True)
    password_hash   = database.Column(database.String(128), default = DANGER_STRING)
    location        = database.Column(database.Integer,     default = 1) #E'Arth
    max_turns       = database.Column(database.Integer,     default = MAX_USER_TURNS)
    turns_run       = database.Column(database.Integer,     default = 0)
    safe_turns_left = database.Column(database.Integer,     default = 60)
    cash            = database.Column(database.Integer,     default = 1000)
    on_planet       = database.Column(database.Boolean,     default = 1)
    pocket_space    = database.Column(database.String(128), default = DANGER_STRING)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserShip(User):
    ship_id                    = database.Column(database.String(128))
    ship_type                  = database.Column(database.String(128))
    fighter_type               = database.Column(database.Integer)
    fighter_count              = database.Column(database.Integer)
    cargo_bay_size             = database.Column(database.Integer)
    size                       = database.Column(database.Integer)
    ship_name                  = database.Column(database.String(128))
    clan_id                    = database.Column(database.Integer) 
    shipclass                  = database.Column(database.String(128)) 
    class_name                 = database.Column(database.String(128))
    class_name_abbr            = database.Column(database.String(128))
    fighters_max               = database.Column(database.Integer)    
    mine_rate_metal            = database.Column(database.Integer)
    mine_rate_fuel             = database.Column(database.Integer)
    move_turn_cost             = database.Column(database.Integer)
    point_value                = database.Column(database.Integer)
    num_ot                     = database.Column(database.Integer)
    num_dt                     = database.Column(database.Integer)
    num_pc                     = database.Column(database.Integer) 
    cargo_manifest             = database.Column(database.PickleType)
    ship_location              = database.Column(database.String(128))
    configuration              = database.Column(database.String(128))
    equipment                  = database.Column(database.PickleType)
    damage_taken               = database.Column(database.Integer)
    shields_max                = database.Column(database.Integer)
    shields_current            = database.Column(database.Integer)
    hull_max                   = database.Column(database.Integer)
    hull_current               = database.Column(database.Integer)
    quark                      = database.Column(database.Integer)
    black_hole_gun             = database.Column(database.Integer)
    nova_wave_time             = database.Column(database.Integer)


admin = User(username=ADMIN_NAME, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest = User(username='guest', email='test@gamebiscuits.fightbiscuits.firewall-gateway.net' , password_hash = 'password')
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.commit()

solar_empire_server.run()

