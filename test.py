import os
#from flask.config import Config
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy



DATABASE_HOST      = "localhost"
DATABASE           = "solar_empire-python"
DATABASE_USER      = "moop"
DATABASE_PASSWORD  = "password"
SERVER_NAME        = "Solar Empire: 2020 - Python Edition"
HTTP_HOST          = "gamebiscuits"
ADMIN_NAME         = "Emperor of Sol"
ADMIN_PASSWORD     = "password"
ADMIN_EMAIL        = "game_admin" + "@" + HTTP_HOST
DANGER_STRING= "TACOCAT"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///solar_empire_test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

solar_empire_server = Flask(__name__ , template_folder="templates" )
solar_empire_server.config.from_object(Config)
database = SQLAlchemy(solar_empire_server)
database.init_app(solar_empire_server)
#One to many relationship
#parent

class User(database.Model):
    __tablename__ = 'User'
    #PARENT: of UserShip, Primary key must link (be the same)
    id            = database.Column(database.Integer, primary_key = True, unique=True, autoincrement=True)
    #reference to CHILD then reference to SELF
    userid       = database.Column(database.relationship('UserShip', \
                            primaryjoin = 'and_(User.id == UserShip.user_id)' , \
                            backref     = 'User' , \
                            uselist     = False ))
#    userid        = database.Column(database.Integer)
    username      = database.Column(database.String(64), index=True)
    email         = database.Column(database.String(120), index=True)
    password_hash = database.Column(database.String(128))

    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.user_id , self.username)

#child
class UserShip(User):
    __tablename__  = 'UserShip'
    #CHILD OF USER: the primary key must link
    #ID is a "universal" identification for the db, SHIP_ID will be a variable 
    # used locally in the system that that user and ship are interacting in
    #id             = database.Column(database.Integer, primary_key=True)
    # The PRIMARY key that is linked bewteen the two, with a new name, the field you want to inherit, is declared next.
    #user_id        = database.Column(database.Integer, database.ForeignKey('User.userid'), nullable=False)
    ship_id        = database.Column(database.Integer)
    ship_name      = database.Column(database.String(128))
    # list of 1-whatever of ships
    ship_type      = database.Column(database.Integer)
    # PARENT OF GENERIC SHIP: the clsses must link like this, backref is __tablename__
    #linked_user    = database.relationship('GenericShip',backref='usership',uselist=False)
    def __repr__(self):
        return '<User id:{} name: {} >'.format(self.ship_id , self.ship_name)

admin = User(username='admin', userid = 1,  email="test@wat" , password_hash = 'passwordadmin')
guest = User(username='guest1', userid = 2, email='test1@game.net' , password_hash = 'password1')
user1 = User(username='guest2', userid = 3, email='test2@game.net' , password_hash = 'password2')
#ship_type = 1 is a special admin ship
usership = UserShip(ship_id=3, ship_name='user ship', ship_type=2)
adminship = UserShip(ship_id=1, ship_name='admin ship', ship_type=1)
guestship = UserShip(ship_id=2, ship_name='guest ship', ship_type=2)

database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.add(user1)
database.session.add(usership)
database.session.add(adminship)
database.session.add(guestship)
database.session.commit()
#solar_empire_server.run()

print(User.query.all())
print(database.session.User.query('User').all())
print(UserShip.query.all())
print(database.session.User.query('UserShip').all())
User.query.filter_by(username='admin').first()

#def user_by_id(id_of_user):
#    return User.query.all.filter_by(user_id = id_of_user).first()
