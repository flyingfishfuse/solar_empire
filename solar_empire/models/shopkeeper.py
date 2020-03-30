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