import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *

class TechResources(database.Model):
    price             = database.Column(database.Integer)

class OrganicResources(database.Model):
    price             = database.Column(database.Integer)

class MetalResources(database.Model):
    price             = database.Column(database.Integer)

class FuelResources(database.Model):
    asdf              = database.Column(database.Integer)
