import solar_empire
from solar_empire.models import *
from solar_empire.common_include import *
from solar_empire.user_include import *


def statusBar(user_id):
	user_has_no_ship    = None 
	user_to_show_bar_to = return_user_by_id(user_id)
	#user is not in an escape pod
	if does_user_have_ship(user_id):
		ship_to_display = user_ship_for_info(user_id) 
	else:
		#user is in escape pod
		user_has_no_ship = True
# is game paused?
	if (GameVars.is_game_paused == True):
		game_menu = "<h1> {game_name} / game paused" + "</h1>\n".format(game_name = GameVars.game_name)
	else :
		game_menu = "<h1> {game_name} / game on!" + "</h1>\n".format(game_name = GameVars.game_name)
# Active Users
	game_menu + "<p>active users: {}</p>\n".format(GameVars.logged_in_players_int)
	for each_player in return_user_list: 
		game_menu + "<p>" + each_player + "</p>\n"
# game paused information	
	if (GameVars.is_game_paused == True):
		game_menu + "<p>{count_days_left_in_game} days left</p>\n"
        game_menu + "<h2>" + user_to_show_bar_to.name + \
                    		 user_to_show_bar_to.clan_id + \
                    		 user_to_show_bar_to.clan_sym + \
                    		 user_to_show_bar_to.clan_sym_color + "</h2>\n"
#safe turns left information
	if (user_to_show_bar_to.turns_run < user_to_show_bar_to.safe_turns_left):
		safe_turns_left = SAFE_TURNS - user_to_show_bar_to.turns_run 
		game_menu + "<p><em>{safe_turns_left}</b> safe turn(s) left</em></p>\n".format(safe_turns_left = user_to_show_bar_to.safe_turns_left)
	else:
		game_menu + "<p><em>Leaving</em> newbie safety!</p>\n" + \
			'You have just left Newbie safety.<p>This means that you are now attackable by any player who can attack. <p>Good Luck.'
# Display turns left, tech and CASH BABY!
		game_menu + "<table>\n\t<tr>\n\t\t<th>Turns</th>\n\t\t<td>" + \
            user_to_show_bar_to.turns+ ' / ' + MAX_USER_TURNS + \
			"</td>\n\t</tr>\n\t<tr>\n\t\t<th>Credits</th>\n\t\t<td>" + user_to_show_bar_to.cash + "</td>\n\t</tr>\n"
		game_menu + "\t<tr>\n\t\t<th>Tech Units</th>\n\t\t<td>" + user_to_show_bar_to.tech + "</td>\n\t</tr>\n"
# Print Ship Info
	game_menu + "\t<tr>\n\t\t<th>Ships Killed</th>\n\t\t<td> " + \
            user_to_show_bar_to.ships_killed + "</td>\n\t</tr>\n\t<tr>\n\t\t<th>Ships Lost</th>\n\t\t<td>" + \
	        user_to_show_bar_to.ships_lost + "</td>\n\t</tr>\n\t<tr>\n\t\t<th>Score</th>\n\t\t<td>" + \
	        user_to_show_bar_to.score + "</td>\n\t</tr>\n</table>\n"

	if (user_to_show_bar_to.ship_id== None):
	   game_menu + "<h2>Your ship is destroyed!</h2>\n"
	else:
	   game_menu + "<h2>" + \
            popup_help('help?popup=1&ship_info=1&shipno=' + \
		    ship_to_display.shipclass, 300, 600, ship_to_display.ship_name) + "</h2>\n<table>\n\t<tr>\n\t\t" + \
            "<th>Class</th>\n\t\t<td>{user_ship_class_name}</td>\n\t</tr>\n\t".format(user_ship_class_name = ship_to_display.class_name) + \
            "<tr>\n\t\t<th>Fighters</th>\n\t\t<td>" + \
            ship_to_display.fighters+ ' / ' + \
            ship_to_display.max_fighters+ "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Shields</th>\n\t\t<td>" + \
            ship_to_display.shields+ ' / ' + \
		    ship_to_display.max_shields+ "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Specials</th>\n\t\t<td>" + \
            is_ship_cargo_empty + "</td>\n\t</tr>\n\t<tr>\n\t\t" + "<th>Cargo Bays</th>\n\t\t<td>"  + \
            ship_to_display.cargo_bay + "</td>\n\t</tr>\n</table>\n"
# LEFT SIDE	
	game_menu + "<h2>Menu</h2>\n<ul>\n" + \
				"\t<li><a href='system_view'>Star System</a></li>\n" + \
				"\t<li><a href='diary'>Fleet Diary</a></li>\n" + \
				"\t<li><a href='news'>Game News</a></li>\n"
# Clan stuff    
#	if (max_clans > 1 or user_to_show_bar_to.login_id== ADMIN_USER_ID):
	game_menu + "\t<li><a href='clan'>Clan Control</a></li>\n"
#	else:
#		if (enable_politics):
	game_menu + "\t<li><a href='politics'>Politics</a></li>\n"
	game_menu + "\t<li><a href='player_stat'>Player Ranking</a></li>\n</ul>\n<ul>\n"
	game_menu + "\t<li><a href='messages_page'>Messages </a> - <a href='send_message'>Send Message</a></li>\n"
	game_menu + "\t<li><a href='forum'>Forum</a><a href='forum?new=1'>forum - new</a></li>\n"
	if user_to_show_bar_to.login_id == ADMIN_USER_ID or user_to_show_bar_to.login_id== OWNER_ID:
		if (user_to_show_bar_to.login_id== ADMIN_USER_ID):
			game_menu + "\t<li><a href='admin_forum'>Admin Forum</a></li>\n"
			game_menu + "\t<li><a href='clan_forum'>Clan Forums</a></li>\n"
	#user has a clan
	elif user_to_show_bar_to.clan_id > 0 :
		    game_menu + "\t<li><a href='clan_forum'><span style='color: #" + user_to_show_bar_to.clan_sym_color + "'>" + \
            user_to_show_bar_to.clan_sym + "</span> Forum</a></li>\n"
	
	game_menu + "\t<li><a href='http://forum.solar-empire.net/'>Global Forum</a></li>\n</ul>\n<ul>\n"

    # admin lower sidebar
	if user_to_show_bar_to.login_id == ADMIN_USER_ID :
		game_menu + "\t<li><a href='admin'>Admin</a></li>\n"
		game_menu + "\t<li><a href='developer'>Server</a>\n"
# help and stuff
	game_menu + "\t<li><a href='help'>Help</a></li>\n" + \
	       "\t<li><a href='options'>Options</a></li>\n"
	if (user_to_show_bar_to.login_id != ADMIN_USER_ID):
		game_menu + "\t<li><a href='logout'>Game List</a></li>\n"
	game_menu + "\t<li><a href='logout?comp_logout=1'>Logout</a></li>\n</ul>\n"
	return game_menu
