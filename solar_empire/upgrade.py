
	"Error","You are unable to buy Accessories & Upgrades here.")
	"Error","You are unable to buy Accessories & Upgrades here, as you do not have a real ship.")
	"Error","Admin has disabled upgrades for this game.")
#increases in capacity:
fighter_inc = 300
shield_inc = 100
cargo_inc = 100
#costs
basic_cost = 5000		#cost of the 3 basic upgrades.
#turret costs - based on size of ship
pea_turret = round(40000 * (usership.size / 100 * 15
defensive_turret = round(45000 * (usership.size / 100 * 15

#cloak cost also based on siz e of ship
cloak_cost = round(40000 * (usership.size / 100 * 15

scanner_cost = 20000
transwarp_cost = 20000
ramjet_cost = 20000
shield_charger = 20000
stabiliser_upgrade = 65000

#maximum number of each turret type:
max_ot = 5
max_dt = 5


"<p><a href=upgrade.php>Return to Accessories & Upgrades Store</a>"
# checks
	if(buy ==1)  #Fighter capacity
		if(usership.max_fighters + fighter_inc >= 5000) 
			 "It is against regulations to have more than 4,999 fighter capacity on a ship unless the ship is registered as a battleship.<br>To do that you'll have to purchase a battleship upgrade from Bilkos.<p>"
		else:
			 make_basic_upgrade("Fighter","max_fighters",fighter_inc,basic_cost)
			 #Shield Capacity
		if usership.max_shields >=1 :
			 "Ships with Sub-Space Jump drieves are not allowed to have shields on due to technical problems involving the dynamics of warp-point generation.<p>"
		else:
			 make_basic_upgrade("Shield","max_shields",shield_inc,basic_cost)
		

	elif(buy ==3)  #Cargo capacity
		 make_basic_upgrade("Cargo Bay","cargo_bays",cargo_inc,basic_cost)

	elif(buy==4)  #shrouder
		if ("ls",usership.config
			 "This ship already has low stealth. It is not possible to upgrade to high-stealth.<p>"
		elif sure 
			get_var('Buy Scanner',filename,"This device will Highly stealth the ship. Enemy players will only see a distortion, and not be able to target it, unless they have a scanner on their ship.<br>If they do have a scanner they will still not be able to see who owns the ship.<p>Are you sure you want to buy a <b class=b1>Shrouding Unit</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 make_standard_upgrade ("Shrouding Unit", "hs", cloak_cost, 2003)
		

	elif(buy==5)  #Shield Charger
		if (usership.max_shields < 1)
			 "Why do you want a <b class=b1>Shield Charging Upgrade</b> on a ship that has no shield capacity? <br>I advise you re-think your strategy.<p>"
		elif sure 
			get_var('Buy Shield Charging Upgrade',filename,"This upgrade will increase the shield charging rate for this ship.<p>Are you sure you want to buy a <b class=b1>Shield Charging Upgrade</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 make_standard_upgrade ("Shield Charging Upgrade", "sh", shield_charger, 2005)
		

	elif(buy==6)  #Transverser upgrade (wormhole stabiliser)
		if ("sj",usership.config
			 "This ship does not have a <b class=b1>SubSpace Jump Drive</b> and so is not capable of using a <b class=b1>Wormhole Stabiliser</b>.<p>"
		elif sure 
			get_var('Buy Wormhole Stabiliser',filename,"This upgrade will allow your ship to take more than 10 ships with it when sub-space jumping.<br>It will also allow you to auto-shift materials and colonists between planets.<p>Are you sure you want to buy a <b class=b1>Wormhole Stabiliser</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 make_standard_upgrade ("Wormhole Stabiliser", "ws", stabiliser_upgrade, 2006)
		

	elif(buy==7)  #Scanner
		if sure 
			get_var('Buy Scanner',filename,"Are you sure you want to buy a <b class=b1>Scanner</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 make_standard_upgrade ("Scanner", "sc", scanner_cost, 2004)
		

	elif(buy ==8)  #transwarp drive
		if ("sj",usership.config
			 "Your ship has a <b class=b1>SubSpace Jump Drive</b> on, and so can't have a <b class=b1>Transwarp Drive</b>.<p>"
		elif sure 
			get_var('Buy Transwarp Drive',filename,"This upgrade will allow your ship (and any ships following it) to jump a limited distance across the universe. Ideal for peninsula hopping, and getting to star-islands.<p>Are you sure you want to buy a <b class=b1>Transwarp Drive</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 make_standard_upgrade ("Transwarp Drive", "tw", transwarp_cost, 2002)
		

	elif(buy==10)  #Pea Turret
		if(user['cash < pea_turret) 
			 "You can not afford to buy a <b class=b1>Pea Shooter</b>.<p>"
		elseif(!avail_check(2000
			 "This item has not been developed yet.<p>"
		elif (usership.num_ot >= max_ot)
			 "Your ship is already equipped with <b>max_ot</b> <b class=b1>Pea Shooters</b>. <br>The power relays on your ship are unable to cope with any more.<p>"
		elif (usership.upgrades < 1)
			 "This ship does not have any upgrade pods available.<p>"
		elif sure 
			get_var('Buy Pea Shooter',filename,"This upgrade will complement your ships fighters in battle, allowing you to do more damage to the enemy ship(s).<p>Are you sure you want to buy a <b class=b1>Pea Shooter</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 "<b class=b1>Pea Shooter</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>pea_turret</b> Credits.<p>"

			take_cash(pea_turret)

			dbn("update db_name_ships set upgrades = upgrades - 1 ,num_ot = num_ot + 1 where ship_id = 'user[ship_id]'")
			usership.upgrades --
			usership.num_ot ++
		

	elif(buy==11)  #Defensive Turret
		if(user['cash < defensive_turret) 
			 "You can not afford to buy a <b class=b1>Defensive Turret</b>.<p>"
		elseif(!avail_check(2001
			 "This item has not been developed yet.<p>"
		elif (usership.num_dt >= max_dt)
			 "Your ship is already equipped with <b>max_dt</b> <b class=b1>Defensive Turrets</b>. <br>The power relays on your ship are unable to cope with any more.<p>"
		elif (usership.upgrades < 1)
			 "This ship does not have any upgrade pods available.<p>"
		elif sure 
			get_var('Buy Defensive Turret',filename,"This turret will destroy enemy fighters <b class=b1>Before</b> they have a chance to hurt your ship.<p>Are you sure you want to buy a <b class=b1>Defensive Turret</b>, for the <b class=b1>user_ship[ship_name]</b>?",'sure','')
		else:
			 "<b class=b1>Defensive Turret</b>, purchased and installed on the <b class=b1>user_ship[ship_name]</b> for <b>defensive_turret</b> Credits.<p>"

			take_cash(defensive_turret)

			dbn("update db_name_ships set upgrades = upgrades - 1,num_dt = num_dt + 1 where ship_id = 'user[ship_id]'")
			usership.upgrades --
			usership.num_dt ++
		
	


b_buy 
	#ensure users don't enter equations in place of numbers.
	settype(num_up, "integer")

	#user should type something in.
	if(num_up < 1) 
		 "Please select a number of upgrades to purchase and fit to the <b>user_ship[ship_name]</b>.<p>"

	#have some free pods?
	elif(num_up > usership.upgrades) 
		 "You do not have that many upgrade pods.<p>"

	#enough money?
	elif((num_up * basic_cost) > user['cash) 
		 "You do not have enough money for that many upgrade pods.<p>"

	#user not allowed more than 5k figs unless the ship is a battleship.
	elif((usership.max_fighters + (fighter_inc * num_up) >= 5000) && !ereg("bs",usership.config) && b_buy == 1) 
		 "It is against regulations to have more than 4,999 fighter capacity on a ship unless the ship is registered as a battleship.<br>To do that you'll have to purchase a battleship upgrade from Bilkos.<p>"

	#not allowed shields on a SJ ship.
	elif (ereg("sj",usership.config) && b_buy == 2)
		 "It is not possible to fit shield capacity to a ship that has a <b class=b1>SubSpace Jump Drive</b> on.<p>The law's of physics are very uncompromising on this point."

	#confirmation
	#elif sure 
	#	get_var('Buy Multiple Upgrades',filename,'Are you sure you want to do a Mass Upgrade?','sure','')

	else:

		if(b_buy == 1)
			up_str = "Fighters"
			up_sql = "max_fighters"
			inc_amount = fighter_inc

		elif(b_buy == 2)
			up_str = "Shields"
			up_sql = "max_shields"
			inc_amount = shield_inc

		 else
			up_str = "Cargo Bays"
			up_sql = "cargo_bays"
			inc_amount = cargo_inc
		
		cost = num_up * basic_cost
		inc_amount *= num_up


		 "You have increased the <b class=b1>user_ship[ship_name]'s</b> up_str capacity by <b>inc_amount</b> for <b>cost</b> Credits. <p>"
		take_cash(cost)
		dbn("update db_name_ships set up_sql = up_sql + 'inc_amount', upgrades = upgrades - 'num_up' where ship_id = 'user_ship[ship_id]'")
		usership.upgrades -= num_up
		user_ship[up_sql] += inc_amount
		if(up_sql == "cargo_bays")
			usership.empty_bays += inc_amount
		
	


#ensure user has some upgrade pods free.
if(usership.upgrades < 1)
	"Accessories & Upgrades","This Ship has no Upgrade pods available.<p>Our upgrades require special 'pods'. As this ship as no such pods, we cannot do anything to it.")

else:


	 "<br>This ship has <b>user_ship[upgrades]</b> upgrade Pod(s) available. Each upgrade will use one pod.<br>"
	 "<br>Warning! Once brought, an upgrade cannot be sold!<p>"

	if(usership.upgrades > 1) 
		 "<table><tr><td>"
	

	 "Basic Upgrades"
	 make_table(array("Item Name","Item Cost"
	 make_row(array("fighter_inc Fighter Capacity",basic_cost,"<a href=filename?buy=1>Buy</a>"
	 make_row(array("shield_inc Shield Capacity",basic_cost,"<a href=filename?buy=2>Buy</a>"
	 make_row(array("cargo_inc Cargo Capacity",basic_cost,"<a href=filename?buy=3>Buy</a>"
	 "</table>"


	if(usership.upgrades > 1) 
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
	 make_row(array("fighter_inc Fighter Capacity",basic_cost,"<a href=filename?buy=1>Buy</a>"
	  make_row(array("shield_inc Shield Capacity",basic_cost,"<a href=filename?buy=2>Buy</a>"
	  make_row(array("cargo_inc Cargo Capacity",basic_cost,"<a href=filename?buy=3>Buy</a>"

	 "</table><br><br>Turrets"
	 make_table(array("Item Name","Notes","Item Cost"),"75%")
	  make_row(array("Pea Shooter","Max of max_ot per ship. Cost based on ship size.",pea_turret,"<a href=filename?buy=10>Buy</a>"
	  make_row(array("Defensive Turret","Max of max_dt per ship. Cost based on ship size.",defensive_turret,"<a href=filename?buy=11>Buy</a>"

	 "</table><br><br>Propulsion Upgrades"
	 make_table(array("Item Name","Notes","Item Cost"),"75%")
	  make_row(array("Transwarp Drive","Cannot be fitted to a ship with a Subspace Jump Drive",transwarp_cost,"<a href=filename?buy=8>Buy</a>"
	if ("sj",user_ship[config]
		  make_row(array("WormHole Stabiliser","Can only be installed on ships with a Subspace Jump Drive.",stabiliser_upgrade,"<a href=filename?buy=6>Buy</a>"
	

	 "</table><br><br>Misc"
	 make_table(array("Item Name","Notes","Item Cost"),"75%")
	  make_row(array("Shrouding Unit","Provides High Stealth. Cost based on ship size.",cloak_cost,"<a href=filename?buy=4>Buy</a>"
	  make_row(array("Scanner","Allows Detection of Cloaked Ships",scanner_cost,"<a href=filename?buy=7>Buy</a>"
	  make_row(array("Shield Charging Upgrade","Increases Shield Charge Rate for the ship.",shield_charger,"<a href=filename?buy=5>Buy</a>"

	 "</table>"
	 "<p><a href=help.php?upgrades=1 target=_blank>Information about Accessories & Upgrades</a>"

	"<p><a href=earth.php>Return to Earth</a>"

	"Accessories & Upgrades",)



#function for adding 'normal' upgrades to a ship.
function make_basic_upgrade (upgrade_str, upgrade_sql, inc_amount, cost)
	global user, user_ship, db_name
	if(user['cash < cost) 
		return "You can not afford any of the Basic Upgrades.<p>"
	elif(usership.upgrades < 1) 
		return ""
	else:
		take_cash(cost)
		dbn("update db_name_ships set upgrade_sql = upgrade_sql + 'inc_amount', upgrades = upgrades - 1 where ship_id = 'user_ship[ship_id]'")
		usership.upgrades --
		user_ship[upgrade_sql] += inc_amount

		if(upgrade_sql == "cargo_bays")
			usership.empty_bays += cargo_inc
		

		return "You have increased the <b class=b1>user_ship[ship_name]s</b> upgrade_str capacity by <b>inc_amount</b> for <b>cost</b> Credits. <p>"
	


?>
