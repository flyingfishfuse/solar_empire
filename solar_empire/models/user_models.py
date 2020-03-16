from solar_empire.inc.configuration_options import *
from solar_empire import database

class User(database.Model):
    __tablename__     = 'User'
    user_id           = database.Column(database.Integer,     primary_key = True, unique=True, autoincrement=True)
    username          = database.Column(database.String(64),  index=True, unique=True)
    email             = database.Column(database.String(120), index=True, unique=True)
    password_hash     = database.Column(database.String(128), default = DANGER_STRING)
    turns_run         = database.Column(database.Integer,     default = 0)
    cash              = database.Column(database.Integer,     default = 1000)
    location          = database.Column(database.String(128))
    max_turns         = database.Column(database.Integer)
    turns_run         = database.Column(database.Integer)
    safe_turns_left   = database.Column(database.Integer)
    cash_available    = database.Column(database.Integer)
    on_planet         = database.Column(database.Boolean)
    active            = database.Column(database.Boolean)
    game_login_count  = database.Column(database.Integer)
    pocket_space      = database.Column(database.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)

#  fuck I love python... you PUT THE USER
## IN THE SHIP!
class UserShip(User):
    __tablename__  = 'UserShip'
    ship_id                    = database.Column(database.Integer)
    ship_name                  = database.Column(database.String(128))
    ship_type                  = database.Column(database.Integer)
    clan_id                    = database.Column(database.Integer) 
    #special weapons
    #shots
    quark                      = database.Column(database.Integer)
    black_hole_gun             = database.Column(database.Integer)
    nova_wave_time             = database.Column(database.Integer)
    #resources
    minerals                   = database.Column(database.Integer)
    technology                 = database.Column(database.Integer)
    organics                   = database.Column(database.Integer)
    fuel                       = database.Column(database.Integer)
    metals                     = database.Column(database.Integer)
    fighters                   = database.Column(database.Integer)