'<p><a href=location.php>Return to star system</a>';
 // Join clan
'Join Clan','You are already a member of a clan.',"?clans=1");
Join Clan','That clan already has the maximum number of members allowed.',"?clans=1");
'Join Clan','You are already a member of a clan.',"?clans=1");
The clan leader may not leave the clan.<p>You may assign a new leader and then leave.";
"You may not Kick the Admin out of your clan.<p>";
Are you sure you want to kick this clan member out?','sure','yes');
"User <b class=b1>$kick_clan[login_name]</b> kicked out of the clan.<p>";
'Disband Clan',$filename,'Are you sure you want to disband this clan?','sure','yes');
"<b class=b1>$user[login_name]</b> disbanded the <b class=b1>$clan[clan_name](<font color=$clan[sym_color]>$clan[symbol]</font>)</b> Clan.");
"The Maximum allowed clans set by the admin has been met.";
"You are already a member of a clan.<p>";
'What should the name of your new clan be?','name','');
'Please choose a three letter symbol for your clan.<br><b class=b1>Must</b> have either two or three letters: <br>(only symbols acceptable: a-z0-9~@$%&*_+-=£§¥²³µ¶)','symbol','');
<form action=\"clan.php\" method=\"post\">";
"<input type=\"hidden\" name=\"$key\" value=\"$value\">";
 "Choose a color for the clan symbol:<p>";
"Enter your own: <input type=\"text\" name=\"sym_color\" size=\"15\" /><p> Or pick one:";
"<table>\n\t<tr>";
 "\n\t\t<td><input type=\"radio\" name=\"sym_color\" value=\"$hex\"> <span style=\"color: #$hex;\">$name</span></td>";
"\n\t</tr>\n\t<tr>""\n\t</tr>\n</table>
<input type=\"submit\" value=\"Submit\">
</form>'Choose symbol color'"?clans=1");
'Create Clan',$filename,'What should the clan password be? (5 Characters Minimum, 25 Max)','passwd','');
"Error","That password is too similar to your account password. Please use a different password.");
'Create Clan',$filename,'Please enter the clan password again.','passwd_verify','');
Create Clan",'The password must be at least 5 characters.',"?clans=1");
"Create Clan",'No-way. You may not use the same pass as your user account. Try a different one.',"?clans=1");
"Create Clan",'The passwords did not match.',"?clans=1");
'Create Clan','Your clan symbol must have at least one character.',"?clans=1");
'Create Clan','Your clan name may contain only letters, numbers or any of these characters: ~!@#$%&*_+-=��������׀��',"?clans=1");
"select symbol from ${db_name}_clans where symbol = '$symbol'");
'Create Clan','That symbol is already in use.',"?clans=1");
"<b class=b1>$user[login_name]</b> created the <b class=b1>$name(<font color=$sym_color>$symbol</font>)</b> Clan.");
"Created the $name clan.");
// Assign new leader
"Please choose another clan member to be the leader:<p>";
"<input type=hidden name=$var value='$value'>";
"<input type=hidden name=$var value='$value'>";
"<select name=leader_id>";
"<option value=$member_name[login_id]>$member_name[login_name]</option>";
"</select>";
"<input type=hidden name=sure value='no'>";
' <input type=submit value=Submit></form>';
'Choose new clan leader',$ostr,"?clans=1");
'Error',"No-one in your clan can become clan leader. That means u're stuck as clan leader.","?clans=1");
'Change Clan Leader',$filename,'Are you sure you want to relinquish leadership of this clan?','sure','yes');
"Clan leader changed<p>";

#################
#Default clan page - if not in a clan.
################
// Clan Ranking
 "Clan Name";
 "c.clan_name";
 "Members";
 "members";
 "Fighters Killed";
 "fkilled";
 "Fighters Lost";
 "flost";
 "Ships Killed";
 "skilled";
 "Ships Lost";
 "slost";
 "Turns Run";
 "trun";
 "Score";
 "score";
#get details of each clan
"There are <b>$clan_count[0]</b> clans at present. <br>The clan limit for this game is <b>$max_clans</b>.<p>Ranking listed by <b class=b1>$order_by_str</b><p>";
"<a href=$filename?ranking=2".$dir_array[2].">Clan Name</a>", "<a href=$filename?ranking=3".$dir_array[3].">Members</a>", "<a href=$filename?ranking=4".$dir_array[4].">Fighters<br>Killed</a>", "<a href=$filename?ranking=5".$dir_array[5].">Fighters<br>Lost</a>", "<a href=$filename?ranking=6".$dir_array[6].">Ships<br>Killed</a>", "<a href=$filename?ranking=7".$dir_array[7].">Ships<br>Lost</a>", "<a href=$filename?ranking=8".$dir_array[8].">Turns<br>Run</a>", "<a href=$filename?ranking=1".$dir_array[1].">Score</a>"));
 "<a href=clan.php?join=$clan[clan_id]>Join</a>";
 "<a href=clan.php>View</a>";
"<b class=b1>$clan[clan_name]</b>(<b><font color=$clan[sym_color]>$clan[symbol]</font></b>)",$clan['members'],$clan['fkilled'],$clan['flost'],$clan['skilled'],$clan['slost'],$clan['trun'],$clan['score'],$option,"<a href=clan.php?clan_info=1&target=$clan[clan_id]>Details</a>"));
 "</table>";
 "<br>There are no clans at present. <br>Maximum number of Clans allowed is <b>$max_clans</b>.";
 "<p><a href=clan.php?create=1>Create a new clan</a><br>";
 "<p>The Maximum number of clans(<b>$max_clans</b>) has been reached.";
"Clan Rankings",$error_str,"?clans=1");
// change password
 "<a href=clan.php>Back To Clan Control</a>";
"stop that","You are not in a clan as such.<p>","?clans=1");
"stop that","You are not the clan leader.<p>","?clans=1");
 "Passwords must be minimum of five(5) characters long and a max of 25.";
 "<table><form action=clan.php method=post><input type=hidden name=changepass value=changed>";
 "<tr><td align=right>Old Password:</td><td><input type=password name=oldpass></td></tr>";
 "<tr><td align=right>New Password:</td><td><input type=password name=newpass></td></tr>";
 "<tr><td align=right>Re-type New Password:</td><td><input type=password name=newpass2></td></tr>";
 "<tr><td></td><td><input type=Submit value='Change Password'></td></tr></form></table><p>";
"Change Password",$temp_str,"?clans=1");
 "The password must be at least 5 characters.<p>";
 "No-way. You may not use the same pass as your user account. Try a different one.<p>";
 "What are you wasting my bandwith for? Thats the same as the previous pass. Try something else.<p>";
 "The old password is not correct!<br>";
 "<a href='javascript:back()'>Go back</a><p>";
 "Clan password changed successfully<p>";
 "Password mismatch!<br>";
 "<a href='javascript:back()'>Go back</a><br>";
 "<a href=clan.php>Clan Control</a>";
 "</table><br><br>Below is a listing of the members of the <b class=b1>$cd[clan_name]</b1> clan. ".make_table(array("User","Turns Run","Fighters Killed","Fighters Lost","Ships Killed","Ships Lost"));
"Bounty"
"Planets"
"Planetary Fighters"
"Launch Pads"
"Research Facilities"
"Shield Generators"
"hield Charges"
"Colonists"
#// print normal page for clan-member
"You are a member of the <b class=b1>$clan_name</b>(<font color=$clan[sym_color]>$clan[symbol]</font>) clan.<p>";
"Password for the clan is <b class=b1>$clan[passwd]</b>.<br><br>";
"Member","Turns","Cash","Tech Units","Kills","Status"));
"select login_name,turns,cash,tech,ships_killed,last_request,login_id from ${db_name}_users where clan_id = $user[clan_id] order by login_name,ships_killed");
 "<a href=message.php?target=$clan_member[login_id]>Message</a>";
" - <a href=clan.php?kick=$temp_id>Kick</a>";
"<a href=$filename?sort_planets=login_name&sorted=$sorted>Planet Owner</a>","<a href=$filename?sort_planets=planet_name&sorted=$sorted>Planet Name</a>","<a href=$filename?sort_planets=location&sorted=$sorted>Location</a>","<a href=$filename?sort_planets=fighters&sorted=$sorted>Fighters</a>","<a href=$filename?sort_planets=colon&sorted=$sorted>Colonists</a>","<a href=$filename?sort_planets=cash&sorted=$sorted>Cash</a>","<a href=$filename?sort_planets=metal&sorted=$sorted>Metal</a>","<a href=$filename?sort_planets=fuel&sorted=$sorted>Fuel</a>","<a href=$filename?sort_planets=elect&sorted=$sorted>Electronics</a>","<a href=$filename?sort_planets=organ&sorted=$sorted>Organics</a>"));
"<b class=b1>$clan_planet[login_name]</b>";
#show all ships, not just other clan members.
#determine if users want to see the abbreviation or not of ship types..
 "<p><a href=clan.php>Show Summary of Clan Ships</a></p>\n";
"<a href=$filename?sort_ships=login_name&sorted_ships=$sorted_ships&show_clan_ships=1>Ship Owner</a>","<a href=$filename?sort_ships=ship_name&sorted_ships=$sorted_ships&show_clan_ships=1>Ship Name</a>","<a href=$filename?sort_ships=$class_temp_var&sorted_ships=$sorted_ships&show_clan_ships=1>Ship Class</a>","<a href=$filename?sort_ships=location&sorted_ships=$sorted_ships&show_clan_ships=1>Location</a>","<a href=$filename?sort_ships=fighters&sorted_ships=$sorted_ships&show_clan_ships=1>Fighters</a>","<a href=$filename?sort_ships=shields&sorted_ships=$sorted_ships&show_clan_ships=1>Shields</a>");
 "<b class=b1>$clan_ship[login_name]</b>";
"<table><p>";
# Summary of Clan ships
 "<br><br><a href=clan.php?show_clan_ships=1>Show All Clan Ships</a><p>";
 "<b class=b1>$clan_ship[login_name]</b> has <b>$clan_ship[total]</b> Ship(s) w/ <b>$clan_ship[fighters]</b> Total Fighters<br>";
 "<br><br>";
 "<a href=clan.php?ranking=1>Clan Rankings</a>";
 "<br><a href=clan.php?clan_info=1&target=$user[clan_id]>Clan Information</a><br><br>";
 "<a href=clan.php?changepass=1>Change Clan Password</a><br>";
 "<a href=player_relations.php?relations=1>Enter Player Relations</a><br>";
 "<a href=clan.php?lead_change=1>Change Clan Leader</a><br>";
 "<a href=message.php?target=-2&clan_id=$user[clan_id]>Message Clan</a><br>";
 "<a href=clan.php?leave=1>Leave Clan</a><br>";
 "<a href=clan.php?disband=1>Disband Clan</a><br>";
 "<a href=message.php?target=-2&clan_id=$user[clan_id]>Message Clan</a><br>";
 "<a href=clan.php?leave=1>Leave Clan</a><br>";
