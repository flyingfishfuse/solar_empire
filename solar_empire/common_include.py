import solar_empire
import solar_empire.models

#Function: connect to the database. Will write to the error log if cannot connect.
#send a query to the database.
	#function db(string)
#collect results of query made by db() function
	#function database_results(rest_type = 0)
#send a query to the database.
	#function db2(string)
#collect results of query made by db2() function
	#function database_results(rest_type = 0)
#send an update or insert query to the database. no select's.
	#function dbn(string)

# will output the beginning of a properly formatted table putting
#the values of the passed array in as the table headers;
# - expects an array.

#//outputs a row of a table with the array values bolded in each cell; expects a four-element array.
	#function quick_row(name, value)
#//function to insert an entry into the user_history table
	#function insert_history(l_id,i_text)
#//post an entry into the news
	#function post_news(headline)
#//function that will send a header correct e-mail, or return failure if it doesn't work
	#function send_mail(myname, myemail, contactname, contactemail, subject, message)

#/********************
#Ship Information Functions
#********************/

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




#def gameVars(db_name):

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
		database_results =  where name = 'score_method'")
		alpha_var = database_results
		score_method = alpha_var['value']
		extra_text = "login_id = 'login_id'"
		plan_text = "login_id = 'login_id'"
	else :
		and_text = " && "
		extra_text = plan_text = "login_id != " . ADMIN_ID

	#scoring method, whereby only kills,are taken into account.
	if(score_method==1):
		dbn("update {db_name}_users set score = (fighters_killed + (ships_killed * 10)) - (fighters_lost * 0.75 + (ships_lost * 5)) where ".extra_text);
	 #takes into account ships lost, ships killed, fighters lost, fighters killed.
	elif(score_method == 2):
		#dbn("update {db_name}_users set score = ships_killed_points - (ships_lost_points * 0.5) where ".extra_text);
	#total fiscal value score.
	elif (score_method == 3):
		db("select sum(fighters) + sum(point_value), login_id from {db_name}_ships where ".extra_text." GROUP BY login_id");
		db2("select sum(fighters), login_id from {db_name}_planets where ".plan_text." GROUP BY login_id");
		if(full == 1){
			while(plan_array = database_results()){
				temp_plan_array[plan_array['login_id']] = plan_array[0];
			}
			while(ship_array = database_results()){
				ship_array[0] += temp_plan_array[ship_array['login_id']];
				dbn("update {db_name}_users set score = 'ship_array[0]' where login_id = 'ship_array[login_id]'");
			}
			dbn("update {db_name}_users set score = 0 where score < 0");
		} else {
			ship_array = database_results();
			plan_array = database_results();
			ship_array[0] += plan_array[0];
			dbn("update {db_name}_users set score = 'ship_array[0]' where login_id = 'login_id'");
		}
	}
}

//function used to calculate the percentage of something. does not divide things by 0 though.
function calc_perc(num1,num2){
	if(num1 == 0 || num2 == 0){
		return "num1 (0%)";
	} else {
		result = number_format((num1 / num2) * 100, 2, '.','');
		return number_format(num1)." (".result."%)";
	}
}

//function to figure out how many empty cargo bays there are on the ship.
function empty_bays(&ship)
{
	ship['empty_bays'] = ship['cargo_bays'] - ship['metal'] -
	 ship['fuel'] - ship['elect'] - ship['colon'] - ship['organ'];
}




/*********************
Misc Functions
*********************/

//function that will create a help-link.
function popup_help(topic, height, width, string = "Info")
{
	return '<a href="' . esc(topic) . '" onclick="popup(\'' . topic .
	 '\', ' . (int)height . ',' . width . '); return false;">' . string .
	 '</a>';
}

//pilfered from the net. and altered it a little for good measure.
//creates a alpha-numeric string of length. contains uper and lower case chars).
function create_rand_string(length)
{
	// salt to select chars from
	salt = "abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
	return_string = "";

	for (i=0;i<length;i++){ // loop and create password
		return_string .= substr(salt, mt_rand() % strlen(salt), 1);
	}
	return return_string;
}


//makes a ship using the parts specified in ship_parts (array), ship_owner (also array)
//returns id of ship inserted.
function make_ship(ship_parts, ship_owner)
{
	global db_name;
	dbn("insert into {db_name}_ships (ship_name, login_id, login_name, clan_id, shipclass, class_name, class_name_abbr, fighters, max_fighters, max_shields, cargo_bays, mine_rate_metal, mine_rate_fuel, config, size, upgrades, move_turn_cost, point_value, num_ot, num_dt, num_pc, num_ew) values('".trim((string)ship_parts['ship_name'])."', 'ship_owner[login_id]', 'ship_owner[login_name]', 'ship_owner[clan_id]', 'ship_parts[type_id]', 'ship_parts[name]', 'ship_parts[class_abbr]', 'ship_parts[fighters]', 'ship_parts[max_fighters]', 'ship_parts[max_shields]', 'ship_parts[cargo_bays]', 'ship_parts[mine_rate_metal]', 'ship_parts[mine_rate_fuel]', 'ship_parts[config]', 'ship_parts[size]', 'ship_parts[upgrades]', 'ship_parts[move_turn_cost]', 'ship_parts[point_value]', 'ship_parts[num_ot]', 'ship_parts[num_dt]', 'ship_parts[num_pc]', 'ship_parts[num_ew]')");
	return mysql_insert_id();
}

// escape a string std
function esc(str)
{
	return htmlspecialchars(str);
}


?>
