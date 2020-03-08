import solar_empire
from solar_empire import database

class User(database.Model):
    login_id        = database.Column(database.Integer, primary_key=True)
    username        = database.Column(database.String(64), index=True, unique=True)
    email           = database.Column(database.String(120), index=True, unique=True)
    password_hash   = database.Column(database.String(128))
    ship_id         = database.Column(database.String(128))
    location        = database.Column(database.String(128))
    turns           = database.Column(database.Integer)
    turns_run       = database.Column(database.Integer)
    safe_turns_left = database.Column(database.Integer)
    cash            = database.Column(database.Integer)
    on_planet       = database.Column(database.Boolean)
    pocket_space    = database.Column(database.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.username)

#fuck I love python... you PUT THE USER
## IN THE SHIP!
class UserShip(User):
    ship_id          = database.Column(database.String(128))
    ship_type        = database.Column(database.String(128))
    fighter_type     = database.Column(database.String(128))
    fighter_count    = database.Column(database.String(128))
    cargo_bay_size   = database.Column(database.String(128))
    # Manifest is a serialized dict of :+
    #    {"equipment_name" : "number_of_units"}
    cargo_manifest   = database.Column(database.PickleType)
    location         = database.Column(database.String(128))
    configuration    = database.Column(database.String(128))
    equipment        = database.Column(database.String(128))

class PublicPost(database.Model):
    time = database.Column(database.String(128))
    content = database.Column(database.String(528))
    user_id = database.Column(database.String(128))

class ClanPost(database.Model):
    clan = database.Column(database.String(128))
    time = database.Column(database.String(128))
    content = database.Column(database.String(528))
    user_id = database.Column(database.String(128))

class GameVars(database.Model):
    score_method               = database.Column(database.Integer)
    ships_built                = database.Column(database.Integer)
    is_game_paused             = database.Column(database.Boolean)
    logged_in_players          = database.Column(database.Integer)
    logged_out_players         = database.Column(database.Integer)
    ships_destroyed            = database.Column(database.Integer)
    clans                      = database.Column(database.Integer)
    global_safe_turns_left     = database.Column(database.Integer)
    newbies_left               = database.Column(database.Integer)
    sudden_death               = database.Column(database.Boolean)
    sudden_death_turns_feft    = database.Column(database.Integer)
    are_we_political           = database.Column(database.Boolean)
    game_name                  = database.Column(database.String(128))
    sv_turns                   = database.Column(database.Integer)
    #we allowing the quark disruptor?
    quark                      = database.Column(database.Boolean)
    turns_before_planet_attack = database.Column(database.Integer)
    # is planet attacking allowed?
    flag_planet_attack         = database.Column(database.Boolean)

class SystemInfo(database.Model):
    asdf = "asdf"

class PlanetInfo(database.Model):
    #planet ID 1 : EARTH
    planet_id        = database.Column(database.Integer)
    planet_num       = database.Column(database.Integer)  
    name             = database.Column(database.String(128))
    x_loc            = database.Column(database.Integer)
    y_loc            = database.Column(database.Integer)
    location         = database.Column(database.String(128))
    user_id_of_owner = database.Column(database.Integer)
    tech_resources   = database.Column(database.Integer) 
    fuel_resources   = database.Column(database.Integer)
    organic_resource = database.Column(database.Integer)
    metal_resources  = database.Column(database.Integer)
    population       = database.Column(database.Integer)
    has_fighters     = database.Column(database.Boolean)
    fighter_count    = database.Column(database.Integer)