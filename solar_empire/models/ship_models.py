import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *
from solar_empire.models.user_models import UserShip

#ship configs:
# 'battleship'
# 'low_stealth'
class GenericShip(UserShip):
    class_abbreviation         = database.Column(database.String(128))
    fighter_type               = database.Column(database.Integer)
    fighter_count              = database.Column(database.Integer)
    cargo_bay_size             = database.Column(database.Integer)
    size                       = database.Column(database.Integer)
    #ship_type_giant            = database.relationship('GiantShip', backref='GenericShip' , lazy=True)
    #ship_type_huge             = database.relationship('HugeShip', backref='GenericShip' , lazy=True)
    #ship_type_capital          = database.relationship('CapitalShip', backref='GenericShip' , lazy=True)
    #ship_type_medium           = database.relationship('MediumShip', backref='GenericShip' , lazy=True)
    #ship_type_small            = database.relationship('SmallShip', backref='GenericShip' , lazy=True)
    #ship_type_pod              = database.relationship('PodShip', backref='GenericShip' , lazy=True)
    ship_class                 = database.Column(database.String(128)) 
    class_name                 = database.Column(database.String(128))
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
    configuration              = database.Column(database.String(128))
    equipment                  = database.Column(database.PickleType)
    damage_taken               = database.Column(database.Integer)
    shields_max                = database.Column(database.Integer)
    shields_current            = database.Column(database.Integer)
    hull_max                   = database.Column(database.Integer)
    hull_current               = database.Column(database.Integer)

class GiantShip(GenericShip):
    #ship_brob                = database.relationship('Brobdingnagian', backref='GiantShip' , lazy=True)
    #ship_terra               = database.relationship('TerraMaelstrom', backref='GiantShip' , lazy=True)
    
    pass

class HugeShip(GenericShip):
    pass

class CapitalShip(GenericShip):
    pass

class MediumShip(GenericShip):
    pass

class LightShip(GenericShip):
    pass

class PodShip(GenericShip):
    pass

class Freighter(MediumShip):
    pass

class 

class Brobdingnagian(GiantShip):

    pass

class TerraMaelstrom(GiantShip):

    pass
