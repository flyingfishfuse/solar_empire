import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *
from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
from solar_empire.models.social_models import *
from solar_empire.models.storekeeper_models import *
from solar_empire.models.system_models import *

class Shopkeeper(database.Model):
    shop_id               = database.Column(database.Integer)
    
class Store(database.Model):
    __tablename__              = "base store class"
    store_id                   = database.Column(database.Integer, primary_key=True)

class Bilkos(Store):
    pass

class BlackMarket(Store):
    blackmarket_id            = database.Column(database.Integer)
    name                       = database.Column(database.String(128))
    location                   = database.Column(database.Integer)
