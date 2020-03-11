import solar_empire
from solar_empire import *
from solar_empire.models import *
from solar_empire.configuration_options import *
from solar_empire.common_include import *
from solar_empire.names.names import *
from math import *


map_layout               = return_game_var('map_layout')
size                     = return_game_var('size')
num_ports 			     = return_game_var("num_ports")
num_starports 		     = return_game_var("num_starports")
num_systems 		     = return_game_var('num_systems')
num_planets              = return_game_var('num_planets')
num_black_markets        = return_game_var('num_black_markets')
mineral_sum 		     = return_game_var('mineral_total')
metal_sum			     = return_game_var('metal_total')
fuel_sum   		         = return_game_var('fuel_total')
fuel_coef                = return_game_var('fuel_percent_coefficient')
metal_coef               = return_game_var('metal_percent_coefficient')
max_planets_per_system   = return_game_var('max_planets_in_system')
min_dist_between_systems = return_game_var('min_dist_between_systems')

all_systems              = System.query.all()
all_planets              = Planet.query.all()

planet_metal    = random.randint(range ( 100 , metal_total    / num_planets ))
planet_fuel     = random.randint(range ( 100 , fuel_total     / num_planets ))
planet_mineral  = random.randint(range ( 100 , mineral_total  / num_planets ))
planet_organics = random.randint(range ( 100 , organics_total / num_planets ))

max_system_fuel      = return_game_var('max_fuel_per_system')
min_system_fuel      = return_game_var('min_fuel_per_system')
min_metal_per_system = return_game_var('min_metal_per_system')
max_metal_per_system = return_game_var('max_metal_per_system')
##add starports to the universe.
# we map location ID's to system ID's
#generates name for starport
def grab_starport_name():
	return names.gen_name()

def get_starport_by_id(starport_id):
	pass

def add_resources_to_starport_by_id(starport_id):
	get_starport_by_id(starport_id)
	pass

def add_minerals(planetID, amount):
	planet_to_update = database.query.filter_by(planet_id = planetID)
	pass


##def that places random events around the universe.
def random_event_placer():
	pass
	##high level random events

def add_starports_sel():
	for star_port in range( 1 , num_starports - 1):
	#create template dict for new port
		possible_new_starport = { 'system_id' : 0 }
		possible_new_starport['system_id'] = random.randint(2, num_systems)
		#system has no port, build one
		# Add resources to port, subtracting that amount from the universes available pool
		if (system_has_port( possible_new_starport['system_id']) == False ):
			spawned_starport = StarPort(name = grab_starport_name(), system_id = possible_new_starport['system_id'])
# TODO 
			#add_resources_to_starport_by_id(spawned_starport.system_id)
			# save to DB
			#format this string
			print_to_console("<div id=''> USER: {} Created port #{} in location {}</div>")
		else:
			pass
	
##add BM's to the universe
## we tie location id's to market id's to easily place and locate by system
#The location id of a market is the SAME as the location id of the system its in
# the market id of a blackmarket is the SAME as the location id of the system is it in
def add_blackmarket_se1():
	blackmarket_type = 0
 	# copy the code for the starport generator here
	for thing in num_black_markets:
		possible_new_black_market = { 'system_id' : 0 }
		possible_new_black_market['system_id'] = random.randint(1,num_black_markets)
		for spawned_system in list_of_spawned_systems:
			if system_has_black_market(possible_new_black_market['system_id'] == False ):
				spawned_blackmarket = BlackMarket(location = possible_new_black_market['location'], \
											blackmarket_name = return_black_market_name(), \
											blackmarket_id = possible_new_black_market['system_id'] )
# TODO 
			#add_resources_to_blackmarket_by_id(spawned_starport.system_id)
			# save to DB
			# format this text, gotta have a function that lets a user place a blackmarket
			print_to_console("<div id=''>  USER: {user_name} Created Blackmarket # in {place}</div>".format())

##def that will pre-generate planets.
#The same rules for location id's and entity id's apply here
def add_planets(): 
	#account for earth and sol
	# generate the planets
	planetoid_list          = [{'planet_id' : 0} , {'system_id' : 0}]
	coefficient_of_chaos	= random.randint(1, num_systems)
	count                   = 1
	for planetoid in range( 8 , num_planets):
	# adds a randomly selected system id to the planet
	# makes the planet reside in that system
	# multiple planets can have the same system ID
		planetoid_list.append([{'planet_id': count} ,{'system_id' : coefficient_of_chaos}])
		count = count + 1
		Planet(name = names.gen_name('all'))
	#planets have been made, now place them in the universe
	for planet in planetoid_list:
		# wow I hate doing the following, multi-dimensional arrays... ugh!
		# if it wasnt in the loop, to access it you would do 
		# two of the [0] instead of one like so
		# noodles = planetoid_list[0][0]['planet_id']
		planet_id_from_list = planet[0]['planet_id']
		add_minerals(planet_id_from_list)
#TODO Turn this function into an actual fuck nugget of logic you sheer bumbling plunk
	# The planets with these ID's need to have thier SYSTEM_ID variable set to 
	# the system ID of the system they are going to be in
	map_planetID_to_systemID(planetoid_list)
	print_to_console("Randomly placed planets... placed")

##add minerals to the systems
#we modify with a co-ef... gives ability to scale in single var
# set co-eff to 1 to prevent scaling 
def add_minerals(type_of_fill = "random"):
	planetary_figs = (planet_metal + planet_fuel) * 1.1
	for each in num_systems:
		if type_of_fill == "random":
			amount_of_fuel_in_system  = random.randint(min_system_fuel, max_system_fuel) * fuel_coef
			amount_of_metal_in_system = random.randint(min_metal_per_system, max_metal_per_system) * metal_coef
		elif type_of_fill == "scattered":
		# TODO stop making to dos and get this done
			pass
		print("<div id=''>Adding Resources to system #{}</div>").format()

#work out the distance (in pixels) between two star systems.
def distance_between_systems(sys1,sys2 ): 
	distance = sqrt(
				pow( ( sys1['x_loc'] - sys2['x_loc'] ) , 2 ) + \
				pow( ( sys1['y_loc'] - sys2['y_loc'] ) , 2 ) \
				)
	return int(distance)

#work out if a system is too close to another system
def system_too_close( sys, systems, within) : 
	for each in systems: 
		#same system
		if system['num'] == sys['num'] :
			continue
		#too close
		if distance_between_systems( sys , system ) < within :
			return true
	return false


#create the star systems
# i am literally amused to the point of chuckling
# im playing it fast and loose with this and Im sitting here thinking
# "well it looks right, I guess thats good enough"
# I tried to leave the algorhithm alone and just did text replacments
#$ and simple re arrangments
def make_systems_1 (systems) : 
	centre = size / 2 #centre of map
	do_this = 0

	if map_layout == 1 :
		rows = sqrt(num_systems)
		row_dist = size / rows
		per_col = num_systems / rows
		col_dist = size / per_col
		row_count = 0
		col_count = 0
	elif map_layout == 2 :
		one_quart = centre / 4
	elif map_layout == 3 : 
		num_clus = sqrt(num_systems) - 1
		stars_per_cluster = num_systems / num_clus
		cluster_size = (size / (num_clus * 0.55)) / 2 
		offset_cluster = size- cluster_size
		sec_count = 0
		basis_x = centre
		basis_y = centre
	elif map_layout == 5 :
		radius = (size / 2) - 5
		degrees_between_stars = 360 / (num_systems- 1 )
		present_degrees = 0
	elif map_layout == 6 :  
		if num_systems< 50 : 
			radius = size / 2) - 5
			degrees_between_stars = 360 / (num_systems - 1)
			present_degrees = 0
			do_this = 1
		elif num_systems< 200 :  
			ring1_star_count = (num_systems / 100) * 30
			ring2_star_count = num_systems- ring1_star_count-1
			ring3_star_count = 0 #(no third ring)
			ring1_radius = centre / 2
			ring2_radius = centre
			ring1_degrees_between = 360 / ring1_star_count
			ring2_degrees_between = 360 / ring2_star_count
			ring1_preset = 0
			ring2_preset = 0
		else :# 3 rings
			ring1_star_count = (num_systems / 100) * 25 
			ring2_star_count = ((num_systems- ring1_star_count) / 100) * 34
			ring3_star_count = num_systems- ring1_star_count-ring2_star_count-1
			ring1_radius = centre / 1.5
			ring2_radius = centre / 1.2
			ring3_radius = centre
			ring1_degrees_between = 360 / ring1_star_count
			ring2_degrees_between = 360 / ring2_star_count
			ring3_degrees_between = 360 / ring3_star_count
			ring1_preset = 0
			ring2_preset = 0
			ring3_preset = 0
	while len(systems) < num_systems : 
		newname = []
		#planetary slot counter
		planet_slots = random.randint(0,uv_planet_slots)
		#another multi dimensional array to map
		newsystem = [ {'num'   : count} , \
                      {'x_loc' : random.randint(0,size) } , \
					  {'y_loc' : random.randint(0,size) } , \
					  {'links' : '' } , \
					  {'planetary_slots' : planet_slots} ]
		if map_layout == 1 :  #grid layout
			if row_count > rows : #create a new column
				row_count = 0
				col_count + 1
			newsystem[1]['x_loc'] = col_dist * col_count
			newsystem[2]['y_loc'] = row_dist * row_count
			row_count + 1
			while system_too_close(newsystem,systems,min_dist_between_systems):
				newsystem[1]['x_loc'] = randint(0,size)
				newsystem[2]['y_loc'] = randint(0,size)
		elif map_layout == 2 :  #galactic core
			basis = randint(0,100)
			if basis > 75 :  #within centre quarter
				div_by = 4
			elif basis > 50 :  #within centre half
				div_by = 3
			elif basis > 25 :  #within half
				div_by = 2
			else :#anywhere
				div_by = 1
				# div_by = 0 NOOOOOOOOOO!
			while distance_between_systems (systems[0],newsystem) > return_game_var('size']/div_by) || system_too_close(newsystem,systems,return_game_var('mindist']) : 
				newsystem['x_loc')= randint(0,return_game_var('size']
				newsystem['y_loc')= randint(0,return_game_var('size']
			}

		elif return_game_var('map_layout') == 3 :  #clusters
			if sec_count > stars_per_cluster :  #create new cluster
				basis_x = randint(cluster_size, offset_cluster
				basis_y = randint(cluster_size, offset_cluster
				sec_count = 0
			}
			newsystem['x_loc')= randint(0, cluster_size #x_loc - within cluster
			if randint(0,100) > 50 :  #decide offset from center of cluster.
				newsystem['x_loc')+= basis_x
			} else {
				newsystem['x_loc')= basis_x - newsystem['x_loc']
			}
			newsystem['y_loc')= randint(0, cluster_size #y_loc - within cluster
			if randint(0,100) > 50 :  #decide offset from center of cluster.
				newsystem['y_loc')+= basis_y
			} else {
				newsystem['y_loc')= basis_y - newsystem['y_loc']
			}
			while(system_too_close(newsystem,systems,return_game_var('mindist']) : 
				newsystem['x_loc')= randint(0,return_game_var('size']
				newsystem['y_loc')= randint(0,return_game_var('size']
			}
			sec_count++

		elif return_game_var('map_layout') == 4 :  #circle layout
			while((distance_between_systems(systems[0],newsystem) > return_game_var('size']/2) || system_too_close(newsystem,systems,return_game_var('mindist']) : 
				newsystem['x_loc')= randint(0,return_game_var('size']
				newsystem['y_loc')= randint(0,return_game_var('size']
			}

		elif return_game_var('map_layout') == 5 || do_this == 1 :  #ring layout
			newsystem['x_loc')= radius * cos(deg2rad(present_degrees)
			newsystem['y_loc')= radius * sin(deg2rad(present_degrees)
			newsystem['x_loc')+= centre
			newsystem['y_loc')+= centre
			present_degrees += degrees_between_stars#prepare for next star

		elif return_game_var('map_layout') == 6 :  #layered rings layout
			if count <= ring1_star_count : #inner ring
				newsystem['x_loc')= ring1_radius * cos(deg2rad(ring1_preset)
				newsystem['y_loc')= ring1_radius * sin(deg2rad(ring1_preset)
				newsystem['x_loc')+= centre
				newsystem['y_loc')+= centre
				ring1_preset += ring1_degrees_between
			elif count <= (ring2_star_count  + ring1_star_count)|| ring3_star_count == 0 : #second ring
				newsystem['x_loc')= ring2_radius * cos(deg2rad(ring2_preset)
				newsystem['y_loc')= ring2_radius * sin(deg2rad(ring2_preset)
				newsystem['x_loc')+= centre
				newsystem['y_loc')+= centre
				ring2_preset += ring2_degrees_between
#				echo "\n"
			} else {#3rd ring if there is one.
				newsystem['x_loc')= ring3_radius * cos(deg2rad(ring3_preset)
				newsystem['y_loc')= ring3_radius * sin(deg2rad(ring3_preset)
				newsystem['x_loc')+= centre
				newsystem['y_loc')+= centre
				ring3_preset += ring3_degrees_between
			}
		else :#random layout
			while(system_too_close(newsystem,systems,return_game_var('mindist']) : 
				newsystem['x_loc')= randint(0,return_game_var('size']
				newsystem['y_loc')= randint(0,return_game_var('size']
			}
		}
		if extinfo : 
			print("<div id='makesys1count'>-System #".(count+1)." created.<script>document.all.makesys1count.scrollIntoView(</script></div>"

		}
		newsystem['event_random')= 0
		systems[)= newsystem
	}
	#exit
}


#aims to stop one way links from being created
#checks all systems that have already been linked to see what links have already been created to this location.
def pre_linked(systems, present_system : 
	links_array = array(
	foreach(systems as new_sys : 
		if (string)new_sys['links')!= "" : 
			present_links = explode(',', new_sys['links']
			if in_array(present_system, present_links) : 
				links_array[)= systems[new_sys['num']]
			}
		}
	}
	return links_array
}


#link the systems
def link_systems_1 (systems : 
	global UNI,extinfo

	foreach(systems as system : 
		numlinks = randint(return_game_var('minlinks'],return_game_var('maxlinks']

		#find the closest systems to the present system. when numlinks closest found, link them
		foreach (get_closest_systems(system,systems,numlinks) as linksys : 
			make_link(systems[system['num']],systems[linksys['num']]
		}
		if extinfo : 
			print "<div id=\"linksys1" . system['num'). "\">-Created " .
			 numlinks . " links in system #" . (system['num')+ 1) .
			 "</div><script type=\"text/javascript\">document.all.linksys1system[num].scrollIntoView(</script>"
		}
	}

	#add wormholes if appropriate
	if return_game_var('wormholes')> 0 && num_systems> 15 : 
		num_worms = ceil(num_systems / 35#num wormholes to make

		worms_placed = array(

		for(a=1 a <= num_worms a++ : #loop through

			start_loc = randint(2,return_game_var('num_systems']
			while(system_has_wormhole(worms_placed, start_loc) : 
				start_loc = randint(2,return_game_var('num_systems']
			}
			worms_placed[)= start_loc#push into wormhole checking array.


			end_loc = randint(1,return_game_var('num_systems']
			while(system_has_wormhole(worms_placed, end_loc) : 
				end_loc = randint(1,return_game_var('num_systems']
			}
			worms_placed[)= end_loc#push into wormhole checking array.

			#make them permanent
			systems[start_loc -1]['wormhole')= end_loc
			if (randint(0,10) > 5 : #two way wormhole
				systems[end_loc -1]['wormhole')= start_loc
			}
		}
	}
}

#check to see if a star system has a wormhole in it already.
def system_has_wormhole (worms_placed, &this_worm : 
	foreach(worms_placed as worm : 
		if worm == this_worm : 
			return true
		}
	}
	return false
}

#def that determines if it's ok to link to a system
def ok_to_link (sys1, &sys2 : 
	global UNI

	#linking to itself.
	if sys1['num') == sys2['num'] : 
		return false
	}

	sys2_links = explode(',', sys2['links']

	#return o.k. if target still has empty links || already linked.
	if (count(sys2_links) < return_game_var('maxlinks']) || in_array(sys1['num'], sys2_links) : 
		return true
	} else {
		return false
	}
}

#find the closest systems to link to.
/*
sys =  linking from
systems = all systens
howmany = number of closest systems to return
*/
def get_closest_systems(sys, systems, howmany : 
	global UNI

	#check to see which systems have already linked to this one.
	systems_to_link = pre_linked(systems, sys['num']
	howmany -= count(systems_to_link
	if howmany < 1 : 
		return systems_to_link
	}

	#establish the distance of all stars in relation to this one
	dists = array(
	foreach(systems as system : 
		if ok_to_link(sys, system) : 
			dists[system['num'])= distance_between_systems(sys,system
		}
	}
	reset(dists
	asort(dists,SORT_NUMERIC

	#link to as many of the closest systems as can.
	while(count(systems_to_link) < howmany : 
		if !present_sys = each(dists) : #get a system out of the dist array. RETURN if none.
			return systems_to_link
		}

		#too far away to be linked to (Sol System excepted).
		if present_sys['value')> return_game_var('link_dist')&& return_game_var('link_dist')> 0 && sys['num')!= 0 : 
			return systems_to_link
		}

		systems_to_link[)= systems[present_sys['key']]
	}
	return systems_to_link
}

#make a single link between two systems.
def make_link (sys1,&sys2 : 
	if (string)sys1['links')!= "" : 
		sys1warps = explode(',',sys1['links']
		if !in_array(sys2['num'],sys1warps) : 
			sys1warps[)= sys2['num']
			sys1['links')= implode(',',sys1warps
		}
	} else {
		sys1['links')= sys2['num']
	}
	if (string)sys2['links')!= "" : 
		sys2warps = explode(',',sys2['links']
		if !in_array(sys1['num'],sys2warps) : 
			sys2warps[)= sys1['num']
			sys2['links')= implode(',',sys2warps
		}
	} else {
		sys2['links')= sys1['num']
	}
}

#generate the three global maps.
def render_global_se1(game_id : 
	global UNI,extinfo,games_dir, systems,preview, directories, gen_new_maps, uv_show_warp_numbers

	size = size+ (return_game_var('map_border')* 2
	offset_x = return_game_var('map_border']
	offset_y = return_game_var('map_border']
	central_star = 1

	im = imagecreatetruecolor(size,size

	#allocate the colours
	color_bg = ImageColorAllocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2]
	color_st = ImageColorAllocate(im, return_game_var('num_color'][0], return_game_var('num_color'][1], return_game_var('num_color'][2]
	color_sd = ImageColorAllocate(im, return_game_var('star_color'][0], return_game_var('star_color'][1], return_game_var('star_color'][2)
	color_sl = ImageColorAllocate(im, return_game_var('link_color'][0], return_game_var('link_color'][1], return_game_var('link_color'][2)
	color_sh = ImageColorAllocate(im, return_game_var('num_color3'][0], return_game_var('num_color3'][1], return_game_var('num_color3'][2)
	color_l = ImageColorAllocate(im, return_game_var('label_color'][0], return_game_var('label_color'][1], return_game_var('label_color'][2)
	worm_1way_color = ImageColorAllocate(im,return_game_var('worm_one_way_color'][0], return_game_var('worm_one_way_color'][1], return_game_var('worm_one_way_color'][2)
	worm_2way_color = ImageColorAllocate(im,return_game_var('worm_two_way_color'][0], return_game_var('worm_two_way_color'][1], return_game_var('worm_two_way_color'][2)

	#get the star systems from the Db if using pre-genned map.
	if (isset(gen_new_maps) : 
		"select (star_id -1) as num, x_loc, y_loc, wormhole, CONCAT(link_1 -1, ',', link_2 -1, ',', link_3 -1, ',', link_4 -1, ',', link_5 -1, ',', link_6 -1) as links from {game_id}_stars order by star_id asc"
		while(systems[)= 1) #dump all entries into systems.
		unset(systems[count(systems) - 1)#remove a surplus entry
	}

	#process stars
	foreach(systems as star : 
		if !empty(star['links']) : #don't link all systems to 1 automatically.
			star_links = array_map("plus_one", explode(',', star['links'])
			star_id = star['num')+ 1

			foreach(star_links as link :  #make star links
				if link < 1 : 
					continue 1
				}
				other_star = systems[link -1]#set other_star to the link destination.
				imageline(im, (star['x_loc')+ offset_x), (star['y_loc')+ offset_y), (other_star['x_loc')+ offset_x), (other_star['y_loc')+ offset_y), color_sl
			}
		}

		if !empty(star['wormhole']) : #Wormhole Manipulation
			other_star = systems[star['wormhole')-1]
			if other_star['wormhole') == star_id :  #two way
				imageline(im, (star['x_loc')+ offset_x), (star['y_loc')+ offset_y), (other_star['x_loc')+ offset_x), (other_star['y_loc')+ offset_y), worm_2way_color
			else :#one way
				imageline(im, (star['x_loc')+ offset_x), (star['y_loc')+ offset_y), (other_star['x_loc')+ offset_x), (other_star['y_loc')+ offset_y), worm_1way_color
			}
		}
	}

	foreach(systems as star :  #place the star itself. This is done after the lines, so the text comes on top.
		star_id = star['num')+ 1
		central_star = 1

		if star_id == central_star : #Place and Highlight central system
			imagestring(im, return_game_var('num_size'], (star['x_loc')+ offset_x + 3), (star['y_loc')+ offset_y - 4), star_id, color_sh
			imagesetpixel(im, (star['x_loc')+ offset_x), (star['y_loc')+ offset_y), color_sh
		else :#place normal Star
			if uv_show_warp_numbers == 1 : 
				imagestring(im, return_game_var('num_size'], (star['x_loc')+ offset_x + 3), (star['y_loc')+ offset_y - 4), star_id, color_st
			}
			imagesetpixel(im, (star['x_loc')+ offset_x), (star['y_loc')+ offset_y), color_sd
		}
	}


	#for just a preview we can quite while we're ahead.
	if (isset(preview) : 
		header("Content-type: image/png"
		imagepng(im
		imagedestroy(im
		exit
	}

	#Draw title
	imagestring(im, 5, ((size/2)-80), 5, "Universal Star Map", color_l

	#Create buffer image
	bb_im = imagecreatetruecolor((size+ return_game_var('localmapwidth']), (size+ return_game_var('localmapheight'])

	ImageColorAllocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2]
	ImageCopy(bb_im, im, (return_game_var('localmapwidth') / 2), (return_game_var('localmapheight') / 2), offset_x, offset_y, return_game_var('size'], return_game_var('size']

	#Create printable map
	p_im = imagecreatetruecolor(size,size
	ImageColorAllocate(p_im, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2]
	ImageCopy(p_im, im, 0, 0, 0, 0, size, size

	#Replace colors
	index = ImageColorExact(p_im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2]
	ImageColorSet(p_im, index, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2]
	index = ImageColorExact(p_im, return_game_var('link_color'][0], return_game_var('link_color'][1], return_game_var('link_color'][2]
	ImageColorSet(p_im, index, return_game_var('print_link_color'][0], return_game_var('print_link_color'][1], return_game_var('print_link_color'][2]
	index = ImageColorExact(p_im, return_game_var('num_color'][0], return_game_var('num_color'][1], return_game_var('num_color'][2]
	ImageColorSet(p_im, index, return_game_var('print_num_color'][0], return_game_var('print_num_color'][1], return_game_var('print_num_color'][2]
	index = ImageColorExact(p_im, return_game_var('num_color3'][0], return_game_var('num_color3'][1], return_game_var('num_color3'][2]
	ImageColorSet(p_im, index, return_game_var('print_num_color'][0], return_game_var('print_num_color'][1], return_game_var('print_num_color'][2]
	index = ImageColorExact(p_im, return_game_var('star_color'][0], return_game_var('star_color'][1], return_game_var('star_color'][2]
	ImageColorSet(p_im, index, return_game_var('print_star_color'][0], return_game_var('print_star_color'][1], return_game_var('print_star_color'][2]

	#Draw new label
	ImageFilledRectangle(p_im, 0, 0, size, return_game_var('map_border'], ImageColorExact(p_im, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2])
	imagestring(p_im, 5, ((size/2)-80), 5, "Printable Star Map", ImageColorExact(p_im, return_game_var('print_label_color'][0], return_game_var('print_label_color'][1], return_game_var('print_label_color'][2])

	#Save map and finish
	if (!file_exists("img/{game_id}_maps") : 
		mkdir("img/{game_id}_maps", 0777
	}
	ImagePng(im, "img/{game_id}_maps/sm_full.png"
	ImagePng(bb_im, "img/{game_id}_maps/bb_full.png"
	ImagePng(p_im, "img/{game_id}_maps/psm_full.png"

	if extinfo : 
		print("<br><br><br><hr><img src='directories[images]/{game_id}_maps/sm_full.png' onLoad='this.scrollIntoView('>"

	}
	ImageDestroy(im
	ImageDestroy(bb_im
	ImageDestroy(p_im
}

#draw the local maps.
def renderLocal(game_id : 
	global UNI, extinfo, directories

	if (!file_exists('img/' . game_id . '_maps') : 
		trigger_error('Map image is missing - dir does not exist', E_USER_ERROR
	}

	full_map = imagecreatefrompng("img/{game_id}_maps/bb_full.png"

	"select star_id, x_loc, y_loc from {game_id}_stars"
	while(star = ) : 

		im = imagecreatetruecolor(return_game_var('localmapwidth'], return_game_var('localmapheight']

		color_bg = color_bg = imagecolorallocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2]
		color_ht = imagecolorallocate(im, return_game_var('num_color2'][0], return_game_var('num_color2'][1], return_game_var('num_color2'][2]
		color_hd = imagecolorallocate(im, return_game_var('num_color2'][0], return_game_var('num_color2'][1], return_game_var('num_color2'][2]

		imagecopy(im, full_map, 0, 0, star['x_loc'], star['y_loc'], return_game_var('localmapwidth'], return_game_var('localmapheight']

		imagestring(im, return_game_var('num_size'], (return_game_var('localmapwidth') / 2) + 3,
		 (return_game_var('localmapheight') / 2) - 4, "star[star_id]", color_ht
		imagesetpixel(im, (return_game_var('localmapwidth') / 2), (return_game_var('localmapheight') / 2), color_hd

		imagepng(im, 'img/' . game_id . '_maps/sm' . star['star_id'). '.png'
		if extinfo : 
			print("<br><img src='img/{game_id}_maps/smstar[star_id].png' onLoad='this.scrollIntoView('>"

		}

		imagedestroy(im
	}

	imagedestroy(full_map
}


def plus_one(a : 
	return a + 1
}

?>
