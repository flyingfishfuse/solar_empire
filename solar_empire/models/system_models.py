import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *
#Base  system class
# SOL is system_id 1!!
class SystemInfo(database.Model):
    name                = database.Column(database.String(128))
    system_id           = database.Column(database.Integer)
    location_id         = database.Column(database.Integer)
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)

#this is what we make a system with.
#now... should anything inherit this class?
class System(SystemInfo):    
    has_pizza_delivery  = database.Column(database.Boolean, default = False)
    has_fighters        = database.Column(database.Boolean)
    has_starport        = database.Column(database.Boolean, default = False)
    navigation_hazard   = database.Column(database.Boolean, default = False)
    num_planets         = database.Column(database.Integer)
    random_events_level = database.Column(database.Integer, default = 0)

#neither should starport
class StarPort(database.Model):
    name                = database.Column(database.String(128))
    system_id           = database.Column(database.Integer)
    location_id         = database.Column(database.Integer)
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)

#planets shouldnt inherit system
class PlanetInfo(database.Model):
    #planet ID 3 : EARTH
    # 8 reserved Planetoids
    planet_id               = database.Column(database.Integer)
    planet_num              = database.Column(database.Integer)
    system_id               = database.Column(database.Integer)
    location_id             = database.Column(database.Integer)
    name                    = database.Column(database.String(128))

class Planet(PlanetInfo):
    #...
    user_id_of_owner        = database.Column(database.Integer)
    has_pizza_delivery      = database.Column(database.Boolean, default = False)
    has_port                = database.Column(database.Boolean, default = False)
    has_factory             = database.Column(database.Boolean, default = False)
    has_mine                = database.Column(database.Boolean, default = False)
    has_shield              = database.Column(database.Boolean, default = False)
    has_fighters            = database.Column(database.Boolean)
    uses_slaves             = database.Column(database.Boolean, default = False)
    attack_planet           = database.Column(database.Boolean, default = False)
    defense_planet          = database.Column(database.Boolean, default = False)

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