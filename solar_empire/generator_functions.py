import solar_empire
from solar_empire import *
from solar_empire.models import *
from solar_empire.configuration_options import *
from solar_empire.common_include import *
from solar_empire.names.names import *


#//deletes all image files.
#function clearImages($path)
num_ports 			= return_game_var("num_ports")
num_starports 		= return_game_var("num_starports")
num_systems 		= return_game_var('num_systems')
num_planets         = return_game_var('num_planets')
num_black_markets   = return_game_var('num_black_markets')
mineral_sum 		= return_game_var('mineral_total')
metal_sum			= return_game_var('metal_total')
fuel_sum   		    = return_game_var('fuel_total')

all_systems         = System.query.all()
all_planets         = Planet.query.all()

planet_metal    = random.randint(range ( 100 , metal_total    / num_planets ))
planet_fuel     = random.randint(range ( 100 , fuel_total     / num_planets ))
planet_mineral  = random.randint(range ( 100 , mineral_total  / num_planets ))
planet_organics = random.randint(range ( 100 , organics_total / num_planets ))


#gamevars
#min_fuel_per_system
#max_fuel_per_system
#fuel_percent_coefficient

#//add starports to the universe.
# we map location ID's to system ID's

def add_starports_se1():
	for port in range( 1 , num_starports - 1):
        #create template dict for new port
		possible_new_starport = { 'location_id' : 0 }
		possible_new_starport['location_id'] = random.randint(2, num_systems)
        #map location_id to system_id... looks up system_id by location_id
        #system has no port, build one
        if system_has_port(possible_new_starport['location_id']) == False :
		    spawned_starport = StarPort(name = grab_starport_name, system_id = possible_new_starport['location_id'])
			add_to_db(spawned_starport)
			#print "<div id='' USER### Created port #"" in location <script>document.all.addports1 location .scrollIntoView();</script></div>");
		else:
			pass


#//add BM's to the universe
def add_blackmarket_se1()
	blackmarket_names = [ "Dodgy Dave", \
				 "Stinkin Sid", \
				 "Goodie-bag Central", \
				 "The Department of Corruption", \
				 "The Ultimate Goodies Store", \
				 "Stompin Jim", \
				 "The War Cabinet", \
				 "Jim  -Dead Eye- Smarms", \
				 "One Eyed Doyle", \
				 "The Ministry of Offence"]
	
	blackmarket_type = 0

	for thing in num_black_markets:
		possible_new_black_market = { 'location_id' : 0 }
		possible_new_black_market['location_id'] = random.randint(2, num_black_markets)
		#bmrkt_type' => "", 'bm_name' => "");
		#less blackmarkets than types
		#print "<div id=''  USER### Created Blackmarket # in <script>document.all.addbms1.   .scrollIntoView();</script></div>");

#//function that will pre-generate planets.
def add_planets(): 
	#account for earth
	planetoid_list      = { 'planet_id' : 0 }

	for planetoid in range( 1 , num_planets - 1 ):
		count  = 1
		planetoid_list.update('planet_id': count )
		count  = count + 1
		Planet(name = names.gen_name( 'all' ))
	print "Randomly Placed Planets Done.\n<br>"

	for planet in planetoid_list:
		add_minerals(planet)
		
#//function that places random events around the universe.
def random_event_placer():
	pass
	#//high level random events

#//add minerals to the systems
def add_minerals(type_of_fill = "random"):
	planetary_figs = (planet_metal + planet_fuel) * 1.1
	for each in systems:
		if type_of_fill = "random"
			#we modify with a co-ef... gives ability to scale in single var
			# set co-eff to 1 to prevent scaling
			return_game_var('fuel_percent_coefficient') * \
				amount_of_fuel_in_system = random.randint(range(return_game_var('min_fuel_per_system'),\
																return_game_var('max_fuel_per_system')))
			return_game_var('metal_percent_coefficient') * \
				amount_of_fuel_in_system = random.randint(range(return_game_var('min_metal_per_system'),\
																return_game_var('max_metal_per_system')))

		print("<div id=''>-Adding minerals to system #<script>document.all.{}.scrollIntoView();</script></div>").format(game_status_html)

//create the star systems
function make_systems_1(&$systems) {
	global $UNI,$extinfo,$tables;
	db("select * from se_svr_star_names order by rand()");

	$centre = round($UNI['size'] / 2); //centre of map
	$do_this = 0;

	if($UNI['map_layout'] == 1) { //grid layout
		$rows = round(sqrt($UNI['numsystems']));
		$row_dist = round($UNI['size'] / $rows);
		$per_col = round($UNI['numsystems'] / $rows);
		$col_dist = round($UNI['size'] / $per_col);
		$row_count = 0;
		$col_count = 0;
	} elseif($UNI['map_layout'] == 2){ //galactic core
		$one_quart = round($centre / 4);
	} elseif($UNI['map_layout'] == 3){ //clusters
		$num_clus = round(sqrt($UNI['numsystems'])) - 1; //number of clusters
		$stars_per_cluster = round($UNI['numsystems'] / $num_clus); //stars per cluster
		$cluster_size = round(($UNI['size'] / ($num_clus * 0.55)) / 2); //size of cluster in pixels
		$offset_cluster = $UNI['size'] - $cluster_size;
		$sec_count = 0;
		$basis_x = $centre;
		$basis_y = $centre;
	} elseif($UNI['map_layout'] == 5){ //ring layout
		$radius = round($UNI['size'] / 2) - 5;
		$degrees_between_stars = 360 / ($UNI['numsystems'] - 1); //number of degrees between each star
		$present_degrees = 0;
	} elseif($UNI['map_layout'] == 6){ //layered rings layout
		if($UNI['numsystems'] < 50){ //single ring
			$radius = round($UNI['size'] / 2) - 5;
			$degrees_between_stars = 360 / ($UNI['numsystems'] - 1);
			$present_degrees = 0;
			$do_this = 1;
		} elseif($UNI['numsystems'] < 200){ //2 rings
			$ring1_star_count = round(($UNI['numsystems'] / 100) * 30); //30% of the stars go into the first ring.
			$ring2_star_count = $UNI['numsystems'] - $ring1_star_count-1; //the rest of the stars (minus Sol).
			$ring3_star_count = 0; //(no third ring)
			$ring1_radius = $centre / 2;
			$ring2_radius = $centre;
			$ring1_degrees_between = 360 / $ring1_star_count;
			$ring2_degrees_between = 360 / $ring2_star_count;
			$ring1_preset = 0;
			$ring2_preset = 0;
		} else { // 3 rings
			$ring1_star_count = round(($UNI['numsystems'] / 100) * 25); //10% of the stars go into the first ring.
			$ring2_star_count = round((($UNI['numsystems'] - $ring1_star_count) / 100) * 34);
			$ring3_star_count = $UNI['numsystems'] - $ring1_star_count-$ring2_star_count-1;
			$ring1_radius = $centre / 1.5;
			$ring2_radius = $centre / 1.2;
			$ring3_radius = $centre;
			$ring1_degrees_between = 360 / $ring1_star_count;
			$ring2_degrees_between = 360 / $ring2_star_count;
			$ring3_degrees_between = 360 / $ring3_star_count;
			$ring1_preset = 0;
			$ring2_preset = 0;
			$ring3_preset = 0;
		}
	}

	while(($count = count($systems)) < $UNI['numsystems']) {
		$result = dbr(1);
		$newname = $result['name'];

		//planetary slot counter
		$planet_slots = mt_rand(0,$UNI['uv_planet_slots']);

		$newsystem = array('num' => $count, 'x_loc' => mt_rand(0,$UNI['size']), 'y_loc' => mt_rand(0,$UNI['size']), 'links' => '', 'name' => $newname, 'fuel' => 0, 'metal' => 0, 'wormhole' => 0, 'planetary_slots' => $planet_slots);


		if($UNI['map_layout'] == 1) { //grid layout
			if($row_count > $rows){//create a new column
				$row_count = 0;
				$col_count++;
			}
			$newsystem['x_loc'] = $col_dist * $col_count;
			$newsystem['y_loc'] = $row_dist * $row_count;
			$row_count++;
			while(system_too_close($newsystem,$systems,$UNI['mindist'])) {
				$newsystem['x_loc'] = mt_rand(0,$UNI['size']);
				$newsystem['y_loc'] = mt_rand(0,$UNI['size']);
			}

		} elseif($UNI['map_layout'] == 2) { //galactic core
			$basis = mt_rand(0,100);

			if($basis > 75){ //within centre quarter
				$div_by = 4;
			} elseif($basis > 50){ //within centre half
				$div_by = 3;
			} elseif($basis > 25){ //within half
				$div_by = 2;
			} else { //anywhere
				$div_by = 1;
			}
			while((get_sys_dist($systems[0],$newsystem) > $UNI['size']/$div_by) || system_too_close($newsystem,$systems,$UNI['mindist'])) {
				$newsystem['x_loc'] = mt_rand(0,$UNI['size']);
				$newsystem['y_loc'] = mt_rand(0,$UNI['size']);
			}

		} elseif($UNI['map_layout'] == 3) { //clusters
			if($sec_count > $stars_per_cluster){ //create new cluster
				$basis_x = mt_rand($cluster_size, $offset_cluster);
				$basis_y = mt_rand($cluster_size, $offset_cluster);
				$sec_count = 0;
			}
			$newsystem['x_loc'] = mt_rand(0, $cluster_size); //x_loc - within cluster
			if(mt_rand(0,100) > 50) { //decide offset from center of cluster.
				$newsystem['x_loc'] += $basis_x;
			} else {
				$newsystem['x_loc'] = $basis_x - $newsystem['x_loc'];
			}
			$newsystem['y_loc'] = mt_rand(0, $cluster_size); //y_loc - within cluster
			if(mt_rand(0,100) > 50) { //decide offset from center of cluster.
				$newsystem['y_loc'] += $basis_y;
			} else {
				$newsystem['y_loc'] = $basis_y - $newsystem['y_loc'];
			}
			while(system_too_close($newsystem,$systems,$UNI['mindist'])) {
				$newsystem['x_loc'] = mt_rand(0,$UNI['size']);
				$newsystem['y_loc'] = mt_rand(0,$UNI['size']);
			}
			$sec_count++;

		} elseif($UNI['map_layout'] == 4) { //circle layout
			while((get_sys_dist($systems[0],$newsystem) > $UNI['size']/2) || system_too_close($newsystem,$systems,$UNI['mindist'])) {
				$newsystem['x_loc'] = mt_rand(0,$UNI['size']);
				$newsystem['y_loc'] = mt_rand(0,$UNI['size']);
			}

		} elseif($UNI['map_layout'] == 5 || $do_this == 1) { //ring layout
			$newsystem['x_loc'] = $radius * cos(deg2rad($present_degrees));
			$newsystem['y_loc'] = $radius * sin(deg2rad($present_degrees));
			$newsystem['x_loc'] += $centre;
			$newsystem['y_loc'] += $centre;
			$present_degrees += $degrees_between_stars;//prepare for next star

		} elseif($UNI['map_layout'] == 6) { //layered rings layout
			if($count <= $ring1_star_count){//inner ring
				$newsystem['x_loc'] = $ring1_radius * cos(deg2rad($ring1_preset));
				$newsystem['y_loc'] = $ring1_radius * sin(deg2rad($ring1_preset));
				$newsystem['x_loc'] += $centre;
				$newsystem['y_loc'] += $centre;
				$ring1_preset += $ring1_degrees_between;
			} elseif($count <= ($ring2_star_count  + $ring1_star_count)|| $ring3_star_count == 0){//second ring
				$newsystem['x_loc'] = $ring2_radius * cos(deg2rad($ring2_preset));
				$newsystem['y_loc'] = $ring2_radius * sin(deg2rad($ring2_preset));
				$newsystem['x_loc'] += $centre;
				$newsystem['y_loc'] += $centre;
				$ring2_preset += $ring2_degrees_between;
//				echo "\n";
			} else {//3rd ring if there is one.
				$newsystem['x_loc'] = $ring3_radius * cos(deg2rad($ring3_preset));
				$newsystem['y_loc'] = $ring3_radius * sin(deg2rad($ring3_preset));
				$newsystem['x_loc'] += $centre;
				$newsystem['y_loc'] += $centre;
				$ring3_preset += $ring3_degrees_between;
			}
		} else { #random layout
			while(system_too_close($newsystem,$systems,$UNI['mindist'])) {
				$newsystem['x_loc'] = mt_rand(0,$UNI['size']);
				$newsystem['y_loc'] = mt_rand(0,$UNI['size']);
			}
		}
		if($extinfo) {
			print("<div id='makesys1$count'>-System #".($count+1)." created.<script>document.all.makesys1$count.scrollIntoView();</script></div>");

		}
		$newsystem['event_random'] = 0;
		$systems[] = $newsystem;
	}
	//exit;
}


//aims to stop one way links from being created
//checks all systems that have already been linked to see what links have already been created to this location.
function pre_linked($systems, $present_system){
	$links_array = array();
	foreach($systems as $new_sys){
		if((string)$new_sys['links'] != ""){
			$present_links = explode(',', $new_sys['links']);
			if(in_array($present_system, $present_links)){
				$links_array[] = $systems[$new_sys['num']];
			}
		}
	}
	return $links_array;
}


//link the systems
function link_systems_1(&$systems) {
	global $UNI,$extinfo;

	foreach($systems as $system) {
		$numlinks = mt_rand($UNI['minlinks'],$UNI['maxlinks']);

		//find the closest systems to the present system. when $numlinks closest found, link them
		foreach (get_closest_systems($system,$systems,$numlinks) as $linksys) {
			make_link($systems[$system['num']],$systems[$linksys['num']]);
		}
		if($extinfo) {
			print "<div id=\"linksys1" . $system['num'] . "\">-Created " .
			 $numlinks . " links in system #" . ($system['num'] + 1) .
			 "</div><script type=\"text/javascript\">document.all.linksys1$system[num].scrollIntoView();</script>";
		}
	}

	//add wormholes if appropriate
	if($UNI['wormholes'] > 0 && $UNI['numsystems'] > 15){
		$num_worms = ceil($UNI['numsystems'] / 35);//num wormholes to make

		$worms_placed = array();

		for($a=1; $a <= $num_worms; $a++){//loop through

			$start_loc = mt_rand(2,$UNI['numsystems']);
			while(system_has_wormhole($worms_placed, $start_loc)) {
				$start_loc = mt_rand(2,$UNI['numsystems']);
			}
			$worms_placed[] = $start_loc;//push into wormhole checking array.


			$end_loc = mt_rand(1,$UNI['numsystems']);
			while(system_has_wormhole($worms_placed, $end_loc)) {
				$end_loc = mt_rand(1,$UNI['numsystems']);
			}
			$worms_placed[] = $end_loc;//push into wormhole checking array.

			//make them permanent
			$systems[$start_loc -1]['wormhole'] = $end_loc;
			if (mt_rand(0,10) > 5) {//two way wormhole
				$systems[$end_loc -1]['wormhole'] = $start_loc;
			}
		}
	}
}

//check to see if a star system has a wormhole in it already.
function system_has_wormhole(&$worms_placed, &$this_worm) {
	foreach($worms_placed as $worm) {
		if($worm == $this_worm) {
			return true;
		}
	}
	return false;
}

//function that determines if it's ok to link to a system
function ok_to_link(&$sys1, &$sys2) {
	global $UNI;

	//linking to itself.
	if($sys1['num'] == $sys2['num']) {
		return false;
	}

	$sys2_links = explode(',', $sys2['links']);

	//return o.k. if target still has empty links || already linked.
	if((count($sys2_links) < $UNI['maxlinks']) || in_array($sys1['num'], $sys2_links)) {
		return true;
	} else {
		return false;
	}
}

//find the closest systems to link to.
/*
$sys =  linking from
$systems = all systens
$howmany = number of closest systems to return
*/
function get_closest_systems($sys, $systems, $howmany) {
	global $UNI;

	//check to see which systems have already linked to this one.
	$systems_to_link = pre_linked($systems, $sys['num']);
	$howmany -= count($systems_to_link);
	if($howmany < 1){
		return $systems_to_link;
	}

	//establish the distance of all stars in relation to this one
	$dists = array();
	foreach($systems as $system) {
		if(ok_to_link($sys, $system)) {
			$dists[$system['num']] = get_sys_dist($sys,$system);
		}
	}
	reset($dists);
	asort($dists,SORT_NUMERIC);

	//link to as many of the closest systems as can.
	while(count($systems_to_link) < $howmany) {
		if(!$present_sys = each($dists)) {//get a system out of the dist array. RETURN if none.
			return $systems_to_link;
		}

		//too far away to be linked to (Sol System excepted).
		if($present_sys['value'] > $UNI['link_dist'] && $UNI['link_dist'] > 0 && $sys['num'] != 0){
			return $systems_to_link;
		}

		$systems_to_link[] = $systems[$present_sys['key']];
	}
	return $systems_to_link;
}

//work out if a system is too close to another system
function system_too_close($sys,&$systems,$within) {
	foreach($systems as $system) {
		if($system['num'] == $sys['num']) {//same system
			continue;
		}
		if($dist = get_sys_dist($sys,$system) < $within) {//too close
			return true;
		}
	}
	return false;
}

//make a single link between two systems.
function make_link(&$sys1,&$sys2) {
	if((string)$sys1['links'] != "") {
		$sys1warps = explode(',',$sys1['links']);
		if(!in_array($sys2['num'],$sys1warps)) {
			$sys1warps[] = $sys2['num'];
			$sys1['links'] = implode(',',$sys1warps);
		}
	} else {
		$sys1['links'] = $sys2['num'];
	}
	if((string)$sys2['links'] != "") {
		$sys2warps = explode(',',$sys2['links']);
		if(!in_array($sys1['num'],$sys2warps)) {
			$sys2warps[] = $sys1['num'];
			$sys2['links'] = implode(',',$sys2warps);
		}
	} else {
		$sys2['links'] = $sys1['num'];
	}
}

//work out the distance (in pixels) between two star systems.
function get_sys_dist(&$sys1,&$sys2) {
	return (int)round(sqrt(pow($sys1['x_loc']-$sys2['x_loc'],2) + pow($sys1['y_loc']-$sys2['y_loc'],2)));
}

//generate the three global maps.
function render_global_se1($game_id) {
	global $UNI,$extinfo,$games_dir, $systems,$preview, $directories, $gen_new_maps, $uv_show_warp_numbers;

	$size = $UNI['size'] + ($UNI['map_border'] * 2);
	$offset_x = $UNI['map_border'];
	$offset_y = $UNI['map_border'];
	$central_star = 1;

	$im = imagecreatetruecolor($size,$size);

	//allocate the colours
	$color_bg = ImageColorAllocate($im, $UNI['bg_color'][0], $UNI['bg_color'][1], $UNI['bg_color'][2]);
	$color_st = ImageColorAllocate($im, $UNI['num_color'][0], $UNI['num_color'][1], $UNI['num_color'][2]);
	$color_sd = ImageColorAllocate($im, $UNI['star_color'][0], $UNI['star_color'][1], $UNI['star_color'][2] );
	$color_sl = ImageColorAllocate($im, $UNI['link_color'][0], $UNI['link_color'][1], $UNI['link_color'][2] );
	$color_sh = ImageColorAllocate($im, $UNI['num_color3'][0], $UNI['num_color3'][1], $UNI['num_color3'][2] );
	$color_l = ImageColorAllocate($im, $UNI['label_color'][0], $UNI['label_color'][1], $UNI['label_color'][2] );
	$worm_1way_color = ImageColorAllocate($im,$UNI['worm_one_way_color'][0], $UNI['worm_one_way_color'][1], $UNI['worm_one_way_color'][2] );
	$worm_2way_color = ImageColorAllocate($im,$UNI['worm_two_way_color'][0], $UNI['worm_two_way_color'][1], $UNI['worm_two_way_color'][2] );

	//get the star systems from the Db if using pre-genned map.
	if (isset($gen_new_maps)) {
		db("select (star_id -1) as num, x_loc, y_loc, wormhole, CONCAT(link_1 -1, ',', link_2 -1, ',', link_3 -1, ',', link_4 -1, ',', link_5 -1, ',', link_6 -1) as links from ${game_id}_stars order by star_id asc");
		while($systems[] = dbr(1)); //dump all entries into $systems.
		unset($systems[count($systems) - 1]); //remove a surplus entry
	}

	//process stars
	foreach($systems as $star){
		if(!empty($star['links'])){//don't link all systems to 1 automatically.
			$star_links = array_map("plus_one", explode(',', $star['links']));
			$star_id = $star['num'] + 1;

			foreach($star_links as $link){ //make star links
				if($link < 1){
					continue 1;
				}
				$other_star = $systems[$link -1];//set other_star to the link destination.
				imageline($im, ($star['x_loc'] + $offset_x), ($star['y_loc'] + $offset_y), ($other_star['x_loc'] + $offset_x), ($other_star['y_loc'] + $offset_y), $color_sl);
			}
		}

		if(!empty($star['wormhole'])) {//Wormhole Manipulation
			$other_star = $systems[$star['wormhole'] -1];
			if($other_star['wormhole'] == $star_id){ //two way
				imageline($im, ($star['x_loc'] + $offset_x), ($star['y_loc'] + $offset_y), ($other_star['x_loc'] + $offset_x), ($other_star['y_loc'] + $offset_y), $worm_2way_color);
			} else { //one way
				imageline($im, ($star['x_loc'] + $offset_x), ($star['y_loc'] + $offset_y), ($other_star['x_loc'] + $offset_x), ($other_star['y_loc'] + $offset_y), $worm_1way_color);
			}
		}
	}

	foreach($systems as $star){ //place the star itself. This is done after the lines, so the text comes on top.
		$star_id = $star['num'] + 1;
		$central_star = 1;

		if($star_id == $central_star) {//Place and Highlight central system
			imagestring($im, $UNI['num_size'], ($star['x_loc'] + $offset_x + 3), ($star['y_loc'] + $offset_y - 4), $star_id, $color_sh);
			imagesetpixel($im, ($star['x_loc'] + $offset_x), ($star['y_loc'] + $offset_y), $color_sh);
		} else { //place normal Star
			if($uv_show_warp_numbers == 1) {
				imagestring($im, $UNI['num_size'], ($star['x_loc'] + $offset_x + 3), ($star['y_loc'] + $offset_y - 4), $star_id, $color_st);
			}
			imagesetpixel($im, ($star['x_loc'] + $offset_x), ($star['y_loc'] + $offset_y), $color_sd);
		}
	}


	//for just a preview we can quite while we're ahead.
	if (isset($preview)) {
		header("Content-type: image/png");
		imagepng($im);
		imagedestroy($im);
		exit;
	}

	//Draw title
	imagestring($im, 5, (($size/2)-80), 5, "Universal Star Map", $color_l);

	//Create buffer image
	$bb_im = imagecreatetruecolor(($UNI['size'] + $UNI['localmapwidth']), ($UNI['size'] + $UNI['localmapheight']));

	ImageColorAllocate($im, $UNI['bg_color'][0], $UNI['bg_color'][1], $UNI['bg_color'][2]);
	ImageCopy($bb_im, $im, ($UNI['localmapwidth'] / 2), ($UNI['localmapheight'] / 2), $offset_x, $offset_y, $UNI['size'], $UNI['size']);

	//Create printable map
	$p_im = imagecreatetruecolor($size,$size);
	ImageColorAllocate($p_im, $UNI['print_bg_color'][0], $UNI['print_bg_color'][1], $UNI['print_bg_color'][2]);
	ImageCopy($p_im, $im, 0, 0, 0, 0, $size, $size);

	//Replace colors
	$index = ImageColorExact($p_im, $UNI['bg_color'][0], $UNI['bg_color'][1], $UNI['bg_color'][2]);
	ImageColorSet($p_im, $index, $UNI['print_bg_color'][0], $UNI['print_bg_color'][1], $UNI['print_bg_color'][2]);
	$index = ImageColorExact($p_im, $UNI['link_color'][0], $UNI['link_color'][1], $UNI['link_color'][2]);
	ImageColorSet($p_im, $index, $UNI['print_link_color'][0], $UNI['print_link_color'][1], $UNI['print_link_color'][2]);
	$index = ImageColorExact($p_im, $UNI['num_color'][0], $UNI['num_color'][1], $UNI['num_color'][2]);
	ImageColorSet($p_im, $index, $UNI['print_num_color'][0], $UNI['print_num_color'][1], $UNI['print_num_color'][2]);
	$index = ImageColorExact($p_im, $UNI['num_color3'][0], $UNI['num_color3'][1], $UNI['num_color3'][2]);
	ImageColorSet($p_im, $index, $UNI['print_num_color'][0], $UNI['print_num_color'][1], $UNI['print_num_color'][2]);
	$index = ImageColorExact($p_im, $UNI['star_color'][0], $UNI['star_color'][1], $UNI['star_color'][2]);
	ImageColorSet($p_im, $index, $UNI['print_star_color'][0], $UNI['print_star_color'][1], $UNI['print_star_color'][2]);

	//Draw new label
	ImageFilledRectangle($p_im, 0, 0, $size, $UNI['map_border'], ImageColorExact($p_im, $UNI['print_bg_color'][0], $UNI['print_bg_color'][1], $UNI['print_bg_color'][2]));
	imagestring($p_im, 5, (($size/2)-80), 5, "Printable Star Map", ImageColorExact($p_im, $UNI['print_label_color'][0], $UNI['print_label_color'][1], $UNI['print_label_color'][2]));

	//Save map and finish
	if (!file_exists("img/{$game_id}_maps")) {
		mkdir("img/{$game_id}_maps", 0777);
	}
	ImagePng($im, "img/${game_id}_maps/sm_full.png");
	ImagePng($bb_im, "img/${game_id}_maps/bb_full.png");
	ImagePng($p_im, "img/${game_id}_maps/psm_full.png");

	if($extinfo) {
		print("<br><br><br><hr><img src='$directories[images]/${game_id}_maps/sm_full.png' onLoad='this.scrollIntoView();'>");

	}
	ImageDestroy($im);
	ImageDestroy($bb_im);
	ImageDestroy($p_im);
}

//draw the local maps.
function renderLocal($game_id) {
	global $UNI, $extinfo, $directories;

	if (!file_exists('img/' . $game_id . '_maps')) {
		trigger_error('Map image is missing - dir does not exist', E_USER_ERROR);
	}

	$full_map = imagecreatefrompng("img/${game_id}_maps/bb_full.png");

	db("select star_id, x_loc, y_loc from ${game_id}_stars");
	while($star = dbr()) {

		$im = imagecreatetruecolor($UNI['localmapwidth'], $UNI['localmapheight']);

		$color_bg = $color_bg = imagecolorallocate($im, $UNI['bg_color'][0], $UNI['bg_color'][1], $UNI['bg_color'][2]);
		$color_ht = imagecolorallocate($im, $UNI['num_color2'][0], $UNI['num_color2'][1], $UNI['num_color2'][2]);
		$color_hd = imagecolorallocate($im, $UNI['num_color2'][0], $UNI['num_color2'][1], $UNI['num_color2'][2]);

		imagecopy($im, $full_map, 0, 0, $star['x_loc'], $star['y_loc'], $UNI['localmapwidth'], $UNI['localmapheight']);

		imagestring($im, $UNI['num_size'], ($UNI['localmapwidth'] / 2) + 3,
		 ($UNI['localmapheight'] / 2) - 4, "$star[star_id]", $color_ht);
		imagesetpixel($im, ($UNI['localmapwidth'] / 2), ($UNI['localmapheight'] / 2), $color_hd);

		imagepng($im, 'img/' . $game_id . '_maps/sm' . $star['star_id'] . '.png');
		if($extinfo) {
			print("<br><img src='img/${game_id}_maps/sm$star[star_id].png' onLoad='this.scrollIntoView();'>");

		}

		imagedestroy($im);
	}

	imagedestroy($full_map);
}


function plus_one($a) {
	return $a + 1;
}

?>