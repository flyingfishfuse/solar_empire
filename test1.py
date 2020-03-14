from flask.config import Config
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy

HTTP_HOST      = "gamebiscuits"
ADMIN_NAME     = "Emperor of Sol"
ADMIN_PASSWORD = "password"
ADMIN_EMAIL    = "game_admin"
DANGER_STRING  = "TACOCAT"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

server = Flask(__name__ , template_folder="templates" )
server.config.from_object(Config)
database = SQLAlchemy(server)
database.init_app(server)

class User(database.Model):
    __tablename__  = 'User'
    user_id       = database.Column(database.Integer,     primary_key = True, unique=True, autoincrement=True)
    username      = database.Column(database.String(64),  index=True, unique=True)
    email         = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128), default = DANGER_STRING)
    turns_run     = database.Column(database.Integer,     default = 0)
    cash          = database.Column(database.Integer,     default = 1000)
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.user_id , self.username)


class UserShip(User):
    __tablename__  = 'UserShip'
    ship_id        = database.Column(database.Integer)
    ship_name      = database.Column(database.String(128))
    ship_type      = database.Column(database.Integer)
    def __repr__(self):
        return '<UserShip id:{} name: {} >'.format(self.ship_id , self.ship_name)

admin     = User(username=ADMIN_NAME, user_id = 1, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest     = User(username='guest',    user_id = 2, email='test@game.net' , password_hash = 'password')
adminship = UserShip(ship_id=1, ship_name='admin ship', ship_type=1)
guestship = UserShip(ship_id=2, ship_name='guest ship', ship_type=2)   
database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.add(adminship)
database.session.add(guestship)
database.session.commit()
print(User.query.all())
print(UserShip.query.all())