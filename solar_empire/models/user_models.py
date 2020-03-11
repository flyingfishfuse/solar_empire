import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *


class User(database.Model):
    __tablename__   = USER_TABLE_NAME
    login_id        = database.Column(database.Integer, primary_key=True)
    user_id         = database.Column(database.Integer)
    username        = database.Column(database.String(64), index=True, unique=True)
    email           = database.Column(database.String(120), index=True, unique=True)
    password_hash   = database.Column(database.String(128))
    location        = database.Column(database.String(128))
    max_turns       = database.Column(database.Integer)
    turns_run       = database.Column(database.Integer)
    safe_turns_left = database.Column(database.Integer)
    cash_available  = database.Column(database.Integer)
    on_planet       = database.Column(database.Boolean)
    pocket_space    = database.Column(database.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)

#fuck I love python... you PUT THE USER
## IN THE SHIP!
class UserShip(User):
    ship_id                    = database.Column(database.Integer,primary_key=True)
    ship_type                  = database.Column(database.Integer)
    ship_name                  = database.Column(database.String(128))
    class_abbreviation         = database.Column(database.String(128))
    fighter_type               = database.Column(database.Integer)
    fighter_count              = database.Column(database.Integer)
    cargo_bay_size             = database.Column(database.Integer)
    size                       = database.Column(database.Integer)
    clan_id                    = database.Column(database.Integer) 
    ship_class                  = database.Column(database.String(128)) 
    class_name                 = database.Column(database.String(128))

    fighters_max               = database.Column(database.Integer)    
    mine_rate_metal            = database.Column(database.Integer)
    mine_rate_fuel             = database.Column(database.Integer)
    move_turn_cost             = database.Column(database.Integer)
    point_value                = database.Column(database.Integer)
    num_ot                     = database.Column(database.Integer)
    num_dt                     = database.Column(database.Integer)
    num_pc                     = database.Column(database.Integer) 
    # Manifest is a serialized dict of :+
    #    {"equipment_name" : "number_of_units"}
    cargo_manifest             = database.Column(database.PickleType)
    location                   = database.Column(database.String(128))
    configuration              = database.Column(database.String(128))
    equipment                  = database.Column(database.PickleType)
    damage_taken               = database.Column(database.Integer)
    shields_max                = database.Column(database.Integer)
    shields_current            = database.Column(database.Integer)
    hull_max                   = database.Column(database.Integer)
    hull_current               = database.Column(database.Integer)
    #special weapons
    #shots
    quark                      = database.Column(database.Integer)
    black_hole_gun             = database.Column(database.Integer)
    #time
    nova_wave_time             = database.Column(database.Integer)