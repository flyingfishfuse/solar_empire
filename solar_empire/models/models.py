import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *
from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
from solar_empire.models.social_models import *
from solar_empire.models.storekeeper_models import *
from solar_empire.models.system_models import *
]
#game variables only !



#grid layout
#galactic core	
#clusters
	#number_of_clusters
	#stars_per_cluster
	#size_of_cluster_in_pixels
#ring layout
	#num_deg_between_stars
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
    num_systems                = database.Column(database.Integer, default = 500)
    num_planets                = database.Column(database.Integer, default = 200)
    num_ports                  = database.Column(database.Integer, default = 50)
    num_starports              = database.Column(database.Integer, default = 50)
    num_black_markets          = database.Column(database.Integer, default = 25)
    max_planets_in_system      = database.Column(database.Integer, default = 6)
    map_layout                 = database.Column(database.Integer, default = 1)
    ships_built                = database.Column(database.Integer)
    is_game_paused             = database.Column(database.Boolean)
    logged_in_players_int      = database.Column(database.Integer)
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
    starting_ship              = database.Column(database.Integer, default = 1)



