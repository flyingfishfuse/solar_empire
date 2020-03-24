import PIL
from PIL import *
import solar_empire
from solar_empire import *
from solar_empire.inc.configuration_options import *
from solar_empire.universe_build.generator_functions import *
from solar_empire.inc.common_include import *
from solar_empire.models.user_models import *
from solar_empire.models.ship_models import *
from solar_empire.models.social_models import *
from solar_empire.models.storekeeper_models import *
from solar_empire.models.resource_models import *
from solar_empire.models.equipment_models import *
from solar_empire.models.system_models import *

devinfo = ''
systems = database.session.query(SystemInfo).all()
new_sys = []
links_array = array()

# dbquery to get all systems
#aims to stop one way links from being created
#checks all systems that have already been linked to see what links have already been created to this location.
def pre_linked(systems, present_system):
    systems = database.session.query(SystemInfo).all()
	links_array = []
	for system in systems:
        #if there IS a link...if NOT EMPTY
		if system.links != "" :
            for link in system.links:
                for other_link in present_system.links:
					if link == other_link:
						links_array.append(systems.links)
	return links_array

def game_grid(map_height:int, map_width:int):
    """
    This function generates the grid, 
    with size_x and size_y constraints
    """
    # declare the existance of a dimension
    # (I choose for this to be silly and diffucult to comprehend)
    #empty_pie = numpy.zeros(size_y,size_x)
    a = []
    x = 0
    y = 0
    # we have to account for indexing differences between 
    # types and methods
    x_max = map_width + 1
    y_max = map_height + 1
    #map_size = x * y
    def make_x(x_c,y_c):
        for each in range(0,x_max):   
            a.append([x_c,y_c])
            x_c = x_c+1
        # now we have an array of a[[1,y]...[100,y]]
    #make y cols to 100, populating with make_x() to generate x rows
    for coords in range(0,y_max):
        make_x(x,y)
        y = y+1
    return a

def get_closest_systems(system:int):
	"""
	system is a system_ID
	returns an array of x,y locations representing linked systems
	In the form: 
	a = [[1,0]...[100,0],[1,1]...[1,100]...[100,100]]
	where length of x_max in a[x][y] == num_links between systems 
	# System 1
	a[0]     == [0, 0]
	a[0][0]  ==  0
	a[0][1]  ==  0
	# System 2
	a[1]     == [1 , 0]
	a[1][0]  ==  1
	a[1][1]  ==  0
	# System 101
	a[2]     == [0 , 1]
	a[2][0]  ==  0 x-coord
	a[2][1]  ==  1 y-coord
	#...and so on...
	"""
	co_ord_list = []
	for star_system in database.session.query(SystemInfo).all()
		co_ord_list.append(star_system.links)
	pass 

def return_system_by_id(sysID:int)
	"""
	Returns the system object from the database matching 
	The supplied system ID
	"""
	return database.session.query(SystemInfo).filter_by(SystemInfo.system_id = sysID)

def make_link(sys1_id:int , sys2_id:int):
	"""
	Makes a travel link fromv system to neighbors
	"""
	system_1 = return_system_by_id(sys1_id)
	system_2 = return_system_by_id(sys2_id)
	#can I do this? Only testing will tell!
	# appends the system id of other system to "links"
	system_1.links = system_1.links.append(system_2.system_id)
	system_2.links = system_2.links.append(system_1.system_id)

def make_link_one_way(from_system, to_system):
	"""
	makes a one way link between systems
	"""
	system_1 = return_system_by_id(from_system)
	system_2 = return_system_by_id(to_system)
	#can I do this? Only testing will tell!
	# appends the system id of other system to "links"
	system_1.links = system_1.links.append(system_2.system_id)

def system_has_wormhole(worms_placed, location):
	"""
	This returns true if system at location has a wormhole link
	loops over an array of type []

	"""
	pass

# subtract and add 1 to each x/y location to get neighbors
# create num_links as 
#the artist previously known as function link_systems_1
def initial_system_linking():
	systems = database.session.query(SystemInfo).all()
	for system in systems : 
		#random number of links per system, between man/max
		numlinks = randint(return_game_var('min_links') , return_game_var('max_links')
		#find the closest systems to the present system. when numlinks closest found, link them
		for each in get_closest_systems(system) as linksys : 
			make_link(system.system_id,linksys.system_id)
		if devinfo : 
			print_to_screen("<div id=\"linksys1" . system.system_num + "\">-Created " + \
			 numlinks + " links in system #" + (system_num + 1) + \
			 "</div><script type=\"text/javascript\">document.all.linksys1system[num].scrollIntoView()</script>"
		#add wormholes if appropriate
		if return_game_var('wormholes') > 0 and return_game_var('numsystems') > 15 :
			num_worms = ceil(return_game_var('numsystems') / 35)
			#num wormholes to make
			worms_placed = array()
		for range(1,num_worms):
			start_loc = randint(2,return_game_var('numsystems'))
			end_loc   = randint(1,return_game_var('numsystems'))
			if not system_has_wormhole(worms_placed, start_loc) and not system_has_wormhole(worms_placed, end_loc): 
				place_wormhole(start_loc,end_loc)

#def that determines if it's ok to link to a system
#return o.k. if target still has empty links || already linked.
	#if count(sys2.links) < return_game_var('maxlinks') or in_array(sys1.num, sys2.links) : 
	#	return True
	#else:
	#	return False
#find the closest systems to link to.
#sys =  linking from
#systems = all systens
#howmany = number of closest systems to return

#def get_closest_systems(sys, systems, howmany : 
	#check to see which systems have already linked to this one.
	#establish the distance of all stars in relation to this one
	#link to as many of the closest systems as can.
	#too far away to be linked to (Sol System excepted).

#work out if a system is too close to another system
def system_too_close(sys,systems,within) : 
	for each in systems : 
		if system_num == sys : #same system
			continue
		
		if dist = get_sys_dist(sys,system) < within : #too close
			return true
		
	
	return false

#work out the distance (in pixels) between two star systems.
def get_sys_dist(sys1,sys2) : 
	star1 = return_system_by_id(sys1)
	star2 = return_system_by_id(sys2)
	return round(sqrt(pow(star1.x_loc - star2.x_loc , 2 ) + pow( star1.y_loc - star2.y_loc , 2 )))

#generate the three global maps.
# render_global_sel
def render_global_maps(game_id) : 
	size = return_game_var('size') + (return_game_var('map_border') * 2)
	offset_x = return_game_var('map_border')
	offset_y = return_game_var('map_border')
	central_star = 1
	map_image = PIL.Image.new("RGB", (size,size))
	color_st = return_game_var('num_color')[0]
	color_sd = return_game_var('star_color')[0]
	color_sl = return_game_var('link_color')[0]
	color_sh = return_game_var('num_color3')[0]
	color_l =  return_game_var('label_color')[0]
	worm_1way_color = return_game_var('worm_one_way_color')
	worm_2way_color = return_game_var('worm_two_way_color')
	#process stars
	# this dude made a function to add one to a number just to add one to all the
	# link numbers... then followed that up with a recursive loop doing the same...
	# Why not just add 2? 
	for star in database.session.query(SystemInfo).all(): #make star links
		star_id = star.system_id # there was a " + 1 " here presumably for the EARF BABEH
								 #... maybe for indexing...  
		other_star = star.link -1#set other_star to the link destination.
		draw = ImageDraw.Draw(map_image)
		line_start = (star.x_loc + offset_x , star.y_loc + offset_y)
		line_end   =  (other_star.x_loc + offset_x , other_star.y_loc + offset_y)
		draw.line(line_start, line_end , color_sl)
		#original comments, please ignore
		#Wormhole Manipulation
		if star.has_wormhole:
			other_star = star.wormhole
			#two way
			if other_star.wormhole == star_id :
				draw.line(line_start, line_end, worm_2way_color)
			#one way
			else:
				draw.line(line_start, line_end, worm_1way_color)
	    #place the star itself. This is done after the lines, so the text comes on top.
		star_id = star.num + 1
		central_star = 1
		#Place and Highlight Earth
		if star_id == central_star : 
			draw.text( (star.x_loc + offset_x + 3 , star.y_loc + offset_y - 4) , "Earth", color_sh)
			draw.point((star.x_loc + offset_x , star.y_loc + offset_y), color_sh)
		#place normal Star
		if uv_show_warp_numbers == 1 : 
			draw.text( (star.x_loc + offset_x + 3 , star.y_loc + offset_y - 4), star.system_id, color_st)
			draw.point(star.x_loc + offset_x , star.y_loc + offset_y) , color_sd)
	#Draw title
	draw.text(((size/2)-80, 5), "Universal Star Map", color_l)
	#Draw new label
	#draw.rectangle(0, 0, print_bg_color)
	draw.text(((size/2)-80), 5, "Printable Star Map", print_label_color)
	#Save map and finish
	map_image.save( "sm_full.png", "png")
