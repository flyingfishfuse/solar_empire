import os
from flask.config import Config
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy
DATABASE_HOST      = "localhost"
DATABASE           = "solar_empire-python"
DATABASE_USER      = "moop"
DATABASE_PASSWORD  = "password"
SERVER_NAME        = "Solar Empire: 2020 - Python Edition"
SERVER_ADDRESS     = ('localhost', 4443)
HTTP_HOST          = "gamebiscuits"
GAME_DIR           = "/solar_empire/"
SEND_AUTH_MAIL     = True
SESSION_TIME_LIMIT = 3600
ADMIN_NAME = "Emperor of Sol"
ADMIN_PASSWORD = "password"
ADMIN_EMAIL = "game_admin" + "@" + HTTP_HOST
#basedir = os.path.abspath(os.path.dirname(__file__))
DANGER_STRING= "TACOCAT"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database    = SQLAlchemy(solar_empire_server)

def update_database(thing):
    database.session.add(thing)
    database.commit()


def user_by_id(id_of_user):
    return User.query.all.filter_by(user_id = id_of_user).first()

#without the flask migrate module, you need to instantiate
# databases with default values. That module wont be loaded 
# yet during the creation of a NEW game
class User(database.Model):
    user_id       = database.Column(database.Integer,     default = 0, primary_key = True)
    username      = database.Column(database.String(64),  default = "tourist", index=True, unique=True)
    email         = database.Column(database.String(120), default = DANGER_STRING , index=True, unique=True)
    password_hash = database.Column(database.String(128), default = DANGER_STRING)
    turns_run     = database.Column(database.Integer,     default = 0)
    cash          = database.Column(database.Integer,     default = 1000)
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.user_id , self.username)

class UserShip(User):
    ship_id      = database.Column(database.String(128),  default = "1")
    ship_name    = database.Column(database.String(128),  default = "goodship moop")
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.ship_id , self.ship_name)

admin = User(username=ADMIN_NAME, user_id = 1, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest = User(username='guest1',    user_id = 2, email='test@game.net' , password_hash = 'password')
user = User(username='guest2',    user_id = 3, email='test@game.net' , password_hash = 'password')
usership = UserShip()
adminship = UserShip()
guestship = UserShip()

database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.add(user)
database.session.add(usership)
database.session.add(adminship)
database.session.add(guestship)
database.session.commit()
#solar_empire_server.run()

User.query.all()
User.query.filter_by(username='admin').first()

#>>> user.email
#>>> print(user.email)
#None
#>>> guest.email
#'test@game.net'
#>>> guest.email = 'blorp'
#>>> database.session.commit()
#>>> guest.email
#'blorp'
#>>> User.query.filter_by(username='admin').first()
#>>> print(User.query.filter_by(username='admin').first())
#None
#>>> print(User.query.filter_by(username=ADMIN_NAME).first())
#None

#>>> def return_user_by_id(id_of_user):
#...     return database.session.query('user_id')
#... 
#>>> return_user_by_id(1)
#<flask_sqlalchemy.BaseQuery object at 0x7f49aad4af60>
#>>> asdf = return_user_by_id(1)
#>>> dbquery = database.session.query('user_id')
#>>> dbquery.
#┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
#│ add_column                    add_columns                   add_entity                    all                                    │
#│ as_scalar                     autoflush                     column_descriptions           correlate                              │
#│ count                         cte                           delete                        dispatch                               │
#└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

>>> asdf = database.session.query(User.user_id == 1)
>>> asdf
<flask_sqlalchemy.BaseQuery object at 0x7f49aacff780>

>>> asdf = database.session.query(User)
>>> asdf
<flask_sqlalchemy.BaseQuery object at 0x7f49aacff780>

>>> User.query.filter_by(user_id == 1 ).first()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    User.query.filter_by(user_id == 1 ).first()
NameError: name 'user_id' is not defined
