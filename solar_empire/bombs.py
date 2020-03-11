#===========
#Damage Bombs
#===========

#determine type of bomb
if bomb_type == 1){ #gamma bomb
	b_text = "Gamma";
	sql_text = "gamma";
elif bomb_type == 2){ #delta Bomb
	b_text = "Delta";
	sql_text = "delta";


// checks
db(target,user)
planets = dbr(

if (emptyplanets)orreturn_user_variable( user_id , 'login_id') == ADMIN_USER_ID :
	if return_user_variable( user_id , 'gamma') < 1 && bomb_type==1 :
		scrolling_output_message("You don't have a Gamma Bomb.";
	elif return_user_variable( user_id , 'delta') < 1 && bomb_type==2 :
		scrolling_output_message("You don't have a Delta Bomb.";
	elif flag_sol_attack == 0 && return_user_variable( user_id , 'location') == 1 && return_user_variable( user_id , 'login_id') != ADMIN_USER_ID :
		scrolling_output_message("The Admin has disabled all forms of attack in the Sol System (system #<b>1</b>).";
	elif sure) :
		scrolling_output_message('Use b_text Bomb','bombs.php',"Are you sure you want to detonate a b_text Bomb?",'sure',''
	 else {

		if return_user_variable( user_id , 'login_id') != ADMIN_USER_ID){
			dbn("update {db_name_users set {b_text = {b_text - 1 where login_id = user[login_id]"
		

		post_news("<b class=b1>user[login_name]</b> unleashed a b_text Bomb in star system #<b>return_user_ship_variable('location]</b>"

		get_star(
		if bomb_type==1 : #gamma bomb
			bomb_damage = 200;
		elif bomb_type==2 : #delta bomb
			#clear all shields on all ships before we start.
			db("select s.ship_id from {db_name_ships s, {db_name_users u where s.location = 'user[location]' && u.login_id	!= 1 && s.ship_id > 1 && s.login_id = u.login_id && u.turns_run > 'turns_safe'"

			whiletarget_ship = dbr(1)){
				dbn("update {db_name_ships set shields = 0 where ship_id = 'target_ship[ship_id]'"
			
			target_ship = "";

			bomb_damage = 5000;
		

		if random_events == 2){
			bomb_damage *= 3;
		

		ship_counter = 0;
		dam_victim = array(
		destroyed_ships = 0;

		lastresort = mysql_query("select s.fighters,s.shields,s.ship_id,s.metal,s.fuel,s.location,s.login_id,s.class_name,s.ship_name,s.point_value,u.login_name, s.num_sa as num_sa from {db_name_ships s,{db_name_users u where s.location = 'user[location]' && s.ship_id > '1' && s.login_id >'1' && s.login_id = u.login_id && u.turns_run >= 'turns_safe'") or mysql_die("Bombs are messed up."

		elim = 0;

		#loop through players to damage.
		whiletarget_ship = mysql_fetch_arraylastresort) :
			#db("select login_name,login_id,ship_id from {db_name_users where login_id = 'target_ship[login_id]'"
			#target = dbr(


			ship_counter++;

			#silicon armour taken into effect.
			this_bomb = bomb_damage - target_ship['num_sa') * upgrade_sa
			temp121 = 0;
			temp121 = damage_shipthis_bomb,0,0,user,target_ship,target_ship

			#Used to limit messages sent, so each player only gets 1 message.
			dam_victim[target_ship['login_id']] .= "\n<br><b class=b1>target_ship[ship_name]</b> target_ship[class_name])";
			if temp121 > 0 :
				dam_victim[target_ship['login_id']] .= " - Destroyed";
				elim++;
			
		 # end bomb while loop.

		elim = 0;
		#loop to send out a message to each player.
		foreachdam_victim as victim_id => ship_list :

			ships_hit = substr_countship_list, "<b class=b1>"
			ships_killed = substr_countship_list, "- Destroyed"
			elim += ships_killed;

			#don't send a message to the user.
			if victim_id == return_user_variable( user_id , 'login_id' :
				continue;
			
			send_messagevictim_id,"<b class=b1>user[login_name]</b> unleashed a b_text Bomb in Star System #<b>return_user_ship_variable('location]</b>.<br>The bomb hit <b>ships_hit</b> of your ships doing <b>bomb_damage</b> damage to each.<br><br>Of those hit, <b>ships_killed</b> were destroyed by the blast.<br>Shown below is a compelte listing of all your ships hit by the bomb:<br>ship_list"
		

		if elim == 0){
			elim = "None";
		

		error_str .= "You have successfully released a b_text Bomb in system #<b>star[star_id]</b>, hitting <b>ship_counter</b> ships in all, and doing <b>".ship_counter*bomb_damage."</b> damage in total, or <b>bomb_damage</b> damage to each ship. Of those hit, <b>elim</b> were destroyed.";
		error_str .= "<br><br>To put that into a more appropriate context:";
		error_str .= "<p><b class=b2>kaaaaBBBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMM!!!!!!!</b>";
	

	db("select * from {db_name_users where login_id = 'user[login_id]'"
	user = dbr(1
	db("select * from {db_name_ships where ship_id = 'user[ship_id]'"
	user_ship = dbr(1
	empty_baysuser_ship
 else {
	scrolling_output_message("You cannot use a b_text Bomb in a system with an Attack Planet in it.";



scrolling_output_message("Use b_text Bomb",error_str
?>