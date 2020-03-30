if( user.location  not  planet.location ) :
	out = "That planet is not in this system."
elif ( planet.login_id  not  user.login_id ) :
	out = "Only the planet owner may authorise that action."
#build missile
def build_omega_missile():
	header = "Omega Missile Construction"
	if(user.cash < 100000 or  planet.elect] < 50 or  planet.metal] < 200 or  planet.fuel] < 100) : #134800
		out + "You can not afford a <b class=b1>Omega Missile</b>."
	elif (enable_superweapons == 0):
		out + "Admin has disabled the ability to use these weapons, as such, building a missile is pointless"
	elif (user.turns < 10):
		out + "You to do not have enough turns to build a <b class=b1>Omega Missile</b>."
	elif ( planet.missile] not 0) :
		out + "You already have a <b class=b1>Omega Missile</b> on this planet."
	elif (sure not 'yes') :
		get_var('Build Omega Missile','add_planetary.php','Are you sure you want to build a <b class=b1>Omega Missile</b>?','sure','yes')
	else :
		take_cash(100000)
		charge_turns(10)
		out + "Your new <b class=b1>Omega Missile</b> is ready, and your planet has been debited the materials needed to construct the Missile."
		dbn("update :db_name}_planets set missile = '-1', elect = elect - 50, metal=metal-200,fuel=fuel-100 where planet_id =  planet.planet_id]")

#build a launch pad
def build_launch_pad() :
	header = 'Launch Pad Construction'
	if ( user.cash  < 100000 or  planet.elect  < 200 or planet.metal  < 100 or  planet.fuel  < 100) :
		out + "<p>You can not afford a Missile Launch Pad</p><p>Required: 100,000 cash, 100 metal, and 100 fuel.</p>"
	elif  (enable_superweapons == 0) :
		out + "<p>Admin has disabled the ability to use these weapons, as such, building a missile pad is pointless.</p>"
	elif ( planet.launch_pad != 0) :
		out + "You already have a <b class=b1>Missile Launch Pad</b> on this planet."
	elif (sure not 'yes') :
		get_var('Build Missile Launch Pad','add_planetary.php','Are you sure you want to build a <b class=b1>Missile Launch Pad</b>?','sure','yes')
	else :
		take_cash(100000)
		out + "Construction of the <b class=b1>Missile Launch Pad</b> is under way.<br>It will be completed in <b>24hrs</b>.<br>Your planet has been debited the materials needed to construct the Pad."
		dbn("update :db_name}_planets set launch_pad = '25', elect = elect - 200, metal=metal-100,fuel=fuel-100 where planet_id =  planet.planet_id]")
	}

#build a research facility
}elseif (flag_research == 1 and isset(research_fac)) :
	header = "Research Facility"

	#check to see how many research centres the user has.
	db("select count(planet_id) from :db_name}_planets where research_fac = 1 and login_id = user.login_id]")
	num_research = dbr()
	if( user.cash  < research_fac_cost) :
		out + "You can not afford a <b class=b1>Research Facility</b>."
	elif ( planet.'research_fac  not 0) :
		out + "You already have a <b class=b1>Research Facility</b> on this planet."
	elif (num_research[0] > 1) :
		out + "You may only own two research centres at a time."
	elif (!isset(sure)) :
		get_var('Buy Research Facility','add_planetary.php','Are you sure you want to purchase a <b class=b1>Research Facility</b>?','sure','yes')
	else :
		take_cash(research_fac_cost)
		out + "You have purchased and installed a <b class=b1>Research Facility</b> on the planet <b class=b1> planet.planet_name]</b> at the cost of <b>research_fac_cost</b> Credits.<p>Note: You are only allowed two research centres at a time, with a maximum of 1 per planet."
		dbn("update :db_name}_planets set research_fac = '1' where planet_id =  planet.planet_id]")
	}

#build a shield generator
elif shield_gen) :
	header = "Shield Generator Construction"
	if( user.cash  < shield_gen_cost) :
		out + "You can not afford a <b class=b1>Shield Generator</b>."
	elif ( planet.'shield_gen  not 0) :
		out + "You already have a <b class=b1>Shield Generator</b> on this planet."
	elif (!isset(sure)) :
		get_var('Buy Shield Generator','add_planetary.php','Are you sure you want to purchase a <b class=b1>Shield Generator</b>?','sure','yes')
	else :
		take_cash(shield_gen_cost)
		out + "You have purchased and installed a <b class=b1>Shield Generator</b> on the planet <b class=b1> planet.planet_name]</b> at the cost of <b>shield_gen_cost</b> Credits."
		dbn("update :db_name}_planets set shield_gen = '3' where planet_id =  planet.planet_id]")
		 planet.'shield_gen  = 3
	}

else :
	out = "You shouldn't be at this page without a reason"
}

print_page(header, out . "<p><a href=\"planet.php?planet_id=planet_id\">Back to The Planet</a></p>")
