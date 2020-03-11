import solar_empire
from solar_empire import *
from solar_empire.models import *
from solar_empire.configuration_options import *
from solar_empire.common_include import *
from solar_empire.names.names import *
from solar_empire.user_include import *
from math import *

random_events = random_events
sure = ask_if_certain()

#supernova effectors, add to db model in moring please
sn_effect = True

#this line needs to go somewhere
#scrolling_output_message('Use SuperNova Effector - Are you sure you want to use the SuperNova Effector?')
random_events = return_system_variable('random_events_level')

def attack_with_bomb(attacker_user, target_user, target_ship):
    attacker = return_user_by_id(attacker_user)
    if return_user_variable( attacker , 'user_id') != ADMIN_USER_ID :
	    if return_user_variable( attacker , 'turns_run') < SAFE_TURNS :
		    scrolling_output_message("Bomb","You can't attack during the first <b>turns_before_attack</b> turns of having your account."
	    if does_user_have_ship() == False :
		    scrolling_output_message("Bomb","You May not use a Bomb when you are not commanding a ship. Try buying a ship then set off a Bomb"
    #SuperNova Effector
    if sn_effect :
	    # random events prevent it from occuring
		if return_user_variable( attacker , 'sn_effect') < 1 :
		    scrolling_output_message("No can Blow: You don't have a SuperNova Effector.")
	    elif random_events == 2 :
		    scrolling_output_message("No can Blow: Sorry. You need a system with a star in to allow you to blow it up. <br>This system is a <b class=b1>Nebula</b>, which means that it is only gases. <br>Try again somewhere else.")
	    elif random_events == 1 :
    		scrolling_output_message("No can Blow: Sorry. You need a system with a star in to allow you to blow it up. <br>The star in this system has already exploded, and has formed a <b class=b1>BlackHole</b>. <br>Try again somewhere else.")
        elif random_events == 6 :
	    	scrolling_output_message("No can Blow: Sorry. You need a system with a star in to allow you to blow it up. <br>The star in this system only just exploded, and is now a <b class=b1>SuperNova Remnant</b>. <br>Try again somewhere else.")
        elif random_events == 5 or random_events == 10 :
    		scrolling_output_message("No can Blow: This star is already fairly likely to Blow-up. <br>There's no point in using your SN Effector here.")
        #no more random events left to evaluate, lets gor for the kill shot...
		# wait this is E'arth, of the sol system...
		# those bastards wanna fire a superwaeapon!?!?
		# wormhole 'em to a hell hole!
		elif return_system_variable('system_id') == 1 :
			wormhole_playership(attacker , 'location')
			scrolling_output_message("Mutiny: <b>What!?!?!</b> You'd try and destroy the <b class=b1>Sol system</b>? <br>What sort of <b>Maniac</b> are you? <br>Fortunatly the crew on your ship knew better, and so <b class=b1>mutineed </b>to stop you destroying everything they hold fair. <p>Your ship was destroyed during the mutiny."
		#they can fire the thing but CAN THEY SURVIVE IT?!?!?
		# ships lower than class 4 get destroyed!
		elif return_user_ship_variable(attacker,'shipclass')  2 :
			create_escape_pod_user(return_user_ship_variable(target_ship))
        else :
			#unexpected conditional condition
			pass
		scrolling_output_message("One of {login_name}</b>s ships was destroyed by a mutiny of the crew."
	elif sure :
		scrolling_output_message('Use SuperNova Effector : Are you sure?'
	else 
		if attacker != ADMIN_USER_ID:
			scrolling_output_message("<b class=b1>{login_name}</b> released a SuperNova Effector in star system #<b>{attacker_location}</b>")
			scrolling_output_message("Due to the Release of a SuperNova Effector in system #<b>{location} </b> by <b class=b1> {login_name} </b> only a few moments ago, the star is set to go SuperNova. This means that everything in the system will be destroyed. The star will explode within the next <b>48 hours</b>.')
			scrolling_output_message("Detonation Complete: The SuperNova Effector has successfully detonated.<br>This star will go SuperNova within the next <b>48 hours</b>.")

#Alpha Bomb
def fire_aplha_bomb(target,user):
	if return_usership_variable( user_id , 'alpha_bombs') < 1 :
		scrolling_output_message("You don't have a Alpha Bomb.")
	elif return_user_variable( user , 'location'):
		scrolling_output_message("The Sol System is protected by a eons old shield that has never flickered once...")
		wormhole_playership(user)
	elif scrolling_output_question('Use Alpha Bomb : Are you sure you want to use an Alpha Bomb?'):
		output = "<b class=b1>{username}</b> imploded a Alpha Bomb in system {location}"
		target_list = get_all_ships_system(target)
		for shieldy_bois in target_list:
			kill_shields(target)
			scrolling_output_text("\n<br><b class=b1>{ship_name}</b> {class_name}")
	#loop to send out a message to each player.
		for targets in target_list:
			victim_id = return_user_ship_by_id(targets)
			#don't send a message to the user if they are hit by a bomb.
			send_message(victim_id,"<b class=b1>{}</b> unleashed an Alpha Bomb in Star System #<b>{}</b>. " + \ 
				"<br>The bomb hit <b class=b1>{ships_hit}</b> of your ships, completely eliminating all of their shields." + \
				"<br>Shown below is a complete listing of your all ships hit by the blast:<br>{ship_list}")
			
			scrolling_output_text("You have successfully released an Alpha Bomb in system #<b>{}</b>, " + \ 
				"hitting <b>{ship_counter}</b> ship(s) in all, and reducing all shields on those ships to <b>0</b>.")
	elif is_attack_planet(target):
		scrolling_output_message("You cannot use a Alpha Bomb in a system with an Attack Planet in it.";
	else:
		scrolling_output_text("")
        pass

