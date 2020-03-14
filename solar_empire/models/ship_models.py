import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *

class GenericShip(UserShip):

    #ship_type_giant            = database.relationship('GiantShip', backref='GenericShip' , lazy=True)
    #ship_type_huge             = database.relationship('HugeShip', backref='GenericShip' , lazy=True)
    #ship_type_capital          = database.relationship('CapitalShip', backref='GenericShip' , lazy=True)
    #ship_type_medium           = database.relationship('MediumShip', backref='GenericShip' , lazy=True)
    #ship_type_small            = database.relationship('SmallShip', backref='GenericShip' , lazy=True)
    #ship_type_pod              = database.relationship('PodShip', backref='GenericShip' , lazy=True)
    ship_id                     = database.Column(database.Integer, primary_key = True, unique=True, autoincrement=True)

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

class SmallShip(GenericShip):
    pass

class PodShip(GenericShip):
    pass

class Brobdingnagian(GiantShip):
    pass

class TerraMaelstrom(GiantShip):
    pass
