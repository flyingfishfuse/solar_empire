#!/usr/bin/python3
import solar_empire
from solar_empire.models import *
from solar_empire.inc.common_include import *
from solar_empire import database
from solar_empire.inc.configuration_options import *
from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
from solar_empire.models.social_models import *
from solar_empire.models.storekeeper_models import *
from solar_empire.models.system_models import *

#generic link to go back to the start system
system_view = "<p><a href='location'>Back to the Star System</a><br>"
admin_view = "<p><a href=admin.php>Back to Admin Page</a>"


def update_bounty_list(user_id):

	pass

def change_user_variable(user_id, var, value):
	user_to_modify = return_user_by_id(user_id)
	database.query(User).filter_by(User.user_id == user_to_modify).update({var,value})

def does_user_have_ship(user_id):
	if UserShip.query.filter_by(user_id).first() != None:
		return True
	else:
		return False

def user_ship_for_info(user_id):
	if does_user_have_ship(user_id):
		pass
	else:
		pass
def return_usership_by_userid(user_id):
	database.session.query(UserShip).all().filter_by(UserShip.user_id)

def return_user_location(userid:int):
	blarp = database.session.query(User).filter_by(User.user_id == userid).all()
	return blarp.location

def return_userfleet_by_userid(user_id:int):
	"""
	Returns the fleet (if any) of a user.
	this is stored as an array in the UserShip model as UserShip.fleet_array
	Remember, these can be gigantic ships, they are just being towed by C&C fleet AI 
	"""
	return database.session.query(UserShip.fleet_array)
def return_user_ship_variable(user_id , var):
	if does_user_have_ship(user_id):
		usership = user_ship_for_info(user_id)
		#usership_var = usership
	else:
		return False
########################################
#	Need another file for the following
# weapons and transportation actions
#######################################
def wormhole_playership(ship_id, location):
	pass

def buy_basic_upgrade(user_id, \
					  upgrade, \
					  cash_cost , \
					  mineral_cost, \
					  metal_cost, \
					  fuel_cost, \
					  tech_cost):
	user_to_modify         = return_user_by_id(user_id)
	user_to_modify.cash    = return_user_variable(user_id , 'cash') - cash_cost
	user_to_modify.mineral = return_user_ship_variable(user_id , 'mineral') - mineral_cost
	user_to_modify.fuel    = return_user_ship_variable(user_id , 'fuel') - fuel_cost
	user_to_modify.metal   = return_user_ship_variable(user_id , 'metal') - metal_cost
	update_database()

def set_bounty(user_with_bounty, user_with_money, comission_percent:int, amount:int):
	"""
	Takes USER ID's and an INTEGER, not a decimal "0.1" or similar for percents
	This function gets used in black markets only
	"""
	cost               = round((amount /100) * comission_percent) + amount + 1
	wanted_man         = return_user_by_id(user_with_bounty)
	asshole            = return_user_by_id(user_with_money)
	update_bounty_list(user_with_bounty, bounty)
	pass


def inject_money(amount: int, player_id: int, all_players: bool):
#give players money
	if all_players == True:
		print_page('How much money do you want to give to each player?')
		print_page("Gave :} credits to all players".format(amount))
	elif all_players == False:
		print_page("Player's money reserves increased by <b>:}</b><br>Note: \
			This has NOT sent a message to the players+ That is your job\
			<br><br>".format(amount))
		dude = return_user_by_id(player_id)
		dude.cash = dude.cash + amount
		update_database()
	
def make_basic_upgrade (user: int, upgrade: str, increase_amount: int, cost: int) :
#def for adding 'normal' upgrades to a ship.
	player    = return_user_by_id(user)
	user_ship = return_usership(user)
	if user.cash < cost:
		print_page("You can not afford any of the Basic Upgrades.<p>")
	elif user_ship.upgrades < 1:
		print_page("")
	else:
		user.cash = user.cash - cost
		user_ship.upgrades - 1
		if upgrade == "cargo_bays" :
			user_ship.empty_bays + increase_amount
	print_page("You have increased the <b class=b1>:user_ship.ship_name}s</b> :upgrade_str} capacity by <b>:inc_amount}</b> for <b>:cost}</b> Credits. <p>")


#/********************
#Account updating functions
#*********************/

def charge_turns(amount, user_id):
	"""
	function that charges turns for something. Admin is exempt.
	"""
	user = return_user_by_id(user_id)
	if user.login_id != ADMIN_USER_ID :
		user.turns_left - amount
		user.turns_run + amount

def get_all_ships_system(system_id):
	pass

def get_all_ships_planet(planet_id):
	pass

def give_cash(user_id, amount):
	pass

def take_cash(user_id:int, amount:int):
	"""
	function takes cash from a player. Admin is exempt.
	"""
	pass

def take_tech(userid:int, amount:int):
	pass

def remove_resource_from_player(user_id, resource, amount):
	pass

def add_resource_to_player(user_id, resource, amount):
	pass

def kill_shields(user_id):
	pass

def kill_fighters():
	pass


def damage_ship(amount, fig_dam, s_dam, attacker, target , target_ship):
	"""
	function that damages a ship with a specified amount of damage.
	send a negative number as the first arguement to destroy a ship outright.
	"""
	#set the shields down first off (if needed).
	#take the fighters down next (if needed).
	# don't want to hurt the admin now do we?
	#shield_damage = 0
	#set ships_killed
	## ship not destroyed


#function retire_user(target)
#post_news("<b class=b1>target_user[login_name]</b> Retired from the Game.")
#function to check if a player is dead and out during sudden death.
	#sudden_death_check(user)
#Choose a system at random
	#random_system_num()
##function to create an escape pod
	#function create_escape_pod(target)
		#rand_star = random_system_num() #make a random system number up.
#function that returns a hostile planet checking query
	#function attack_planet_check(db_name,user)
#load ship types from database.
	#function load_ship_types()
#Function to figure out the bonuses offered by weapon upgrades
	#function bonus_calc(ship)
#A function that gets all the details for the user's new ship, and returns the completed user_ship array.
#function userShip(id)
#a function that allows a message to be sent to all players.
def show_active(): 
	"""
	active user listing
	"""
	active_users = database.session.query(User).filter_by(User.active).all()
	title_string = "Users that have logged with within the past 5 mins+"
	time_string = "<br>Time Loaded::timeNOW}<br><a href=admin?show_active=1>Reload</a>".format(date_time_NOW)
	out = ""
	for player in active_users:
 		active_players = UserShip.query.filter_by('active').all()
		if active_players == []:
			out + "<p>There are no active users+"
			out + "<p><table>"
			out + "<tr bgcolor='#555555'><td>Login Name</td><td>Last Request</td></tr>"
			out + "<tr bgcolor='#333333'><td>"+ player.username + "</td><td>" + date_time_NOW + player.last_request + \
				"</td><td> - <a href=message+php?target=player[login_id]>Message</a><br></td></tr>"
			out + "</table>"
	rs = "<p><a href=admin+php>Back to Admin Page</a>"
	print_page("Active Users",out)

def	make_standard_upgrade(userid:int, upgrade_str, config_addon, cost, developement_id:int , tech_cost:int = 0):
	"""
	a function to allow for easy addition of upgrades.
	#This function will select fill as many ships in a fleet as possible with whatever is requested.
	1st arguement sent to it is the sql name for whatever is to be loaded.
	2nd arguement is the name of the sql entry for the most of that material that any one ship can hold.
	3rd arguement contains the textual string
	4th arguement holds the cost per unit of the item.
	5th arguement is the name of the orginating script

	"""
	user_to_mod     = return_user_by_id(userid)
	if does_user_have_ship == True:
		ship_to_display = return_usership_by_userid(user_to_mod.user_id)
	else:
		print_page("lol") 
	if ( user_to_mod.cash < cost):
		return "You can not afford to buy a <b class=b1>upgrade_str</b>.<p>"
	elif ( user_to_mod.tech < tech_cost and tech_cost > 0):
		return "Ignorant Planet Dweller. You don't have enough tech points.<p>"
	elif (ship_to_display.config, config_addon) != false:
		return "Your ship is already equipped with a <b class=b1>upgrade_str</b>.<br>There is no point in having more than one on a ship.<p>"
	elif (ship_to_display.upgrades < 1):
		return ""
	else :
		take_cash(cost)
		take_tech(user_to_mod.user_id , tech_cost)
		ship_to_display.config.update(config_addon)
		#update db_name    ships set config = '
		# user_ship[config] ', 
		# upgrades = upgrades - 1 where ship_id = 'user[ship_id]'")
		return "<b class=b1>upgrade_str</b>, purchased and fitted to the <b class=b1>"
		#user_ship[ship_name]</b> for <b>cost</b> Credits.<p>"

def fill_fleet(userid , item_sql, item_max_sql, item_str, item_cost, script_name, cargo_run = 0):
	#taken = 0 #item taken from earth far.
	#ship_counter = 0 #ships passed through
	user_to_mod = return_user_by_id(userid)
	ships       = 
	item_id		= return_item_by_id(item_str)
	item_cost	= "TODO"
	ret_str     = ""
	if cargo_run == 1: ##cargo
		print("lol")
	else : ##not cargo
		print("lol")
#	#elect all viable ships
	#insufficient cash
	if (user_to_mod.cash < item_cost):
		ret_str + "You do not have enough money for even 1 unit of <b class=b1>item_str</b>. You certainly can't afford to fill a fleet."
	elif (maths['total_ships'] < 1): #ensure there are some ships.
		ret_str + "This operation failed as there are no ships that have any free capacity to hold <b class=b1>item_str</b> in this system that belong to you."
	else :
		##work out the total value of them all.
		total_cost = [total_capacity * item_cost]
		#user CAN afford to fill the whole fleet
		if ( total_cost <= user_to_mod.cash) :
			if empty(sure): #confirmation
				get_var('Load ships',script_name,"There is capacity for <b>maths[total_capacity]</b> <b class=b1>item_str</b> in <b>maths[total_ships]</b> ships in this system. <p>You have enough money to fill all the ships with <b class=b1>item_str</b>. Do you wish to do that?",'sure','yes')
			else : #process.
				take_cash(total_cost)
				if  cargo_run == 0: #not cargo bay stuff
					user_ship[item_sql] = user_ship[item_max_sql]
				else : #cargo bay stuff
					user_ship[item_sql] += ship_to_display.empty_bays
				ret_str + "<b>maths[total_capacity]</b> <b class=b1>item_str</b> were added to <b>maths[total_ships]</b> ships.<br>All ships are now at maximum capacity."
		#user CANNOT afford to fill the whole fleet, so we'll have to do it the hard way.
		else :
			total_can_afford = user_to_mod.cash / item_cost #work out amount can afford.
			if sure : #confirmation
				extra_text = "<p><input type=radio name=fill_dir value=1 CHECKED> - Fill highest capacity ships ships first."
				extra_text + "<br><input type=radio name=fill_dir value=2> - Fill lowest capacity ships first."
				get_var('Load ships',script_name,"There is capacity for <b>maths[total_capacity]</b> <b class=b1>item_str</b> in <b>maths[total_ships]</b> ships in this system. <br>However, you can only afford <b>total_can_afford</b> item_str.<p>Do you want to fill as many ships as you can afford to fill?".extra_text,'sure','yes')
			else : #process
				if fill_dir == 1:
					order_dir = "desc"
				else :
					order_dir = "asc"
					if total_can_afford < 1: #error checking
						print_page("Unable to fill any ships with anything.")
				used_copy_afford = total_can_afford #make copy of the above.
				final_cost = item_cost * total_can_afford #work out the final cash cost of it all.
				fill_ships_sql = "" #intiate sql string to load a bunch of ships at once
				temp_str = ""
				for ships in database.session.query(UserShip).all().filter_by(UserShip.user_id = user_to_mod.user_id): #loop through the ships
					ship_counter = 1 #increment counter
					free_space = ships['max - ships[item_sql] #capacity of present ship

					if ( free_space < used_copy_afford) : #can load ship
						used_copy_afford -= free_space #num to use
						fill_ships_sql + "ship_id = 'ships[ship_id]' or "

						temp_str + "<br><b class=b1>ships[ship_name]</b> had its item_str cargo increased by <b>free_space</b> to maximum capacity."

						if ( ships['ship_id == ship_to_display.ship_id: #do the user ship too.
							if ( cargo_run == 0: #not cargo bay stuff
								user_ship[item_sql] = user_ship[item_max_sql]
							else : #cargo bay stuff
								user_ship[item_sql] += ship_to_display.empty_bays
							
						

					else : #cannot load ship whole ship.
						dbn("update :db_name_ships set item_sql = item_sql + 'used_copy_afford' where ship_id = 'ships[ship_id]'")

						if ( ships['ship_id == ship_to_display.ship_id && cargo_run == 0: #do the user ship too.
							user_ship[item_sql] += used_copy_afford
						 elif  ( ships['ship_id == ship_to_display.ship_id) : #cargo bay stuff
							user_ship[item_sql] += used_copy_afford
						
						temp_str + "<br><b class=b1>ships[ship_name]</b>s <b class=b1>item_str</b> count was increased by <b>used_copy_afford</b>."
						break 1
					
				 #end of while

				ret_str + "<b>ship_counter</b> ships had their <b class=b1>item_str</b> count augmented by more item_str.<br>Total increase in item_str = <b>total_can_afford</b> Cost = <b>final_cost</b><p>More Detailed Statistics :".temp_str

				#update database with fully loaded ships.
				if(!empty(fill_ships_sql):
					fill_ships_sql = preg_replace("/\|\| /", "", fill_ships_sql)
					dbn("update :db_name_ships set item_sql = item_max_sql where ".fill_ships_sql)
				
				take_cash(final_cost) #charge the cash
			
		
	
	return ret_str #return the result string.



#function that will return a list of the contents of the ships cargo bays.
function bay_storage(ship:
	if(empty(ship_type.cargo_bays)) :
		return "\n<b>None</b>"
	
	ret_str = ""
	if(!empty(ship_type.metal)) :
		ret_str + "\n<b>ship[metal]</b> Metals"
	
	if(!empty(ship_type.fuel)) :
		if(!empty(ret_str):
			ret_str + "<br>"
		
		ret_str + "\n<b>ship[fuel]</b> Fuels"
	
	if(!empty(ship_type.organ)) :
		if(!empty(ret_str):
			ret_str + "<br>"
		
		ret_str + "\n<b>ship[organ]</b> Organics"
	
	if(!empty(ship_type.elect)) :
		if(!empty(ret_str):
			ret_str + "<br>"
		
		ret_str + "\n<b>ship[elect]</b> Electronics"
	
	if(!empty(ship_type.colon)) :
		if(!empty(ret_str):
			ret_str + "<br>"
		
		ret_str + "\n<b>ship[colon]</b> Colonists"
	
	empty_bays(ship)
	if ( ship_type.empty_bays > 0) :
		if(!empty(ret_str):
			ret_str + "<br>"
		
		ret_str + "\n<b>ship[empty_bays]</b> Empty"
	
	return ret_str


#function that will work out how many flagships this player has got through.
function num_flagships (num_ships:
	if ( num_ships == 0:
		return 0
	

	result_num = 0
	while(num_ships > 1:
		num_ships = num_ships / 2
		result_num ++
	
	return result_num


?>
