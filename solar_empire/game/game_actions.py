import solar_empire
from solar_empire import *
from solar_empire.inc.configuration_options import *
from solar_empire.universe_build.generator_functions import *

from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
from solar_empire.models.social_models import *
from solar_empire.models.storekeeper_models import *
from solar_empire.models.resource_models import *
from solar_empire.models.equipment_models import *
from solar_empire.models.system_models import *

def add_resources_to_player(user_id, resource_type, resource_amount):
    user_to_mod = database.query(User).filter_by(User.user_id).first()
    if resource_type   == 'minerals':
        user_to_mod.minerals = resource_amount
    elif resource_type == 'technology':
        user_to_mod.technology = resource_amount
    elif resource_type == 'metals':
        user_to_mod.metals = resource_amount
    elif resource_type == 'fuel':
        user_to_mod.fuel = resource_amount
    elif resource_type == 'fighters':
        user_to_mod.fighters = resource_amount
    elif resource_type == 'organics':
        user_to_mod.organics = resource_amount

#returns a list of the ship_types
def load_ship_types():

def return_game_var(var):
    return GameVars.query.filter_by(var)

def grab_starport_name():
	return names.gen_name()

def return_planet_by_id(planet_id):
    database.query(PlanetInfo.planet_id)

def add_to_db(thingie):
    """
    Takes SQLAchemy Class_model Objects like NEW USERS and SHIPS
    For updating changes to Class_model.Attribute using the form:

    Class_model.Attribute = some_var 
    
    for USERS: change_user_var(user_id, var, value)
    for SHIPS: change_ship_var(ship_id, var, value)
    for UNIV : change_game_var(var, value)
    """
    database.session.add(thingie)
    database.session.commit

def update_db():
    database.session.commit()

def change_game_var(the_var , new_value):
    current_value            = return_game_var(the_var)
    new_game_variable_value  = 

def hit_the_brakes():
    #game already paused
    if return_game_var('is_game_paused') == True:



def game_status():
    if request.method == 'POST' and Request.form.post('oven_timer'):
        make_systems()
        add_planets()
        add_starports()
        add_blackmarkets()
        place_resources()
    elif request.method == 'POST' and Request.form.post('pause_button'):
        hit_the_brakes
    elif request.method == 'POST' and Request.form.post('give_minerals'):
        resource_type = Request.form.post('resource_type')
        amount        = Request.form.post('amount')
        player        = Request.form.post('player')
        add_resources(player, resource_type, amount)
    return render_template('game_status.html')

def bilkos_blackmarket_shop():
    return render_template('bilkos.html')

def pause():
#(un)pause
	if return_game_var('paused') == False:
		out = "Game Paused<p>"
		post_news("Game Paused")
		insert_history(user.username,"Paused Game+")
	 elif return_game_var('paused') == True
		post_news("Game Un-Paused")
		out = "Game Un-paused+<p>"
		insert_history(user.username , "Unpaused Game+")