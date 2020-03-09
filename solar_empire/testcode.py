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

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)

class User(database.Model):
    login_id        = database.Column(database.Integer, primary_key=True)
    user_id         = database.Column(database.Integer)
    username        = database.Column(database.String(64), index=True, unique=True)
    email           = database.Column(database.String(120), index=True, unique=True)
    password_hash   = database.Column(database.String(128))
    location        = database.Column(database.String(128))
    max_turns       = database.Column(database.Integer)
    turns_run       = database.Column(database.Integer)
    safe_turns_left = database.Column(database.Integer)
    cash            = database.Column(database.Integer)
    on_planet       = database.Column(database.Boolean)
    pocket_space    = database.Column(database.String(128))
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


solar_empire_server.route('/',             methods=['GET', 'POST'])
solar_empire_server.route('/login',        methods=['GET', 'POST'])
solar_empire_server.route('/user',         methods=['GET', 'POST'])
solar_empire_server.route('/diary',        methods=['GET', 'POST'])
solar_empire_server.route('/location',     methods=['GET', 'POST'])
solar_empire_server.route('/news',         methods=['GET', 'POST'])
solar_empire_server.route('/politics',     methods=['GET', 'POST'])
solar_empire_server.route('/message',      methods=['GET', 'POST'])
solar_empire_server.route('/mpage',        methods=['GET', 'POST'])
solar_empire_server.route('/clan',         methods=['GET', 'POST'])
solar_empire_server.route('/forum',        methods=['GET', 'POST'])
solar_empire_server.route('/player_stat',  methods=['GET', 'POST'])
solar_empire_server.route('/help',         methods=['GET', 'POST'])
solar_empire_server.route('/options',      methods=['GET', 'POST'])
solar_empire_server.route('/developer',    methods=['GET', 'POST'])
solar_empire_server.route('/game_info',    methods=['GET', 'POST'])
solar_empire_server.route('/clan_forum',   methods=['GET', 'POST'])
solar_empire_server.route('/game_status',  methods=['GET', 'POST'])

def index():
    return render_template('index.html')

def login_form():
    return render_template('login.html')

def game_page():
    return render_template('game_page.html')

admin       = User(username=ADMIN_NAME, email=ADMIN_EMAIL , password = ADMIN_PASSWORD)
guest       = User(username='guest', email='test@gamebiscuits.fightbiscuits.firewall-gateway.net' , password = 'password')
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.commit()

solar_empire_server.run()

