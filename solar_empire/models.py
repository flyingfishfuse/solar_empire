import solar_empire
from solar_empire import database
from solar_empire.configuration_options import *

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
    cash_available  = database.Column(database.Integer)
    on_planet       = database.Column(database.Boolean)
    pocket_space    = database.Column(database.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)

#fuck I love python... you PUT THE USER
## IN THE SHIP!
class UserShip(User):
    ship_id                    = database.Column(database.String(128))
    ship_type                  = database.Column(database.String(128))
    ship_name                  = database.Column(database.String(128))
    class_abbreviation         = database.Column(database.String(128))
    fighter_type               = database.Column(database.Integer)
    fighter_count              = database.Column(database.Integer)
    cargo_bay_size             = database.Column(database.Integer)
    size                       = database.Column(database.Integer)
    clan_id                    = database.Column(database.Integer) 
    shipclass                  = database.Column(database.String(128)) 
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

class PublicPost(database.Model):
    time                       = database.Column(database.String(128))
    content                    = database.Column(database.String(528))
    user_id                    = database.Column(database.String(128))

class ClanPost(database.Model):
    clan                       = database.Column(database.String(128))
    time                       = database.Column(database.String(128))
    content                    = database.Column(database.String(528))
    user_id                    = database.Column(database.String(128))

#grid layout
#galactic core	
#clusters
	#number of clusters
	#stars per cluster
	#size of cluster in pixels
#ring layout
	#number of degrees between each star
#layered rings layout
	#single ring
	#2 rings
	#30% of the stars go into the first ring.
	#the rest of the stars (minus Sol).
	#10% of the stars go into the first ring.
#MAP_LAYOUT GAME VARIABLE
# GOES FROM 1-6 with INTEGERs

class GameVars(database.Model):
    score_method               = database.Column(database.Integer, default = 1)
    mineral_total              = database.Column(database.Integer, default = 1)
    metal_total                = database.Column(database.Integer, default = 1)
    organic_total              = database.Column(database.Integer, default = 1)
    #let us NOT get into complex economics here
    # we are limiting the cash and everything else is trade/production
    money_total                = database.Column(database.Integer, default = 1)
    mineral_total              = database.Column(database.Integer, default = 1)
    size                       = database.Column(database.Integer, default = 1000)
    num_systems                = database.Column(database.Integer, default = 200)
    num_planets                = database.Column(database.Integer, default = 100)
    num_ports                  = database.Column(database.Integer, default = 50)
    num_starports              = database.Column(database.Integer, default = 50)
    num_black_markets          = database.Column(database.Integer, default = 25)
    max_planets_in_system      = database.Column(database.Integer, default = 6)
    map_layout                 = database.Column(database.Integer, default = 1)
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
    #turns required to attack per round? set to 30?
    sv_turns                   = database.Column(database.Integer)
    #we allowing the quark disruptor?
    quark                      = database.Column(database.Boolean)
    quark_damage               = database.Column(database.Integer, default = QUARK_DAMAGE)
    turns_before_planet_attack = database.Column(database.Integer)
    # is planet attacking allowed?
    flag_planet_attack         = database.Column(database.Boolean)
    random_events              = database.Column(database.Integer)

class SystemInfo(database.Model):
    name                = database.Column(database.String(128))
    system_id           = database.Column(database.Integer)
    location_id         = database.Column(database.Integer)
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)

class System(SystemInfo):    
    has_pizza_delivery  = database.Column(database.Boolean, default = False)
    has_fighters        = database.Column(database.Boolean)
    has_starport        = database.Column(database.Boolean, default = False)
    navigation_hazard   = database.Column(database.Boolean, default = False)
    num_planets         = database.Column(database.Integer)

class StarPort(database.Model):
    name                = database.Column(database.String(128))
    system_id           = database.Column(database.Integer)
    location_id         = database.Column(database.Integer)
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)

class PlanetInfo(database.Model):
    #planet ID 1 : EARTH
    planet_id               = database.Column(database.Integer)
    planet_num              = database.Column(database.Integer)
    name                    = database.Column(database.String(128))
    location_id             = database.Column(database.String(128))
    user_id_of_owner        = database.Column(database.Integer)


class Planet(PlanetInfo):
    #...
    has_pizza_delivery      = database.Column(database.Boolean, default = False)
    has_port                = database.Column(database.Boolean, default = False)
    has_factory             = database.Column(database.Boolean, default = False)
    has_mine                = database.Column(database.Boolean, default = False)
    has_shield              = database.Column(database.Boolean, default = False)
    has_fighters            = database.Column(database.Boolean)
    uses_slaves             = database.Column(database.Boolean, default = False)

    tech_resources          = database.Column(database.Integer) 
    fuel_resources          = database.Column(database.Integer)
    organic_resource        = database.Column(database.Integer)
    metal_resources         = database.Column(database.Integer)
    mineral_resources       = database.Column(database.Integer)

    population              = database.Column(database.Integer)
    fighter_count           = database.Column(database.Integer)
    shield_amount           = database.Column(database.Integer)

class PlanetPort(PlanetInfo):
    tech_resources_mined    = database.Column(database.Integer) 
    fuel_resources_mined    = database.Column(database.Integer)
    organic_resource_mined  = database.Column(database.Integer)
    metal_resources_mined   = database.Column(database.Integer)

class Weapons(database.Model):
    name_cost = "asdf"

class Equipment(database.Model):
    name_cost = "asdf"

class SpecialWeapons(database.Model):
    allowed = "asdf"

class TechResources(database.Model):
    price = "asdf"

class OrganicResources(database.Model):
    price = "asdf"

class MetalResources(database.Model):
    price = "asdf"

class FuelResources(database.Model):
    asdf = "asdf"
