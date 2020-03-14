from solar_empire.inc.configuration_options import *
from solar_empire import database

class User(database.Model):
    __tablename__  = 'User'
    user_id       = database.Column(database.Integer,     primary_key = True, unique=True, autoincrement=True)
    username      = database.Column(database.String(64),  index=True, unique=True)
    email         = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128), default = DANGER_STRING)
    turns_run     = database.Column(database.Integer,     default = 0)
    cash          = database.Column(database.Integer,     default = 1000)
    location          = database.Column(database.String(128))
    max_turns         = database.Column(database.Integer)
    turns_run         = database.Column(database.Integer)
    safe_turns_left   = database.Column(database.Integer)
    cash_available    = database.Column(database.Integer)
    on_planet         = database.Column(database.Boolean)
    game_login_count  = database.Column(database.Integer)
    pocket_space      = database.Column(database.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)

#  fuck I love python... you PUT THE USER
## IN THE SHIP!
class UserShip(User):
    __tablename__  = 'UserShip'
    # CHILD OF USER: the primary key must link
    # ID is a "universal" identification for the db, SHIP_ID will be a variable 
    # used locally in the system that that user and ship are interacting in
    #id             = database.Column(database.Integer, primary_key=True)
    # you can either do class inheritance or database relationship linking
    # to accomplish this task... I prefer inheritance.
    # to do this with inheritance you simply need to avoid having conflicting
    # keys in the classes, same issues with inheritance apply as normal.
    # The PRIMARY key that is linked bewteen the two, with a new name, the field you want to inherit, is declared next.
    #user_id                    = database.Column(database.Integer, database.ForeignKey('User.userid'), nullable=False)
    ship_id                    = database.Column(database.Integer)
    ship_name                  = database.Column(database.String(128))
    # list of 1-whatever of ships
    ship_type                  = database.Column(database.Integer)
    # PARENT OF GENERIC SHIP: the clsses must link like this, backref is __tablename__
    #linked_user    = database.relationship('GenericShip',backref='usership',uselist=False)
    class_abbreviation         = database.Column(database.String(128))
    fighter_type               = database.Column(database.Integer)
    fighter_count              = database.Column(database.Integer)
    cargo_bay_size             = database.Column(database.Integer)
    size                       = database.Column(database.Integer)
    clan_id                    = database.Column(database.Integer) 
    ship_class                 = database.Column(database.String(128)) 
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