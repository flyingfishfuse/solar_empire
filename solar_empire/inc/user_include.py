#!/usr/bin/python3
import solar_empire
from solar_empire.models import *
from solar_empire.inc.common_include import *

#generic link to go back to the start system
system_view = "<p><a href='location'>Back to the Star System</a><br>"
#damage capacity of the silicon armour module
admin_view = "<p><a href=admin.php>Back to Admin Page</a>";

def return_user_by_id(id_of_user):
	dbquery = database.session.query('user_id')

def return_user_list():
	pass

def return_user_variable(user_id , var):
	user_to_probe = return_user_by_id(user_id) 
	pass

def update_database(thing):
	database.session.add(thing)
	database.commit()
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
	# remove the cost from player
	user_to_modify     = return_user_by_id(user_id)
	# add amounts to current values for those things 
	subtracted_cash    = return_user_variable(user_id , 'cash') - cash_cost
	subtracted_mineral = return_user_ship_variable(user_id , 'mineral') - mineral_cost
	subtracted_metal   = return_user_ship_variable(user_id , 'metal') - metal_cost
	subtracted_fuel    = return_user_ship_variable(user_id , 'fuel') - fuel_cost

	# add the upgrade to player
	#update database
	pass

def pay_bounty(user_with_bounty, user_with_money, comission_percent):
	amount = round((amount /100) * comission_percent) + amount + 1
	#bount = round((list_em[bounty] / 100) * commission_percent
	#bount1 = round((topay[bounty] / 100) * commission_percent
	pass

#/********************
#Account updating functions
#*********************/

#function that charges turns for something. Admin is exempt.
def charge_turns(amount, user_id):
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

#function takes cash from a player. Admin is exempt.
def take_cash(user_id, amount):
	pass

def remove_resource_from_player(user_id, resource, amount):
	pass

def add_resource_to_player(user_id, resource, amount):
	pass

def kill_shields(user_id):
	pass

def kill_fighters():
	pass

#function that damages a ship with a specified amount of damage.
#send a negative number as the first arguement to destroy a ship outright.
def damage_ship(amount, fig_dam, s_dam, attacker, target , target_ship):
	#set the shields down first off (if needed).
	#take the fighters down next (if needed).
	# don't want to hurt the admin now do we?
	#shield_damage = 0;
	#set ships_killed
	#// ship not destroyed


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
	#dist = round(sqrt(abs((star1['x_loc - star2['x_loc) * 2) + abs((star1['y_loc - star2['y_loc)*2)))
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
	#target['location = $rand_star;


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
#	$dam['dt = round(330 * (mt_rand(75, 125) / 100)) * $ship['num_dt;

	#offensive turret : lvl 1
#	$dam['ot = round(200 * (mt_rand(80, 120) / 100)) * $ship['num_dt;

	#silicon armour : lvl 2
#	$dam['sa = round($upgrade_sa * (mt_rand(90, 110) / 100)) * $ship['num_sa;

	#plasma cannon : lvl 2
#	$dam['pc = round(420 * (mt_rand(92, 108) / 100)) * $ship['num_pc;

	#electronic warfare module : lvl 1
#	$dam['ewd = round(325 * (mt_rand(85, 115) / 100)) * $ship['num_ew;
#	$dam['ewa = round(225 * (mt_rand(80, 120) / 100)) * $ship['num_ew;

#	return $dam;

#A function that gets all the details for the user's new ship, and returns the completed user_ship array.
#function userShip($id)

#a function that allows a message to be sent to all players.

#a function to allow for easy addition of upgrades.
def	make_standard_upgrade(upgrade_str, config_addon, cost, developement_id, tech_cost = 0):
	if ( user_to_show_bar_to.cash < cost):
		return "You can not afford to buy a <b class=b1>$upgrade_str</b>.<p>"

	elif ( user_to_show_bar_to.tech < tech_cost and tech_cost > 0):
		return "Ignorant Planet Dweller. You don't have enough tech points.<p>"
	
	elif (ship_to_display.config, config_addon) != false:
		return "Your ship is already equipped with a <b class=b1>$upgrade_str</b>.<br>There is no point in having more than one on a ship.<p>"

	elif (ship_to_display.upgrades < 1):
		return "";
	else :
		take_cash(cost);
		take_tech(tech_cost);
		ship_to_display.config + ":" + config_addon;
		#update db_name    ships set config = '
		# user_ship[config] ', 
		# upgrades = upgrades - 1 where ship_id = '$user[ship_id]'");
		return "<b class=b1>$upgrade_str</b>, purchased and fitted to the <b class=b1>"
		#user_ship[ship_name]</b> for <b>$cost</b> Credits.<p>";


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
	if ( user_to_show_bar_to.cash < $item_cost:
		$ret_str .= "You do not have enough money for even 1 unit of <b class=b1>$item_str</b>. You certainly can't afford to fill a fleet.";
	} elseif(empty($maths) || $maths['total_ships < 1) { //ensure there are some ships.
		$ret_str .= "This operation failed as there are no ships that have any free capacity to hold <b class=b1>$item_str</b> in this system that belong to you.";
	else :
		//work out the total value of them all.
		$total_cost = $maths['total_capacity * $item_cost;

		//user CAN afford to fill the whole fleet
		if ( total_cost <= $user_to_show_bar_to.cash) {

			if(empty($sure): //confirmation
				get_var('Load ships',$script_name,"There is capacity for <b>$maths[total_capacity]</b> <b class=b1>$item_str</b> in <b>$maths[total_ships]</b> ships in this system. <p>You have enough money to fill all the ships with <b class=b1>$item_str</b>. Do you wish to do that?",'sure','yes');
			else : //process.
				dbn("update ${db_name}_ships set $item_sql = $item_max_sql where ".$sql_where_clause);
				take_cash($total_cost);

				if ( cargo_run == 0: //not cargo bay stuff
					$user_ship[$item_sql] = $user_ship[$item_max_sql];
				else : //cargo bay stuff
					$user_ship[$item_sql] += $ship_to_display.empty_bays;
				}

				$ret_str .= "<b>$maths[total_capacity]</b> <b class=b1>$item_str</b> were added to <b>$maths[total_ships]</b> ships.<br>All ships are now at maximum capacity.";
			}

		//user CANNOT afford to fill the whole fleet, so we'll have to do it the hard way.
		else :
			$total_can_afford = floor($user_to_show_bar_to.cash / $item_cost); //work out amount can afford.

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
					$free_space = $ships['max - $ships[$item_sql]; //capacity of present ship

					if ( free_space < $used_copy_afford) { //can load ship
						$used_copy_afford -= $free_space; //num to use
						$fill_ships_sql .= "ship_id = '$ships[ship_id]' || ";

						$temp_str .= "<br><b class=b1>$ships[ship_name]</b> had its $item_str cargo increased by <b>$free_space</b> to maximum capacity.";

						if ( ships['ship_id == $ship_to_display.ship_id: //do the user ship too.
							if ( cargo_run == 0: //not cargo bay stuff
								$user_ship[$item_sql] = $user_ship[$item_max_sql];
							else : //cargo bay stuff
								$user_ship[$item_sql] += $ship_to_display.empty_bays;
							}
						}

					else : //cannot load ship whole ship.
						dbn("update ${db_name}_ships set $item_sql = $item_sql + '$used_copy_afford' where ship_id = '$ships[ship_id]'");

						if ( ships['ship_id == $ship_to_display.ship_id && $cargo_run == 0: //do the user ship too.
							$user_ship[$item_sql] += $used_copy_afford;
						} elseif ( ships['ship_id == $ship_to_display.ship_id) { //cargo bay stuff
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
	if(empty($ship['cargo_bays)) {
		return "\n<b>None</b>";
	}
	$ret_str = "";
	if(!empty($ship['metal)) {
		$ret_str .= "\n<b>$ship[metal]</b> Metals";
	}
	if(!empty($ship['fuel)) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[fuel]</b> Fuels";
	}
	if(!empty($ship['organ)) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[organ]</b> Organics";
	}
	if(!empty($ship['elect)) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[elect]</b> Electronics";
	}
	if(!empty($ship['colon)) {
		if(!empty($ret_str):
			$ret_str .= "<br>";
		}
		$ret_str .= "\n<b>$ship[colon]</b> Colonists";
	}
	empty_bays($ship);
	if ( ship['empty_bays > 0) {
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
