import solar_empire
import solar_empire.models
from solar_empire import *
from solar_empire.models import *

from datetime import datetime
from solar_empire.configuration_options import *

def add_resources_to_player_by_id(player_id, resource_type, resource_amount):
	
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


#//post an entry into the news
	#function post_news(headline)
#//function that will send a header correct e-mail, or return failure if it doesn't work
	#function send_mail(myname, myemail, contactname, contactemail, subject, message)

#function takes cash from a player. Admin is exempt.
	#function take_cash($amount)

#take tech support units from a player. Admin is exempt.
	#function take_tech($amount)

#Give tech support units to a player. Admin is exempt.
	#function give_tech($amount)

#/********************
#Message Functions
#*********************/

#sends $text to $to, from global $user
	#function send_message($to,$text)

#function that damages a ship with a specified amount of damage.
#send a negative number as the first arguement to destroy a ship outright.
	#function damage_ship($amount,$fig_dam,$s_dam,$from,$target,$target_ship) {

#set the shields down first off (if needed).
	#target_ship['shields'] 
#DB ships 
#target_ship[ship_id]'");

#take the fighters down next (if needed).
# don't want to hurt the admin now do we?
	#if ( target['login_id'] != ADMIN_ID) {
	#shield_damage = 0;
#set ships_killed
#// ship not destroyed
	#users set last_attack = ".time().", last_attack_by = '$from[login_name]' where login_id = '$target[login_id]'");
#	ships set fighters = fighters - '$amount', shields = shields - '$shield_damage' where ship_id = '$target_ship[ship_id]'");
	#users set fighters_lost = fighters_lost + '$amount' where login_id = '$target[login_id]'");
	#_users set fighters_killed = fighters_killed + '$amount' where login_id = '$from[login_id]'");

#function retire_user($target)
#	post_news("<b class=b1>$target_user[login_name]</b> Retired from the Game.");

#/********************
#Get Information
#*********************/
#// retrieve the star data
	#function get_star()
		#global $user, $star, $db_name;
		#database("select * from {$db_name}_stars where star_id = '$user[location]'");
		#return star 

#//get distance between stars $s1 and $s2
	# get_star_dist($s1,$s2) {
	#"select x_loc,y_loc from ${db_name}_stars where star_id = '$s1' || star_id = '$s2'");
	#star1
	#star2
	#dist = round(sqrt(abs((star1['x_loc'] - star2['x_loc']) * 2) + abs((star1['y_loc'] - star2['y_loc'])*2)))
	#return dist

#function to check if a player is dead and out during sudden death.
#function sudden_death_check($user)
#	if ($numships[0] <= 0) {
#	print_page("Sudden Death", "You have no ship, and this game is Sudden Death. <br>As such you are out of the game. <br>You may still access the Forum, and send/recieve private messages though.");

#Choose a system at random
	#random_system_num()


#/********************
#Create an Escape Pod Function
#*********************/

#//function to create an escape pod
#function create_escape_pod($target)
	#rand_star = random_system_num(); #make a random system number up.
	#ship_types = load_ship_types(); #load ship data
	#ship_stats = $ship_types[2]; #ep is num 2
	#(ship_name, login_id, login_name, shipclass, class_name, class_name_abbr, fighters, max_fighters, max_shields, cargo_bays, mine_rate_metal, mine_rate_fuel, move_turn_cost, location, config,clan_id";
	#values('Escape Pod',target[login_id],
	#target['location'] = $rand_star;


#function that returns a hostile planet checking query
#function attack_planet_check($db_name,$user)
	#return planets where fighter_set = 1 
	#&& fighters > 0 
	#&& login_id != '$user[login_id]' 
	#&& (clan_id != '$user[clan_id]' 
	#&& clan_id != 0) 
	#&& location = '$user[location]' o
	#order by fighter_set desc, fighters desc limit 1";

#load ship types from database.
#function load_ship_types()

#Function to figure out the bonuses offered by weapon upgrades
#function bonus_calc($ship)
	#defensive turret : lvl 1
#	$dam['dt'] = round(330 * (mt_rand(75, 125) / 100)) * $ship['num_dt'];

	#offensive turret : lvl 1
#	$dam['ot'] = round(200 * (mt_rand(80, 120) / 100)) * $ship['num_dt'];

	#silicon armour : lvl 2
#	$dam['sa'] = round($upgrade_sa * (mt_rand(90, 110) / 100)) * $ship['num_sa'];

	#plasma cannon : lvl 2
#	$dam['pc'] = round(420 * (mt_rand(92, 108) / 100)) * $ship['num_pc'];

	#electronic warfare module : lvl 1
#	$dam['ewd'] = round(325 * (mt_rand(85, 115) / 100)) * $ship['num_ew'];
#	$dam['ewa'] = round(225 * (mt_rand(80, 120) / 100)) * $ship['num_ew'];

#	return $dam;

#A function that gets all the details for the user's new ship, and returns the completed user_ship array.
#function userShip($id)

#a function that allows a message to be sent to all players.


#def user_is_admin(id_entity):


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


#function that will create a help-link.
def popup_help(topic, height, width, string = "Info"):
	return '<a href="' + topic + '" onclick="popup(\'' + topic + '\', ' + height + ',' + width + '); return false;">' + string + '</a>'

#prints to a fun little dev console in the admin area
def print_to_console(text_to_console):
	pass

#//makes a ship using the parts specified in $ship_parts (array), ship_owner (also array)
#//returns id of ship inserted.
#function make_ship($ship_parts, $ship_owner)
	

#def gameVars(db_name):


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
#def empty_bays(ship)
#	ship['empty_bays'] = ship['cargo_bays'] - ship['metal'] - ship['fuel'] - ship['elect'] - ship['colon'] - ship['organ']

#/*********************
#Misc Functions
#*********************/

#function that calls many other functions to result in a printed out page..
def print_page(title, text):
	thing_to_print = "<div id='gameMenu'>" + \
		statusBar + \
		"</div>" + "<div id='gameBody'>" + \
		game_data_body + "</div>" + \
		print_footer + \
		text + \
		pageStop(title)


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

