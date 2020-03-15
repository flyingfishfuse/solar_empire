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


def shop(userid, ):
if user.location != '1':
	print_page("Error","You are unable to buy Accessories & Upgrades here.")
elif user.ship_id == None and user.login_id !=1:
	print_page("Error","You are unable to buy Accessories & Upgrades here, as you do not have a real ship.")
# checks
if buying =='fighter_upgrade': #Fighter capacity
	if user_ship.max_fighters + fighter_inc >= 5000 and user_ship.config != 'battleship':
		"It is against regulations to have more than 4,999 fighter capacity on a ship unless the ship is registered as a battleship.<br>To do that you'll have to purchase a battleship upgrade from Bilkos.<p>"
	else :
		make_basic_upgrade("Fighter","max_fighters",fighter_inc,basic_cost)
	elif buy ==2:  #Shield Capacity
		if user_ship.config == 'subspace_jumpdrive':
			"Ships with Sub-Space Jump drieves are not allowed to have shields on due to technical problems involving the dynamics of warp-point generation.<p>"
		else :
			make_basic_upgrade("Shield","max_shields",shield_inc, basic_cost )
	elif buy ==3: #Cargo capacity
		make_basic_upgrade("Cargo Bay","cargo_bays", cargo_inc , basic_cost )
	elif buy==4: #shrouder
		if user_ship.config == 'low_stealth':
			"This ship already has low stealth. It is not possible to upgrade to high-stealth.<p>"
		elif:
			get_var('Buy Scanner',filename,"This device will Highly stealth the ship. Enemy players will only see a distortion, and not be able to target it, unless they have a scanner on their ship.<br>If they do have a scanner they will still not be able to see who owns the ship.<p>Are you sure you want to buy a <b class=b1>Shrouding Unit</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			make_standard_upgrade ("Shrouding Unit", "hs", cloak_cost, 2003)
	elif buy==5: #Shield Charger
		if user_ship.max_shields < 1 :
			"Why do you want a <b class=b1>Shield Charging Upgrade</b> on a ship that has no shield capacity? <br>I advise you re-think your strategy.<p>"
		 else 
			get_var('Buy Shield Charging Upgrade',filename,"This upgrade will increase the shield charging rate for this ship.<p>Are you sure you want to buy a <b class=b1>Shield Charging Upgrade</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			make_standard_upgrade ("Shield Charging Upgrade", "sh", shield_charger, 2005)
	elif buy==6: #Transverser upgrade (wormhole stabiliser)
		if !"sj",user_ship.config :
			"This ship does not have a <b class=b1>SubSpace Jump Drive</b> and so is not capable of using a <b class=b1>Wormhole Stabiliser</b>.<p>"
		 else :
			get_var('Buy Wormhole Stabiliser',filename,"This upgrade will allow your ship to take more than 10 ships with it when sub-space jumping.<br>It will also allow you to auto-shift materials and colonists between planets.<p>Are you sure you want to buy a <b class=b1>Wormhole Stabiliser</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			make_standard_upgrade ("Wormhole Stabiliser", "ws", stabiliser_upgrade, 2006)
	elif buy==7: #Scanner
			get_var('Buy Scanner',filename,"Are you sure you want to buy a <b class=b1>Scanner</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			make_standard_upgrade ("Scanner", "sc", scanner_cost, 2004)
	elif buy ==8: #transwarp drive
		if "sj",user_ship.config :
			"Your ship has a <b class=b1>SubSpace Jump Drive</b> on, and so can't have a <b class=b1>Transwarp Drive</b>.<p>"
		 else :
			get_var('Buy Transwarp Drive',filename,"This upgrade will allow your ship (and any ships following it) to jump a limited distance across the universe. Ideal for peninsula hopping, and getting to star-islands.<p>Are you sure you want to buy a <b class=b1>Transwarp Drive</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			make_standard_upgrade ("Transwarp Drive", "tw", transwarp_cost, 2002)
	elif buy==10: #Pea Turret
		if user.cash < pea_turret:
			"You can not afford to buy a <b class=b1>Pea Shooter</b>.<p>"
		else :if(!avail_check(2000) :
			"This item has not been developed yet.<p>"
		elif user_ship.num_ot >= max_ot :
			"Your ship is already equipped with <b>max_ot</b> <b class=b1>Pea Shooters</b>. <br>The power relays on your ship are unable to cope with any more.<p>"
		elif user_ship.upgrades < 1 :
			"This ship does not have any upgrade pods available.<p>"
		 else :
			get_var('Buy Pea Shooter',filename,"This upgrade will complement your ships fighters in battle, allowing you to do more damage to the enemy ship(s).<p>Are you sure you want to buy a <b class=b1>Pea Shooter</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			"<b class=b1>Pea Shooter</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>pea_turret</b> Credits.<p>"
			take_cash(pea_turret)
			upgrades = upgrades - 1 num_ot = num_ot + 1
			user_ship.upgrades 
			user_ship.num_ot + 1
	elif buy==11: #Defensive Turret
		if user.cash < defensive_turret:
			"You can not afford to buy a <b class=b1>Defensive Turret</b>.<p>"
		else :if(!avail_check(2001) :
			"This item has not been developed yet.<p>"
		elif user_ship.num_dt >= max_dt :
			"Your ship is already equipped with <b>max_dt</b> <b class=b1>Defensive Turrets</b>. <br>The power relays on your ship are unable to cope with any more.<p>"
		elif user_ship.upgrades < 1 :
			"This ship does not have any upgrade pods available.<p>"
		 else :
			get_var('Buy Defensive Turret',filename,"This turret will destroy enemy fighters <b class=b1>Before</b> they have a chance to hurt your ship.<p>Are you sure you want to buy a <b class=b1>Defensive Turret</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else :
			"<b class=b1>Defensive Turret</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>defensive_turret</b> Credits.<p>"

			take_cash(defensive_turret)

			dbn("update {db_name_ships set upgrades = upgrades - 1,num_dt = num_dt + 1 where ship_id = 'user[ship_id]'")
			user_ship.upgrades --
			user_ship.num_dt ++
		
	


if(isset(b_buy):
	#ensure users don't enter equations in place of numbers.
	settype(num_up, "integer")

	#user should type something in.
	if num_up < 1:
		"Please select a number of upgrades to purchase and fit to the <b>user_ship[ship_name]</b>.<p>"

	#have some free pods?
	elif num_up > user_ship.upgrades']:
		"You do not have that many upgrade pods.<p>"

	#enough money?
	 else :if((num_up * basic_cost) > user.cash']:
		"You do not have enough money for that many upgrade pods.<p>"

	#user not allowed more than 5k figs unless the ship is a battleship.
	 else :if((user_ship.max_fighters + (fighter_inc * num_up) >= 5000) and !ereg("bs",user_ship.config and b_buy == 1:
		"It is against regulations to have more than 4,999 fighter capacity on a ship unless the ship is registered as a battleship.<br>To do that you'll have to purchase a battleship upgrade from Bilkos.<p>"

	#not allowed shields on a SJ ship.
	elif ereg("sj",user_ship.config and b_buy == 2 :
		"It is not possible to fit shield capacity to a ship that has a <b class=b1>SubSpace Jump Drive</b> on.<p>The law's of physics are very uncompromising on this point."

	#confirmation
	# else :
	#	get_var('Buy Multiple Upgrades',filename,'Are you sure you want to do a Mass Upgrade?','sure','')

	else :

		if b_buy == 1 :
			up_str = "Fighters"
			up_sql = "max_fighters"
			inc_amount = fighter_inc

		elif b_buy == 2 :
			up_str = "Shields"
			up_sql = "max_shields"
			inc_amount = shield_inc

		 else :{
			up_str = "Cargo Bays"
			up_sql = "cargo_bays"
			inc_amount = cargo_inc
		
		cost = num_up * basic_cost
		inc_amount *= num_up


		"You have increased the <b class=b1>user_ship[ship_name]'s</b> up_str capacity by <b>inc_amount</b> for <b>cost</b> Credits. <p>"
		take_cash(cost)
		dbn("update {db_name_ships set up_sql = up_sql + 'inc_amount', upgrades = upgrades - 'num_up' where ship_id = 'user_ship[ship_id]'")
		user_ship.upgrades -= num_up
		user_ship[up_sql] += inc_amount
		if up_sql == "cargo_bays" :
			user_ship.empty_bays += inc_amount
		
	


#ensure user has some upgrade pods free.
if user_ship.upgrades < 1 :
	print_page("Accessories & Upgrades","This Ship has no Upgrade pods available.<p>Our upgrades require special 'pods'. As this ship as no such pods, we cannot do anything to it.")

else :


	"<br>This ship has <b>user_ship[upgrades]</b> upgrade Pod(s) available. Each upgrade will use one pod.<br>"
	"<br>Warning! Once brought, an upgrade cannot be sold!<p>"

	if user_ship.upgrades > 1:
		"<table><tr><td>"
	

	"Basic Upgrades"
	make_table(array("Item Name","Item Cost"))
	make_row(array("fighter_inc Fighter Capacity",basic_cost,"<a href=filename?buy=1>Buy</a>"))
	make_row(array("shield_inc Shield Capacity",basic_cost,"<a href=filename?buy=2>Buy</a>"))
	make_row(array("cargo_inc Cargo Capacity",basic_cost,"<a href=filename?buy=3>Buy</a>"))
	"</table>"


	if user_ship.upgrades > 1:
		"</td><td align=right>"
		"<p>Mass upgrades:"
		"<FORM method=get action=upgrade.php>"
		"&nbsp&nbsp&nbsp&nbsp<select name=b_buy>"
		"<option value=1> + fighter_inc Fighter Capacity"
		"<option value=2> + shield_inc Shield Capacity"
		"<option value=3> + cargo_inc Cargo Capacity"
		"</select>"
		" - <input type='text' size='3' name='num_up'>"
		"<p><INPUT type=submit value=Submit></form><p>"
		"</td></tr></table>"
	

	"<br>This ship has <b>upgrade_pods[0]</b> upgrade Pod(s) available. Each upgrade will use one pod.<br>"
	"<br>Warning! Once brought, an upgrade cannot be sold!"

	"Basic Upgrades"
	make_table(array("Item Name","Item Cost"),"75%")
	make_row(array("fighter_inc Fighter Capacity",basic_cost,"<a href=filename?buy=1>Buy</a>"))
	 make_row(array("shield_inc Shield Capacity",basic_cost,"<a href=filename?buy=2>Buy</a>"))
	 make_row(array("cargo_inc Cargo Capacity",basic_cost,"<a href=filename?buy=3>Buy</a>"))

	"</table><br><br>Turrets"
	make_table(array("Item Name","Notes","Item Cost"),"75%")
	 make_row(array("Pea Shooter","Max of max_ot per ship. Cost based on ship size.",pea_turret,"<a href=filename?buy=10>Buy</a>"))
	 make_row(array("Defensive Turret","Max of max_dt per ship. Cost based on ship size.",defensive_turret,"<a href=filename?buy=11>Buy</a>"))

	"</table><br><br>Propulsion Upgrades"
	make_table(array("Item Name","Notes","Item Cost"),"75%")
	 make_row(array("Transwarp Drive","Cannot be fitted to a ship with a Subspace Jump Drive",transwarp_cost,"<a href=filename?buy=8>Buy</a>"))
	if "sj",user_ship[config]) :
		 make_row(array("WormHole Stabiliser","Can only be installed on ships with a Subspace Jump Drive.",stabiliser_upgrade,"<a href=filename?buy=6>Buy</a>"))
	

	"</table><br><br>Misc"
	make_table(array("Item Name","Notes","Item Cost"),"75%")
	 make_row(array("Shrouding Unit","Provides High Stealth. Cost based on ship size.",cloak_cost,"<a href=filename?buy=4>Buy</a>"))
	 make_row(array("Scanner","Allows Detection of Cloaked Ships",scanner_cost,"<a href=filename?buy=7>Buy</a>"))
	 make_row(array("Shield Charging Upgrade","Increases Shield Charge Rate for the ship.",shield_charger,"<a href=filename?buy=5>Buy</a>"))

	"</table>"
	"<p><a href=help.php?upgrades=1 target=_blank>Information about Accessories & Upgrades</a>"

	rs = "<p><a href=earth.php>Return to Earth</a>"

	print_page("Accessories & Upgrades",error_str)

