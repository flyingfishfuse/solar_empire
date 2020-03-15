
devinfo = ''

    systems = database.session.query(SystemInfo).all()
    new_sys = []
	links_array = array()

# dbquery to get all systems
#aims to stop one way links from being created
#checks all systems that have already been linked to see what links have already been created to this location.
def pre_linked(systems, present_system):
    #systems = database.session.query(SystemInfo).all()
	links_array = []
	for system in systems:
        #if there IS a link...if NOT EMPTY
		if system.links != "" :
			present_links = split(',', system.links)
            for link in present_links:
                if present_system.links == link:
				links_array.append(systems.links)
	return links_array

#link the systems
#new functions...
# after creating systems, itterate over them
# subtracty and add 1 to each x/y location to get neighbors
# create num_links as 
def link_systems_1(systems):
	for system in systems : 
		numlinks = randint(return_game_var('min_links') , return_game_var('max_links')
		#find the closest systems to the present system. when numlinks closest found, link them
		for each get_closest_systems(system,systems,numlinks) as linksys : 
			make_link(systems[system_num],systems[linksys['num']])
		if devinfo : 
			print_to_screen("<div id=\"linksys1" . system.system_num + "\">-Created " + \
			 numlinks + " links in system #" + (system_num + 1) .
			 "</div><script type=\"text/javascript\">document.all.linksys1system[num].scrollIntoView()</script>"
		
	

	#add wormholes if appropriate
	if return_game_var('wormholes'] > 0 && return_game_var('numsystems'] > 15 :
		num_worms = ceil(return_game_var('numsystems'] / 35)#num wormholes to make

		worms_placed = array()

		for(a=1 a <= num_worms a++ :#loop through

			start_loc = randint(2,return_game_var('numsystems'])
			while(system_has_wormhole(worms_placed, start_loc) : 
				start_loc = randint(2,return_game_var('numsystems'])
			
			worms_placed[] = start_loc#push into wormhole checking array.


			end_loc = randint(1,return_game_var('numsystems'])
			while(system_has_wormhole(worms_placed, end_loc) : 
				end_loc = randint(1,return_game_var('numsystems'])
			
			worms_placed[] = end_loc#push into wormhole checking array.

			#make them permanent
			systems[start_loc -1]['wormhole'] = end_loc
			if (randint(0,10) > 5 : #two way wormhole
				systems[end_loc -1]['wormhole'] = start_loc
			
		
	


#check to see if a star system has a wormhole in it already.
def system_has_wormhole(&worms_placed, &this_worm : 
	for each worms_placed as worm : 
		if worm == this_worm : 
			return true
		
	
	return false


#def that determines if it's ok to link to a system
def ok_to_link(&sys1, &sys2 : 
	global UNI

	#linking to itself.
	if sys1['num'] == sys2['num'] : 
		return false
	

	sys2_links = explode(',', sys2['links'])

	#return o.k. if target still has empty links || already linked.
	if (count(sys2_links) < return_game_var('maxlinks']) || in_array(sys1['num'], sys2_links) : 
		return true
	 else {
		return false
	


#find the closest systems to link to.
/*
sys =  linking from
systems = all systens
howmany = number of closest systems to return
*/
def get_closest_systems(sys, systems, howmany : 
	global UNI

	#check to see which systems have already linked to this one.
	systems_to_link = pre_linked(systems, sys['num'])
	howmany -= count(systems_to_link)
	if howmany < 1 :
		return systems_to_link
	

	#establish the distance of all stars in relation to this one
	dists = array()
	for each systems as system : 
		if ok_to_link(sys, system) : 
			dists[system_num] = get_sys_dist(sys,system)
		
	
	reset(dists)
	asort(dists,SORT_NUMERIC)

	#link to as many of the closest systems as can.
	while(count(systems_to_link) < howmany : 
		if !present_sys = each(dists) : #get a system out of the dist array. RETURN if none.
			return systems_to_link
		

		#too far away to be linked to (Sol System excepted).
		if present_sys['value'] > return_game_var('link_dist'] && return_game_var('link_dist'] > 0 && sys['num'] != 0 :
			return systems_to_link
		

		systems_to_link[] = systems[present_sys['key']]
	
	return systems_to_link


#work out if a system is too close to another system
def system_too_close(sys,systems,within) : 
	for each in systems : 
		if system_num == sys['num'] : #same system
			continue
		
		if dist = get_sys_dist(sys,system) < within : #too close
			return true
		
	
	return false


#make a single link between two systems.
def make_link(&sys1,&sys2 : 
	if (string)sys1['links'] != "" : 
		sys1warps = explode(',',sys1['links'])
		if !in_array(sys2['num'],sys1warps) : 
			sys1warps[] = sys2['num']
			sys1['links'] = implode(',',sys1warps)
		
	 else {
		sys1['links'] = sys2['num']
	
	if (string)sys2['links'] != "" : 
		sys2warps = explode(',',sys2['links'])
		if !in_array(sys1['num'],sys2warps) : 
			sys2warps[] = sys1['num']
			sys2['links'] = implode(',',sys2warps)
		
	 else {
		sys2['links'] = sys1['num']
	


#work out the distance (in pixels) between two star systems.
def get_sys_dist(&sys1,&sys2 : 
	return (int)round(sqrt(pow(sys1['x_loc']-sys2['x_loc'],2) + pow(sys1['y_loc']-sys2['y_loc'],2)))


#generate the three global maps.
def render_global_se1(game_id : 
	global UNI,devinfo,games_dir, systems,preview, directories, gen_new_maps, uv_show_warp_numbers

	size = return_game_var('size'] + (return_game_var('map_border'] * 2)
	offset_x = return_game_var('map_border']
	offset_y = return_game_var('map_border']
	central_star = 1

	im = imagecreatetruecolor(size,size)

	#allocate the colours
	color_bg = ImageColorAllocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2])
	color_st = ImageColorAllocate(im, return_game_var('num_color'][0], return_game_var('num_color'][1], return_game_var('num_color'][2])
	color_sd = ImageColorAllocate(im, return_game_var('star_color'][0], return_game_var('star_color'][1], return_game_var('star_color'][2] )
	color_sl = ImageColorAllocate(im, return_game_var('link_color'][0], return_game_var('link_color'][1], return_game_var('link_color'][2] )
	color_sh = ImageColorAllocate(im, return_game_var('num_color3'][0], return_game_var('num_color3'][1], return_game_var('num_color3'][2] )
	color_l = ImageColorAllocate(im, return_game_var('label_color'][0], return_game_var('label_color'][1], return_game_var('label_color'][2] )
	worm_1way_color = ImageColorAllocate(im,return_game_var('worm_one_way_color'][0], return_game_var('worm_one_way_color'][1], return_game_var('worm_one_way_color'][2] )
	worm_2way_color = ImageColorAllocate(im,return_game_var('worm_two_way_color'][0], return_game_var('worm_two_way_color'][1], return_game_var('worm_two_way_color'][2] )

	#get the star systems from the Db if using pre-genned map.
	if (isset(gen_new_maps) : 
		db("select (star_id -1) as num, x_loc, y_loc, wormhole, CONCAT(link_1 -1, ',', link_2 -1, ',', link_3 -1, ',', link_4 -1, ',', link_5 -1, ',', link_6 -1) as links from {game_id_stars order by star_id asc")
		while(systems[] = dbr(1)) #dump all entries into systems.
		unset(systems[count(systems) - 1]) #remove a surplus entry
	

	#process stars
	for each systems as star :
		if !empty(star['links']) :#don't link all systems to 1 automatically.
			star_links = array_map("plus_one", explode(',', star['links']))
			star_id = star['num'] + 1

			for each star_links as link : #make star links
				if link < 1 :
					continue 1
				
				other_star = systems[link -1]#set other_star to the link destination.
				imageline(im, (star['x_loc'] + offset_x), (star['y_loc'] + offset_y), (other_star['x_loc'] + offset_x), (other_star['y_loc'] + offset_y), color_sl)
			
		

		if !empty(star['wormhole']) : #Wormhole Manipulation
			other_star = systems[star['wormhole'] -1]
			if other_star['wormhole'] == star_id : #two way
				imageline(im, (star['x_loc'] + offset_x), (star['y_loc'] + offset_y), (other_star['x_loc'] + offset_x), (other_star['y_loc'] + offset_y), worm_2way_color)
			 else { #one way
				imageline(im, (star['x_loc'] + offset_x), (star['y_loc'] + offset_y), (other_star['x_loc'] + offset_x), (other_star['y_loc'] + offset_y), worm_1way_color)
			
		
	

	for each systems as star : #place the star itself. This is done after the lines, so the text comes on top.
		star_id = star['num'] + 1
		central_star = 1

		if star_id == central_star : #Place and Highlight central system
			imagestring(im, return_game_var('num_size'], (star['x_loc'] + offset_x + 3), (star['y_loc'] + offset_y - 4), star_id, color_sh)
			imagesetpixel(im, (star['x_loc'] + offset_x), (star['y_loc'] + offset_y), color_sh)
		 else { #place normal Star
			if uv_show_warp_numbers == 1 : 
				imagestring(im, return_game_var('num_size'], (star['x_loc'] + offset_x + 3), (star['y_loc'] + offset_y - 4), star_id, color_st)
			
			imagesetpixel(im, (star['x_loc'] + offset_x), (star['y_loc'] + offset_y), color_sd)
		
	


	#for just a preview we can quite while we're ahead.
	if (isset(preview) : 
		header("Content-type: image/png")
		imagepng(im)
		imagedestroy(im)
		exit
	

	#Draw title
	imagestring(im, 5, ((size/2)-80), 5, "Universal Star Map", color_l)

	#Create buffer image
	bb_im = imagecreatetruecolor((return_game_var('size'] + return_game_var('localmapwidth']), (return_game_var('size'] + return_game_var('localmapheight']))

	ImageColorAllocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2])
	ImageCopy(bb_im, im, (return_game_var('localmapwidth'] / 2), (return_game_var('localmapheight'] / 2), offset_x, offset_y, return_game_var('size'], return_game_var('size'])

	#Create printable map
	p_im = imagecreatetruecolor(size,size)
	ImageColorAllocate(p_im, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2])
	ImageCopy(p_im, im, 0, 0, 0, 0, size, size)

	#Replace colors
	index = ImageColorExact(p_im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2])
	ImageColorSet(p_im, index, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2])
	index = ImageColorExact(p_im, return_game_var('link_color'][0], return_game_var('link_color'][1], return_game_var('link_color'][2])
	ImageColorSet(p_im, index, return_game_var('print_link_color'][0], return_game_var('print_link_color'][1], return_game_var('print_link_color'][2])
	index = ImageColorExact(p_im, return_game_var('num_color'][0], return_game_var('num_color'][1], return_game_var('num_color'][2])
	ImageColorSet(p_im, index, return_game_var('print_num_color'][0], return_game_var('print_num_color'][1], return_game_var('print_num_color'][2])
	index = ImageColorExact(p_im, return_game_var('num_color3'][0], return_game_var('num_color3'][1], return_game_var('num_color3'][2])
	ImageColorSet(p_im, index, return_game_var('print_num_color'][0], return_game_var('print_num_color'][1], return_game_var('print_num_color'][2])
	index = ImageColorExact(p_im, return_game_var('star_color'][0], return_game_var('star_color'][1], return_game_var('star_color'][2])
	ImageColorSet(p_im, index, return_game_var('print_star_color'][0], return_game_var('print_star_color'][1], return_game_var('print_star_color'][2])

	#Draw new label
	ImageFilledRectangle(p_im, 0, 0, size, return_game_var('map_border'], ImageColorExact(p_im, return_game_var('print_bg_color'][0], return_game_var('print_bg_color'][1], return_game_var('print_bg_color'][2]))
	imagestring(p_im, 5, ((size/2)-80), 5, "Printable Star Map", ImageColorExact(p_im, return_game_var('print_label_color'][0], return_game_var('print_label_color'][1], return_game_var('print_label_color'][2]))

	#Save map and finish
	if (!file_exists("img/{game_id_maps") : 
		mkdir("img/{game_id_maps", 0777)
	
	ImagePng(im, "img/{game_id_maps/sm_full.png")
	ImagePng(bb_im, "img/{game_id_maps/bb_full.png")
	ImagePng(p_im, "img/{game_id_maps/psm_full.png")

	if devinfo : 
		print_to_screen(("<br><br><br><hr><img src='directories[images]/{game_id_maps/sm_full.png' onLoad='this.scrollIntoView()'>")

	
	ImageDestroy(im)
	ImageDestroy(bb_im)
	ImageDestroy(p_im)


#draw the local maps.
def renderLocal(game_id : 
	global UNI, devinfo, directories

	if (!file_exists('img/' . game_id . '_maps') : 
		trigger_error('Map image is missing - dir does not exist', E_USER_ERROR)
	

	full_map = imagecreatefrompng("img/{game_id_maps/bb_full.png")

	db("select star_id, x_loc, y_loc from {game_id_stars")
	while(star = dbr() : 

		im = imagecreatetruecolor(return_game_var('localmapwidth'], return_game_var('localmapheight'])

		color_bg = color_bg = imagecolorallocate(im, return_game_var('bg_color'][0], return_game_var('bg_color'][1], return_game_var('bg_color'][2])
		color_ht = imagecolorallocate(im, return_game_var('num_color2'][0], return_game_var('num_color2'][1], return_game_var('num_color2'][2])
		color_hd = imagecolorallocate(im, return_game_var('num_color2'][0], return_game_var('num_color2'][1], return_game_var('num_color2'][2])

		imagecopy(im, full_map, 0, 0, star['x_loc'], star['y_loc'], return_game_var('localmapwidth'], return_game_var('localmapheight'])

		imagestring(im, return_game_var('num_size'], (return_game_var('localmapwidth'] / 2) + 3,
		 (return_game_var('localmapheight'] / 2) - 4, "star[star_id]", color_ht)
		imagesetpixel(im, (return_game_var('localmapwidth'] / 2), (return_game_var('localmapheight'] / 2), color_hd)

		imagepng(im, 'img/' . game_id . '_maps/sm' . star['star_id'] . '.png')
		if devinfo : 
			print_to_screen(("<br><img src='img/{game_id_maps/smstar[star_id].png' onLoad='this.scrollIntoView()'>")

		

		imagedestroy(im)
	

	imagedestroy(full_map)



def plus_one(a : 
	return a + 1


?>