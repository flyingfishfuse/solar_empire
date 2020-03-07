#!/usr/bin/python3
from flask import Flask
from flask import request
from models import User, UserShip
import solar_empire , solar_empire.models

#Get game info if not admin (loaded for admin in check_auth)
if (User.login_id != ADMIN_ID):
	#Get the game information
	database("select * from se_games where db_name = '$db_name'")
    #game_info = dbr(1)

#database("select * from ${db_name}_users where login_id = '$login_id'")
#user = dbr(1)

#database("select * from {$db_name}_user_options where login_id = " + user['login_id'])
#user_options = dbr(1)
# update last request (so as know when user last requested a page in THIS game.
#dbn("UPDATE `{$db_name}_users` SET `last_request` = " + time() + " WHERE `login_id` = " + user['login_id'])
#gameVars(db_name)
# load the ship present usership


#user_ship = userShip(user['ship_id'])

if (user_ship == None & user['ship_id'] != None) :
	database("SELECT `ship_id` FROM `{db_name}_ships` WHERE `login_id` = " + user['login_id'])
	other = dbr(1)

if (other == false): 
    user['ship_id'] = None
    database("UPDATE `{$db_name}_users` SET `ship_id` = NULL WHERE `login_id` = " + user['login_id'])
else :
	user['ship_id'] = other['ship_id']
	user_ship = userShip(user['ship_id'])
	user['location'] = user_ship['location']
	database("UPDATE `{db_name}_users` SET `location` = " + user['location'] + 'WHERE `login_id` = ' + user['login_id'])

#generic link to go back to the start system
system_view = "<p><a href=\"location\">Back to the Star System</a><br>"
#damage capacity of the silicon armour module
upgrade_sa = 750

def is_game_paused():
    if (game_info['paused'] == True): 
        return "Paused" 
    else :
        return "Unpaused"

def is_ship_cargo_empty():
    if (user_ship['config'] == None):
        return ""
    elif (user_ship['config'] != None):
        return user_ship['config']


def statusBar():
    global user, \
        user_ship, \
        count_days_left_in_game, \
        db_name, \
        max_turns, \
        enable_politics, \
        turns_safe, \
        flag_research, \
        max_clans, \
        game_info
    game_menu = "<h1>" + \
                popup_help('game_info?db_name=' + \
                db_name, \
                600, \
                450, \
                game_info['name']) + \
                is_game_paused + \
                "</h1>\n"
    game_menu + "<p>{sstart}{llr_result} active user(s:eend}</p>\n".format( \
            sstart = start , \
            llr_result = lr_result, \
            eend = end )
    game_menu + "<p>" + date_time_NOW  + "</p>\n"
	
    if (game_info['paused'] == True):
        game_menu + "<p>{count_days_left_in_game} days left</p>\n"
        game_menu + "<h2>" + \
                    user['name'] + \
                    user['clan_id'] + \
                    user['clan_sym'] + \
                    user['clan_sym_color'] + "</h2>\n"
	if (user['turns_run'] < turns_safe):
		safe_turns_left = turns_safe - user['turns_run']
		game_menu + "<p><em>{safe_turns_left}</b> safe turn(s) left</em></p>\n".format(safe_turns_left = safe_turns)
	else:
		game_menu + "<p><em>Leaving</em> newbie safety!</p>\n"
		dbn("update ${db_name}_users set turns_run = turns_run + 1 where login_id = '{user[login_id]}'")
		dbn("insert into ${db_name}_messages (timestamp,sender_name, sender_id, login_id, text) \
            values('{current_time}',\
            '{user[login_name]}',\
            '{user[login_id]}',\
            '{user[login_id]}',\
            'You have just left Newbie safety.<p>This means that you are now attackable by any player who can attack. <p>Good Luck.')")
	game_menu + "<table>\n\t<tr>\n\t\t<th>Turns</th>\n\t\t<td>" + \
            user['turns'] + ' / ' + \
            max_turns     + "</td>\n\t</tr>\n\t<tr>\n\t\t<th>Credits</th>\n\t\t<td>" + \
	        user['cash']  + "</td>\n\t</tr>\n"
	if (flag_research != 0):
		game_menu + "\t<tr>\n\t\t<th>Tech Units</th>\n\t\t<td>" + \
		        user['tech'] + "</td>\n\t</tr>\n"

#/**************
#* Print Ship Info
#**************/
	game_menu + "\t<tr>\n\t\t<th>Ships Killed</th>\n\t\t<td> " + \
            user['ships_killed'] + "</td>\n\t</tr>\n\t<tr>\n\t\t<th>Ships Lost</th>\n\t\t<td>" + \
	        user['ships_lost'] + "</td>\n\t</tr>\n\t<tr>\n\t\t<th>Score</th>\n\t\t<td>" + \
	        user['score'] + "</td>\n\t</tr>\n</table>\n"

	if (user['ship_id'] == None):
	   game_menu + "<h2>Your ship is destroyed!</h2>\n"
	else:
	   game_menu + "<h2>" + \
            popup_help('help?popup=1&ship_info=1&shipno=' + \
		    user_ship['shipclass'], 300, 600, \
            user_ship['ship_name']) + "</h2>\n<table>\n\t<tr>\n\t\t" + \
            "<th>Class</th>\n\t\t<td>{user_ship[class_name]}</td>\n\t</tr>\n\t" + \
            "<tr>\n\t\t<th>Fighters</th>\n\t\t<td>" + \
            user_ship['fighters'] + ' / ' + \
            user_ship['max_fighters'] + "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Shields</th>\n\t\t<td>" + \
            user_ship['shields'] + ' / ' + \
		    user_ship['max_shields'] + "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Specials</th>\n\t\t<td>" + \
            is_ship_cargo_empty + "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Cargo Bays</th>\n\t\t<td>"  + \
            bay_storage(user_ship) + "</td>\n\t</tr>\n</table>\n"
# LEFT SIDE	
	game_menu + "<h2>Menu</h2>\n<ul>\n" + \
				"\t<li><a href=\"location\">Star System</a></li>\n" + \
				"\t<li><a href=\"diary\">Fleet Diary</a></li>\n" + \
				"\t<li><a href=\"news\">Game News</a></li>\n"
    
	if (max_clans > 1 or user['login_id'] == ADMIN_ID):
		game_menu + "\t<li><a href=\"clan\">Clan Control</a></li>\n"
	else:
		if (enable_politics):
			game_menu + "\t<li><a href=\"politics\">Politics</a></li>\n"
		game_menu + "\t<li><a href=\"player_stat\">Player Ranking</a></li>\n</ul>\n<ul>\n"
	
	database("select count(message_id) from ${db_name}_messages where login_id = " + user['login_id'])
	watlist(counted) = dbr()
    game_menu + "\t<li><a href=\"mpage\">$counted Msg(s)</a> - <a href=\"message\">Send</a></li>\n"
    database("select count(message_id) as new_messages from {db_name}_messages where timestamp > '{user[last_access_forum]}' && login_id = -1 && sender_id != '$user[login_id]'")
    messg_count_forum = dbr()
    temp_forum_text = ""
    if (messg_count_forum['new_messages'] > 0):
		temp_forum_text = "({messg_count_forum[new_messages]} <a href=/forum?last_time={user[last_access_forum]}&find_last=1>new</a>)"
    game_menu + "\t<li><a href=\"forum\">Forum</a>$temp_forum_text</li>\n"

    if (user['login_id'] == ADMIN_ID or user['login_id'] == OWNER_ID):
        if (user['login_id'] == ADMIN_ID):
			database("select last_access_admin_forum from se_games where db_name = '{db_name}'")
			l_view = dbr()
			time_from = l_view['last_access_admin_forum']
        else:
			time_from = time()
        
        database("select count(message_id) as new_messages from se_central_forum where timestamp > '$time_from'")
        messg_count_forum = dbr()
        adminForumNew = ""
        if (messg_count_forum['new_messages'] > 0):
            adminForumNew = " ({messg_count_forum[new_messages]} <a href=forum?last_time={time_from}&view_a_forum=1>new</a>)"
        
        game_menu + "\t<li><a href=\"forum?view_a_forum=1\">Admin Forum</a> {adminForumNew}</li>\n"
	if (user['login_id'] == ADMIN_ID or user['login_id'] == OWNER_ID):
		game_menu + "\t<li><a href=\"forum?clan_forum=1\">Clan Forums</a></li>\n"
	else :
        if ( user['clan_id'] > 0) :
		    database("select count(message_id) as new_messages from ${db_name}_messages where timestamp > '{user[last_access_clan_forum]}' && \
                    login_id = -5 && \
                    clan_id = '{user[clan_id]}' && \
                    sender_id != '{user[login_id]}'")
		    messg_count_clan_forum = dbr()
		    temp_clan_forum_text_var = ""
        if ( messg_count_clan_forum['new_messages'] > 0):
		    temp_clan_forum_text_var = "({messg_count_clan_forum[new_messages]}<a href=forum?clan_forum=1&\
                                        last_time={user[last_access_clan_forum]}&find_last=1>new</a>)"
		    game_menu + "\t<li><a href=\"forum?clan_forum=1\"><span style=\"color: #" + \
            user['clan_sym_color'] + "\">" + \
            user['clan_sym'] + "</span> Forum</a>{temp_clan_forum_text_var}</li>\n"

    game_menu + "\t<li><a href=\"http://forum.solar-empire.net/\">Global Forum</a></li>\n</ul>\n<ul>\n"

    # admin lower sidebar
    if (user['login_id'] == ADMIN_ID or user['login_id'] == OWNER_ID):
		game_menu + "\t<li><a href=\"admin\">Admin</a></li>\n"
		if (user['login_id'] == OWNER_ID):
			game_menu + "\t<li><a href=\"developer\">Server</a>\n"
    
    game_menu + "\t<li><a href=\"help\">Help</a></li>\n" + \
	       "\t<li><a href=\"options\">Options</a></li>\n"
    
    if (user['login_id'] != ADMIN_ID):
		game_menu + "\t<li><a href=\"logout?logout_single_game=1\">Game List</a></li>\n"
    
    game_menu + "\t<li><a href=\"logout?comp_logout=1\">Logout</a></li>\n</ul>\n"
    return game_menu

#function that can be used create a viable input form. Adds hidden vars.
def get_var(title, page_name, text, var_name, var_default):
	pageStart()
	html_stuff = "<p>{title}</p>".format() + \
        "<form name='{get_var_form}' action='{page_name}' method=\'post\'>"
#flask get and post args processing goes here!!
	input_form = ""
	for each in request.args:
		input_form + "\n<input type=hidden name={key}='{value}'>"
	
	if ( var_name == 'sure'):
		input_form + "\n<input type=hidden name=sure value=yes>";
		input_form + "\n<input type=submit name=submit value=Yes> - <input type='Button' width='30' value='No' onclick=\"javascript: history.back()\">\n</form>";
	elif (var_name == 'passwd' or var_name == 'passwd_verify' or var_name == 'passwd2'):
		input_form + "\n<input type=password name=$var_name value='$var_default' size=20> - "
		input_form + "\n<input type=submit value=Submit>\n</form>"
	elif ( var_name == 'text') :
		input_form + "\n<textarea name=$var_name cols=50 rows=20 wrap=soft>" + var_default + "</textarea>"
		input_form + "\n<p><input type=submit value=Submit></form>"
	else :
		input_form + "\n<input name=$var_name value='$var_default' size=20> - "
		input_form + "\n<input type=submit value=Submit></form>"
	if ( var_name != 'sure'):
		input_form + "\n<script> document.get_var_form.$var_name.focus(); </script>"
	else :
		input_form + "\n<script> document.get_var_form.submit.focus(); </script>"
	pageStop(title)


#/********************
#Account updating functions
#*********************/

#function that charges turns for something. Admin is exempt.
def charge_turns(amount):
	if User.login_id == ADMIN_ID or OWNER_ID:
		return "asdf"
	database. (users set turns = turns - '$amount', turns_run = turns_run + '$amount' where login_id = '$user[login_id]'");
	user['turns'] - amount
	user['turns_run'] + amount
}


//function that can give a user cash. Admin is exempt.
function give_cash($amount)
{
	global $db_name,$user;
	if ($user['login_id'] != ADMIN_ID) {
		dbn("update ${db_name}_users set cash = cash + '$amount' where login_id = '$user[login_id]'");
		$user['cash'] += $amount;
	}
}

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

#a function to allow for easy addition of upgrades.
def	make_standard_upgrade(upgrade_str, config_addon, cost, developement_id, tech_cost = 0):
	if ( user['cash'] < cost):
		return "You can not afford to buy a <b class=b1>$upgrade_str</b>.<p>"

	elif ( user['tech'] < tech_cost and tech_cost > 0):
		return "Ignorant Planet Dweller. You don't have enough tech points.<p>"
	
	elif (user_ship['config'], config_addon) != false:
		return "Your ship is already equipped with a <b class=b1>$upgrade_str</b>.<br>There is no point in having more than one on a ship.<p>"

	elif (user_ship['upgrades'] < 1):
		return "";
	else :
		take_cash(cost);
		take_tech(tech_cost);
		user_ship['config'] + ":" + config_addon;
		#update db_name    ships set config = '
		# user_ship[config] ', 
		# upgrades = upgrades - 1 where ship_id = '$user[ship_id]'");
		return "<b class=b1>$upgrade_str</b>, purchased and fitted to the <b class=b1>
		#user_ship[ship_name]</b> for <b>$cost</b> Credits.<p>";
	}
}


/*
This function will select fill as many ships in a fleet as possible with whatever is requested.

- 1st arguement sent to it is the sql name for whatever is to be loaded.
- 2nd arguement is the name of the sql entry for the most of that material that any one ship can hold.
- 3rd arguement contains the textual string
- 4th arguement holds the cost per unit of the item.
- 5th arguement is the name of the orginating script

*/
function fill_fleet($item_sql, $item_max_sql, $item_str, $item_cost, $script_name, $cargo_run = 0:
	global $user, $user_ship, $db_name, $sure, $fill_dir;

	$ret_str = "";
	$taken = 0; //item taken from earth far.
	$ship_counter = 0; //ships passed through

	if ( cargo_run == 1: //cargo
		$sql_max_check = $item_max_sql;
		$sql_where_clause = " location = '$user[location]' && login_id='$user[login_id]' && $item_max_sql > 0 ";
		$cargo_run = 1;

	else ://not cargo
		$sql_max_check = "($item_max_sql - $item_sql)";
		$sql_where_clause = " location = '$user[location]' && login_id='$user[login_id]' && $item_max_sql > 0 && $item_sql < $item_max_sql ";
	}

	//elect all viable ships
	database("select sum($sql_max_check) as total_capacity, count(ship_id) as total_ships from ${db_name}_ships where ".$sql_where_clause);
	$maths = dbr(1);

	//insufficient cash
	if ( user['cash'] < $item_cost:
		$ret_str .= "You do not have enough money for even 1 unit of <b class=b1>$item_str</b>. You certainly can't afford to fill a fleet.";
	} elseif(empty($maths) || $maths['total_ships'] < 1) { //ensure there are some ships.
		$ret_str .= "This operation failed as there are no ships that have any free capacity to hold <b class=b1>$item_str</b> in this system that belong to you.";
	else :
		//work out the total value of them all.
		$total_cost = $maths['total_capacity'] * $item_cost;

		//user CAN afford to fill the whole fleet
		if ( total_cost <= $user['cash']) {

			if(empty($sure): //confirmation
				get_var('Load ships',$script_name,"There is capacity for <b>$maths[total_capacity]</b> <b class=b1>$item_str</b> in <b>$maths[total_ships]</b> ships in this system. <p>You have enough money to fill all the ships with <b class=b1>$item_str</b>. Do you wish to do that?",'sure','yes');
			else : //process.
				dbn("update ${db_name}_ships set $item_sql = $item_max_sql where ".$sql_where_clause);
				take_cash($total_cost);

				if ( cargo_run == 0: //not cargo bay stuff
					$user_ship[$item_sql] = $user_ship[$item_max_sql];
				else : //cargo bay stuff
					$user_ship[$item_sql] += $user_ship['empty_bays'];
				}

				$ret_str .= "<b>$maths[total_capacity]</b> <b class=b1>$item_str</b> were added to <b>$maths[total_ships]</b> ships.<br>All ships are now at maximum capacity.";
			}

		//user CANNOT afford to fill the whole fleet, so we'll have to do it the hard way.
		else :
			$total_can_afford = floor($user['cash'] / $item_cost); //work out amount can afford.

			if(empty($sure)) { //confirmation
				$extra_text = "<p><input type=radio name=fill_dir value=1 CHECKED> - Fill highest capacity ships ships first.";
				$extra_text .= "<br><input type=radio name=fill_dir value=2> - Fill lowest capacity ships first.";
				get_var('Load ships',$script_name,"There is capacity for <b>$maths[total_capacity]</b> <b class=b1>$item_str</b> in <b>$maths[total_ships]</b> ships in this system. <br>However, you can only afford <b>$total_can_afford</b> $item_str.<p>Do you want to fill as many ships as you can afford to fill?".$extra_text,'sure','yes');
			else : //process
				if ( fill_dir == 1:
					$order_dir = "desc";
				else :
					$order_dir = "asc";
				}

				if ( total_can_afford < 1: //error checking
					return "Unable to fill any ships with anything.";
				}

				$used_copy_afford = $total_can_afford; //make copy of the above.
				$final_cost = $item_cost * $total_can_afford; //work out the final cash cost of it all.
				$fill_ships_sql = ""; //intiate sql string to load a bunch of ships at once
				$temp_str = "";

				db2("select ship_id, $item_sql, $item_max_sql as max, ship_name from ${db_name}_ships where ".$sql_where_clause." order by $item_max_sql $order_dir");

				while($ships = dbr2(1)) { //loop through the ships

					$ship_counter++; //increment counter
					$free_space = $ships['max'] - $ships[$item_sql]; //capacity of present ship

					if ( free_space < $used_copy_afford) { //can load ship
						$used_copy_afford -= $free_space; //num to use
						$fill_ships_sql .= "ship_id = '$ships[ship_id]' || ";

						$temp_str .= "<br><b class=b1>$ships[ship_name]</b> had its $item_str cargo increased by <b>$free_space</b> to maximum capacity.";

						if ( ships['ship_id'] == $user_ship['ship_id']: //do the user ship too.
							if ( cargo_run == 0: //not cargo bay stuff
								$user_ship[$item_sql] = $user_ship[$item_max_sql];
							else : //cargo bay stuff
								$user_ship[$item_sql] += $user_ship['empty_bays'];
							}
						}

					else : //cannot load ship whole ship.
						dbn("update ${db_name}_ships set $item_sql = $item_sql + '$used_copy_afford' where ship_id = '$ships[ship_id]'");

						if ( ships['ship_id'] == $user_ship['ship_id'] && $cargo_run == 0: //do the user ship too.
							$user_ship[$item_sql] += $used_copy_afford;
						} elseif ( ships['ship_id'] == $user_ship['ship_id']) { //cargo bay stuff
							$user_ship[$item_sql] += $used_copy_afford;
						}
						$temp_str .= "<br><b class=b1>$ships[ship_name]</b>s <b class=b1>$item_str</b> count was increased by <b>$used_copy_afford</b>.";
						break 1;
					}
				} //end of while

				$ret_str .= "<b>$ship_counter</b> ships had their <b class=b1>$item_str</b> count augmented by more $item_str.<br>Total increase in $item_str = <b>$total_can_afford</b>; Cost = <b>$final_cost</b><p>More Detailed Statistics :".$temp_str;

				//update database with fully loaded ships.
				if(!empty($fill_ships_sql):
					$fill_ships_sql = preg_replace("/\|\| $/", "", $fill_ships_sql);
					dbn("update ${db_name}_ships set $item_sql = $item_max_sql where ".$fill_ships_sql);
				}
				take_cash($final_cost); //charge the cash
			}
		}
	}
	return $ret_str; //return the result string.
}


//function that will return a list of the contents of the ships cargo bays.
function bay_storage($ship:
	if(empty($ship['cargo_bays'])) {
		return "\n<b>None</b>";
	}
	$ret_str = "";
	if(!empty($ship['metal'])) {
		$ret_str .= "\n<b>$ship[metal]</b> Metals";
	}
	if(!empty($ship['fuel'])) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[fuel]</b> Fuels";
	}
	if(!empty($ship['organ'])) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[organ]</b> Organics";
	}
	if(!empty($ship['elect'])) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[elect]</b> Electronics";
	}
	if(!empty($ship['colon'])) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[colon]</b> Colonists";
	}
	empty_bays($ship);
	if ( ship['empty_bays'] > 0) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[empty_bays]</b> Empty";
	}
	return $ret_str;
}

//function that will work out how many flagships this player has got through.
function num_flagships ($num_ships:
	if ( num_ships == 0:
		return 0;
	}

	$result_num = 0;
	while($num_ships > 1:
		$num_ships = $num_ships / 2;
		$result_num ++;
	}
	return $result_num;
}

?>
