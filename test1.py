from flask.config import Config
from flask import Flask, render_template, Response, Request ,Config
from flask_sqlalchemy import SQLAlchemy
import numpy 

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

########################################################################
## SYSTEM INFO
########################################################################
class SystemInfo(database.Model):
    __tablename__       = 'SystemInfo'
    system_id           = database.session.Column(database.Integer, primary_key = True, unique=True, autoincrement=True)
    location_id         = database.session.Column(database.session.Integer)
    name                = database.session.Column(database.session.String(128))
    x_loc               = database.session.Column(database.session.Integer)
    y_loc               = database.session.Column(database.session.Integer)
    num_stars           = database.session.Column(database.session.Integer)
    navigation_hazard   = database.session.Column(database.session.Boolean)
    random_events_level = database.session.Column(database.session.Integer)
    links               = database.session.Column(database.session.PickleType)

def game_grid(map_height:int, map_width:int):
    """
    This function generates the grid, 
    with size_x and size_y constraints
    """
    # declare the existance of a dimension
    # (I choose for this to be silly and diffucult to comprehend)
    #empty_pie = numpy.zeros(size_y,size_x)
    a = []
    x = 0
    y = 0
    # we have to account for indexing differences between 
    # types and methods
    x_max = map_width + 1
    y_max = map_height + 1
    #map_size = x * y
    def make_x(x_c,y_c):
        for each in range(0,x_max):   
            a.append([x_c,y_c])
            x_c = x_c+1
        # now we have an array of a[[1,y]...[100,y]]
    #make y cols to 100, populating with make_x() to generate x rows
    for coords in range(0,y_max):
        make_x(x,y)
        y = y+1
    return a


admin     = User(username=ADMIN_NAME, user_id = 1, email=ADMIN_EMAIL , password_hash = ADMIN_PASSWORD)
guest     = User(username='guest',    user_id = 2, email='test@game.net' , password_hash = 'password')
adminship = UserShip(ship_id=1, ship_name='admin ship', ship_type=1)
guestship = UserShip(ship_id=2, ship_name='guest ship', ship_type=2) 
#on a 1000x1000 grid
system1   = SystemInfo(system_id=1, \
                        x_loc=1, \
                        y_loc=1, \
                        num_stars=1, \
                        navigation_hazard=False, \
                        random_events_level=0
                        links= [[1,2],[2,1],[2,2])

database.create_all()
database.session.add(admin)
database.session.add(guest)
database.session.add(adminship)
database.session.add(guestship)
database.session.commit()
print(User.query.all())
print(UserShip.query.all())