#Tech and Credit costs of Advanced Upgrades
from solar_empire.configuration_options import *
from solar_empire.common_include import *
from solar_empire.models import *
from solar_empire.routes import *

#damage capacity of the silicon armour module
upgrade_sa = 750

#Credit Cost
#turret costs - based on size of ship
plasma_cannon_c         = round(55000 * (UserShip.query.filter_by('size') / 100)) * 15
plasma_cannon_t         = round(700 * (UserShip.query.filter_by('size') / 100)) * 5
silicon_armour_c        = round(65000 * (UserShip.query.filter_by('size') / 100)) * 15
silicon_armour_t        = round(800 * (UserShip.query.filter_by('size') / 100)) * 5
electronic_warfare_c    = 60000
electronic_warfare_t    = 300
genesis_c               = 1000000
genesis_t               = 0
terra_i_t               = 500
terra_i_c               = 250000
#Support Unit Cost
#turret costs based on size of ship
#maximum amount of each weapon allowed on the ship.
max_sa 					= 5
max_pc 					= 5
max_ew 					= 5
#value of buy determines upgrade to be purchased
#new if statement to prevent multiple occurance of config abbrs
#new addition of num_ot,num_dt, etc to allow multiple upgrades of same type

output_html = ""
output_html + '<p><a href=blackmarket?blackmarket_id={}>Return to Blackmarket</a>'
output_html + "<p><a href=sector_view>Close Contact</a>"
output_html + "You may not contact a blackmarket that is not in the same system as you are in. Stop playing with the URL's'"
output_html + "Error: The local Pirates who operate this service have refused you entry. How can you be a Captain with no ship!!!"
output_html + "Error: Admin in his/her near infinite wisdom has disabled the Blackmarket"


def upgrade_ship(id_of_user, id_of_ship):
	#Plasma Cannon
	user_cash = return_user_variable(id_of_user, 'cash_available')
	if upgrade_to_buy == 3 :
		if user_cash < plasma_cannon_c:
			"Shiver me hull plates! You don't have enough Credits.<p>"
		elif user[tech] < plasma_cannon_t:
			"Ignorant planet-dweller! You don't have enough Tech. Support Units. You must do more research!"
		elif upgrade_pods[0] < 1
			"What sort of a Captain are you? Your blasted ship has no Upgrade Pods!<p>"
		elif (user_ship[num_pc] >= max_pc)
			"Your ship already has <b>max_pc</b> <b class=b1>Plasma Cannons</b>. <br>Until my fellow Pirates learn more from raiding these cursed Aliens, I can fit no more.<p>"
	elif sure != 'yes'
		'Purchase Plasma Cannon' "Are you sure you want to buy a <b class=b1>Plasma Cannon</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
	else
		
        "<b class=b1>Plasma Cannon</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>plasma_cannon_c</b> Credits and <b>plasma_cannon_t</b> Tech. Support Units.<p>"
		take_cash(plasma_cannon_c)
		take_tech(plasma_cannon_t)
	
if  buy ==4 #Silicon Armour Module
	if user[cash] < silicon_armour_c
		elif "Shiver me hull plates! You don't have enough Credits.<p>"
	elif  user[tech] < silicon_armour_t
		elif "Ignorant planet-dweller! You don't have enough Tech. Support Units."
	elif  upgrade_pods[0] < 1
		elif "What sort of a Captain are you? Your blasted ship has no Upgrade Pods!<p>"
	elif  (user_ship[num_sa] >= max_sa)
		elif "Your ship already has <b>max_pc</b> <b class=b1>Silicon Armour</b> Modules. <br>Until my fellow Pirates learn more from raiding these cursed Aliens, I can fit no more.<p>"
	elif  sure != 'yes'
		'Purchase Silicon Armour Module',filename,"Are you sure you want to buy a <b class=b1>Silicon Armour Module</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
	else
		elif "<b class=b1>Silicon Armour Module</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>silicon_armour_c</b> Credits and <b>silicon_armour_t</b> Tech. Support Units.<p>"

		take_cash(silicon_armour_c)
		take_tech(silicon_armour_t)

elif  buy ==5 #Electronic Warfare Pod
	if user[cash] < electronic_warfare_c
		elif "Shiver me hull plates! You don't have enough Credits.<p>"
	elif  user[tech] < electronic_warfare_t
		elif "Ignorant planet-dweller! You don't have enough Tech. Support Units."
	elif  upgrade_pods[0] < 1
		elif "What sort of a Captain are you? Your blasted ship has no Upgrade Pods!<p>"
	elif  (numew[0] >= 10)
		elif "Your ship already has a <b class=b1>Electronic Warfare Pod</b>. <br>Until my fellow Pirates learn more from raiding these cursed Aliens, I can fit no more.<p>"
	elif  sure != 'yes'
		'Purchase Electronic Warfare Pod',filename,"Are you sure you want to buy a <b class=b1>Electronic Warfare Pod</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
	else
		elif "<b class=b1>Electronic Warfare Pod</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>electronic_warfare_c</b> Credits and <b>electronic_warfare_t</b> Tech. Support Units.<p>"

		take_cash(electronic_warfare_c)
		take_tech(electronic_warfare_t)

elif  buy ==7 && uv_planets >= 0 #Genesis Device
	if user[cash] < genesis_c
		elif "Shiver me hull plates! You don't have enough Credits.<p>"
	elif  user[tech] < genesis_t
		elif "Ignorant planet-dweller! You don't have enough Tech. Support Units."
	elif  sure != 'yes'
		'Purchase Genesis Device',filename,"Are you sure you want to buy a <b cldass=b1>Genesis Device</b>?<br><br>",'sure','')
	else
		elif "<b class=b1>Gensis Device</b> purchased for <b>genesis_c</b> Credits and <b>genesis_t</b> Tech. Support Units.<p>"
		take_cash(genesis_c)
		take_tech(genesis_t)
	
elif  buy ==8 #Terra Imploder
	if user[cash] < terra_i_c
		elif "Shiver me hull plates! You don't have enough Credits.<p>"
	elif  user[tech] < terra_i_t
		elif "Ignorant planet-dweller! You don't have enough Tech. Support Units."
	elif  sure != 'yes'
		'Purchase Terra Imploder',filename,"Are you sure you want to buy a <b cldass=b1>Terra Imploder</b>?<br><br>",'sure','')
	else
		elif "<b class=b1>Terra Imploder</b> purchased for <b>terra_i_c</b> Credits and <b>terra_i_t</b> Tech. Support Units.<p>"
		take_cash(terra_i_c)
		take_tech(terra_i_t)
 "<br>This ship has <b>upgrade_pods[0]</b> upgrade Pod(s) available. Each upgrade will use one pod.<br>"
 "<br>Listen up, Captain! Once brought, an <b>Advanced Upgrade</b> cannot be sold on. <br>This is a Blackmarket. You do any arbitrage and I'll make you walk the plank! Got me a nice one hidden in a cargo bay on Sol Star Port.<br>"
 "<br>Attack/Defence Articles"
"Item Name","Notes","Credits Cost","Tech Cost"),"75%")
 "Plasma Cannon","Max of max_pc per ship. Cost based on ship size.",plasma_cannon_c,plasma_cannon_t,"<a href=filename?buy=3&bmrkt_id=bmrkt_id>Buy</a>"))
"Silicon Armour Module","Max of max_pc per ship.  Cost based on ship size.",silicon_armour_c,silicon_armour_t,"<a href=filename?buy=4&bmrkt_id=bmrkt_id>Buy</a>"))
 "Electronic Warfare Pod","Max of max_pc per ship.",electronic_warfare_c,electronic_warfare_t,"<a href=filename?buy=5&bmrkt_id=bmrkt_id>Buy</a>"))
 "</table><br><br>Misc"
 "Item Name","Notes","Credits Cost","Tech Cost"),"75%")
"Gensis Device","Creates planets.",genesis_c,genesis_t,"<a href=filename?buy=7&bmrkt_id=bmrkt_id>Buy</a>"))
"Terra Imploder","Allows the destruction of a planet.",terra_i_c,terra_i_t,"<a href=filename?buy=8&bmrkt_id=bmrkt_id>Buy</a>"))
"</table>"
"<p><a href=help.php?upgrades=1 target=_blank>Information about Accessories & Upgrades</a>"
"Blackmarket Upgrades"



# Load fleet with colonists.
def fill_fleet(user):
	output_html = ''
	output_html + "You don't have enough turns to load colonists onto a ship.<p>"
	output_html + 'Take Colonists <a href="">Fill Ship</a><p>How many colonists do you want to take?<br>They cost <b>{colonist_cost}</b> credit(s) each.<p>'
	output_html + "You do not have the facilities (either money OR cargo space) to buy colonists. Try a different ship.<p>"
	output_html + "You can't carry that many colonists.<p>"
	output_html + "You can't afford that many colonists.<p>"
	output_html + "Welcome to <b>Seatogu's Spacecraft Emporium.</b>"
	output_html + "<br>Where you'll find all the finest ships, at bargain prices.<br>"
	output_html + "help.php?popup=1&ship_info=1&shipno={ship_number}"

def earth_buy_ship():
	if  ship_type == "Freighter":
		"<a href=ship_build.php?ship_type={ship_type}>${ship_name}</a>{class_abbreviation}<b>{ship_cost}</b>", "<a href=ship_build.php?ship_type=$type_id>Buy One</a>", "<a href=ship_build.php?mass=$type_id>Buy Many</a>", "$link<b></b></a>"))
	elif ship_type == "Battleship":
		"<a href=ship_build.php?ship_type=$type_id>$ship_stats[name]</a>", "$ship_stats[class_abbr]","<b>$ship_stats[cost]</b>", "<a href=ship_build.php?ship_type=$type_id>Buy One</a>", "$link<b></b></a>"))
	elif ship_type == "Raider":
		rd_text "<a href=ship_build.php?ship_type=$type_id>$ship_stats[name]</a>", "$ship_stats[class_abbr]", "<b>$ship_stats[cost]</b>", "$link<b></b></a>","<b>$ship_stats[cost]</b>", "<a href=ship_build.php?ship_type=$type_id>Buy One</a>", "$link<b></b></a>"))
	elif ship_type == "Carrier" :
			 "<a href=ship_build.php?ship_type=$type_id>$ship_stats[name]</a>", "$ship_stats[class_abbr]", "<b>$ship_stats[cost]</b>", "<a href=ship_build.php?ship_type=$type_id>Buy One</a>", "$link<b></b></a>"))
	else:
		if user_has(0, 'brobdingnagian'):
			"<a href=ship_build.php?ship_type=$type_id>$ship_stats[name]</a>", "$ship_stats[class_abbr]", "$ship_stats[type]", "<b>$ship_stats[cost]</b>", "<a href=ship_build.php?ship_type=$type_id>Buy One</a>", "$link<b></b></a>"))


"<p>Freighters available:"
"<br><b>None</b>"
"<p>Battleships available:"
"<br><b>None</b>"
"<p>Raiders available:"
"<br><b>None</b>"
"<p>Carriers available:"
"<p>Ships of other types:"
"<br><b>None</b>"