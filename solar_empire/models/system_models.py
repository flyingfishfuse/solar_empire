import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *
#Base  system class
# SOL is system_id 1!!
class SystemInfo(database.Model):
    __tablename__       = 'SystemInfo'
    system_id           = database.Column(database.Integer, primary_key = True, unique=True, autoincrement=True)
    location_id         = database.Column(database.Integer)
    name                = database.Column(database.String(128))
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)
    num_stars           = database.Column(database.Integer)
    navigation_hazard   = database.Column(database.Boolean)
    random_events_level = database.Column(database.Integer)
    # thou shall not say pickle rick
    links               = database.Column(database.PickleType)
    has_wormhole        = database.Column(database.Boolean)
    # system ID of link location
    wormhole            = database.Column(database.Integer)
    
#this is what we make a system with.
#now... should anything inherit this class?
class System(SystemInfo):
    __tablename__       = 'System'
    #system_id           = database.Column(database.Integer, database.ForeignKey('systeminfo.systemid'))
    has_pizza_delivery  = database.Column(database.Boolean)
    has_fighters        = database.Column(database.Boolean)
    has_starport        = database.Column(database.Boolean)
    num_planets         = database.Column(database.Integer)

#neither should starport
class StarPort(database.Model):
    __tablename__       = 'starport'
    starport_id         = database.Column(database.Integer)
    system_id           = database.Column(database.Integer)
    location_id         = database.Column(database.Integer)
    name                = database.Column(database.String(128))
    x_loc               = database.Column(database.Integer)
    y_loc               = database.Column(database.Integer)

#planets shouldnt inherit system
class PlanetInfo(database.Model):
    #planet ID 3 : EARTH
    # 8 reserved Planetoids
    __tablename__           = 'planetinfo'
    planet_id               = database.Column(database.Integer, primary_key = True, unique=True, autoincrement=True)
    system_id               = database.Column(database.Integer)
    name                    = database.Column(database.String(128))
    

class Planet(PlanetInfo):
    #...
    __tablename__           = 'planet'
    #planet_id               = database.Column(database.Integer, database.ForeignKey('planetinfo.planetid'), nullable=False)
    location_id             = database.Column(database.Integer)
    user_id_of_owner        = database.Column(database.Integer)
    has_pizza_delivery      = database.Column(database.Boolean)
    has_port                = database.Column(database.Boolean)
    attack_planet           = database.Column(database.Boolean)
    defense_planet          = database.Column(database.Boolean)

    tech_resources          = database.Column(database.Integer) 
    fuel_resources          = database.Column(database.Integer)
    organic_resource        = database.Column(database.Integer)
    metal_resources         = database.Column(database.Integer)
    mineral_resources       = database.Column(database.Integer)

    population              = database.Column(database.Integer)
    fighter_count           = database.Column(database.Integer)
    shield_amount           = database.Column(database.Integer)

class PlanetPort(PlanetInfo):
    __tablename__           = 'planetport'
    # planet_id               = database.ForeignKey('planetinfo.planetid'), nullable=False)
    user_id_of_owner        = database.Column(database.Integer)
    has_factory             = database.Column(database.Boolean)
    has_mine                = database.Column(database.Boolean)
    has_shield              = database.Column(database.Boolean)
    has_fighters            = database.Column(database.Boolean)
    uses_slaves             = database.Column(database.Boolean)
    tech_resources_mined    = database.Column(database.Integer) 
    fuel_resources_mined    = database.Column(database.Integer)
    organic_resource_mined  = database.Column(database.Integer)
    metal_resources_mined   = database.Column(database.Integer)