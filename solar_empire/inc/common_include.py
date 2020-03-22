import solar_empire
import solar_empire.models
from solar_empire import *
from solar_empire.models import *

from datetime import datetime
from solar_empire.inc.configuration_options import *

def return_user_by_id(id_of_user:int):
	"""
	Give this function a USER ID as an INTEGER
	Returns An SQLAlchemy User Class Object for manipulation
	You can do things like this with it:
	
	return_object = return_user_by_id(some_int)
	return_object.attribute = some_var
	update_database()

	"""
	dbquery = database.session.query(User).filter_by(User.user_id = id_of_user)

def return_user_list():
	pass

def return_user_variable(user_id , var):
	user_to_probe = return_user_by_id(user_id) 
	pass

def update_database(thing):
	database.session.add(thing)
	database.commit()
	pass

def add_resources_to_player_by_id(player_id, resource_type, resource_amount):
	
	pass

def return_system_variable(system_id):
	pass

def ask_if_certain():
	pass

def return_game_var(var):
    return GameVars.query.filter_by(var)

def is_game_paused():
    #if (game_info['paused'] == True): 
    #    return "Paused" 
    #else :
        return "Unpaused"

def is_ship_cargo_empty(ship_id):
	#ship_to_inspect = 
    #if (ship_to_inspect.config == None):
    #    return ""
    #elif (ship_to_inspect.config != None):
        return 'blarg'

def set_bounty(user_with_problem, user_in_trouble):
	pass

def add_to_db(thingie):
    database.session.add(thingie)
    database.session.commit

#returns a LIST of all the systems that have been added to the database
def list_of_spawned_systems():
	list_of_systems = System.query.all()
	return list_of_systems

#check to see if a planet already has a port
def planet_has_port(planet):
    found_planet = Planet.query.filter_by(planet_id = planet )
    return found_planet.has_port

#check to see if a system already has a port
def system_has_port(sys_id):
    found_system = System.query.filter_by(system_id = sys_id)
    return found_system.has_starport


#function that calls many other functions to result in a printed out page..
def print_page(title, text):
	thing_to_print = "<div id='gameMenu'>" + \
		statusBar + \
		"</div>" + "<div id='gameBody'>" + \
		game_data_body + "</div>" + \
		print_footer + \
		text + \
		pageStop(title)

#cat time
def date_time_NOW():
	time_now = datetime.now()
	# dd/mm/YY H:M:S
	return time_now.strftime("%d/%m/%Y %H:%M:%S")

def return_blackmarket_name():
	blackmarket_names = [ "Dodgy Dave", "Stinkin Sid", \
				 "Goodie-bag Central", "The Department of Corruption", \
				 "The Ultimate Goodies Store", "Stompin Jim", \
				 "The War Cabinet", "Jim  -Dead Eye- Smarms", \
				 "One Eyed Doyle", "The Ministry of Offence"]
	return blackmarket_names[random.randint(1, len(blackmarket_names))]

def scrolling_output_text(text_string):
	#javascript to scroll the text into view
	pass
#function that will create a help-link.
def popup_help(topic, height, width, string = "Info"):
	return '<a href="' + topic + '" onclick="popup(\'' + topic + '\', ' + height + ',' + width + '); return false;">' + string + '</a>'

#prints to a fun little dev console in the admin area
def print_to_console(text_to_console):
	pass

#//function used to work out players scores
def score_func(login_id,full):
#Listed below are all of the score methods, and some info on them.
#0 = Scores are off.
#1 = (fighter kills + (ship kills * 10)) - (fighter kills * 0.75 + (ship kills *5))
#2 = ship points killed - (ship points lost * 0.5)
#3 = total value (ship/planet fighters plus ship point value)
#4 = ultimate score. takes everything into account.
#	//determines if admin is updateing all scores, or an individual players score is being updated.
	if (full != 1): 
		#database_results =  where name = 'score_method'
		alpha_var = database_results
		score_method = alpha_var['value']
		extra_text = "login_id = 'login_id'"
		plan_text = "login_id = 'login_id'"
	else :
		and_text = " && "
		extra_text = plan_text = "login_id != " . ADMIN_ID

	#scoring method, whereby only kills,are taken into account.
	if(score_method==1):
		#users set score = (fighters_killed + (ships_killed * 10)) - (fighters_lost * 0.75 + (ships_lost * 5)) where ".extra_text);
	 #takes into account ships lost, ships killed, fighters lost, fighters killed.
		asdf = "asdf"
	elif(score_method == 2):
		#"update {db_name}_users set score = ships_killed_points - (ships_lost_points * 0.5) where ".extra_text);
		#total fiscal value score.
		asd = print("asdf")
	elif (score_method == 3):
		#"select sum(fighters) + sum(point_value), login_id from {db_name}_ships where ".extra_text." GROUP BY login_id");
		#"select sum(fighters), login_id from {db_name}_planets where ".plan_text." GROUP BY login_id");
		print ("asdf")
	else:
		ship_array = database_results()
		plan_array = database_results()
		ship_array[0] += plan_array[0]
		#update {db_name}_users set score = 'ship_array[0]' where login_id = 'login_id'")

#//post an entry into the news
	#function post_news(headline)

#send a negative number as the first arguement to destroy a ship outright.
#function damage_ship($amount,$fig_dam,$s_dam,$from,$target,$target_ship) {
#set the shields down first off (if needed).
#take the fighters down next (if needed).
#set ships_killed

#//get distance between stars $s1 and $s2
	# get_star_dist($s1,$s2) {
	#"select x_loc,y_loc from ${db_name}_stars where star_id = '$s1' || star_id = '$s2'");
	#star1
	#star2
	#dist = round(sqrt(abs((star1['x_loc'] - star2['x_loc']) * 2) + abs((star1['y_loc'] - star2['y_loc'])*2)))
	#return dist

#/********************
#Create an Escape Pod Function
#*********************/

def discern_size (size):
	if (size == 1):
		return "Tiny"
	elif(size == 2):
		return "Very Small"
	elif(size == 3):
		return "Small"
	elif(size == 4):
		return "Medium"
	elif(size == 5):
		return "Large"
	elif(size == 6):
		return "Very Large"
	elif(size == 7):
		return "Huge"
	elif(size == 8):
		return "Gigantic"

msgColours = { 	'blue'   : '0000FF', \
				'lime'   : '00FF00', \
				'green'  : '00CC00', \
				'red'    : 'FF0000', \
				'black'  : '000000', \
				'white'  : 'FFFFFF', \
				'yellow' : 'FFFF00', \
				'cyan'   : '00FFFF', \
				'pink'   : 'FF00FF', \
				'purple' : 'CC66CC', \
				'orange' : 'FFCC00' }

smileTypes = ['happy', 'mad'   , 'sad', \
			  'surp' , 'tongue', 'wink', \
			  'oh'   , 'unsure', 'cool', \
			  'laugh', 'blush' , 'sealed']

smileSets = [ '', 'war', 'cow', 'pirate', 'evil']

#//function to figure out the size of a ship in textual terms
def discern_size (size):
	if (size == 1):
		return "Tiny"
	elif(size == 2):
		return "Very Small"
	elif(size == 3):
		return "Small"
	elif(size == 4):
		return "Medium"
	elif(size == 5):
		return "Large"
	elif(size == 6):
		return "Very Large"
	elif(size == 7):
		return "Huge"
	elif(size == 8):
		return "Gigantic"


#//makes a ship using the parts specified in $ship_parts (array), ship_owner (also array)
#//returns id of ship inserted.
#function make_ship($ship_parts, $ship_owner)
#/********************
#Calculating Functions
#*********************/
#	if($score_method==1){ //scoring method, whereby only kills,are taken into account.
#		dbn("update ${db_name}_users set score = (fighters_killed + (ships_killed * 10)) - (fighters_lost * 0.75 + (ships_lost * 5)) where ".$extra_text);
#	} elseif($score_method == 2){ //takes into account ships lost, ships killed, fighters lost, fighters killed.
#		dbn("update ${db_name}_users set score = ships_killed_points - (ships_lost_points * 0.5) where ".$extra_text);
#	} elseif($score_method == 3){ //total fiscal value score.
#		db("select sum(fighters) + sum(point_value), login_id from ${db_name}_ships where ".$extra_text." GROUP BY login_id");
#		db2("select sum(fighters), login_id from ${db_name}_planets where ".$plan_text." GROUP BY login_id");
#		if($full == 1){
#//function to figure out how many empty cargo bays there are on the ship.



