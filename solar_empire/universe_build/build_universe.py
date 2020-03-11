<?php

print("Generating Systems...<br>");
//don't make a new uni for map making
//only output text for html page. not map preview png
 print("Linking Systems...<br>");
//don't make a new uni for map making
//generating a new universe
print("Adding Minerals...<br>");
print("Adding Starports...<br>");
print("Adding Blackmarkets...<br>");
print("Saving Universe...<br>");
print("Creating pre-genned planets...<br>");
print("<p><b class=b1>Warning</b>!<br>You do not have the <b class=b1>gd</b> module installed with this PHP installation, therefore the maps cannot be generated.<p>To fix this, find and install the GD library, or get the server operator to do it if it's a paid for server.");
//another minute to make the images
print("<br>Deleting old images...<br>");
clearImages("img/${db_name}_maps");
print("Rendering global map...<br>");
print("Rendering local maps...<br>");
print("Game Paused");
print("<div id='done'>Finished.<script>document.all.done.scrollIntoView();</script></div>");
//generating some new maps for some reason
print("<br>Deleting old images...<br>");
clearImages("img/${db_name}_maps");
print("Rendering global map...<br>");
print("Rendering local maps...<br>");
//previewing universes
"Choose something to do with the universe generator.<br>Only the bottom choice will re-generate the universe!"
"<p><a href='/preview'>Preview</a> a universe that uses your present variable settings. This won't do anything to the present game!!!";
"<p><br>Generate a <a href='/build_universe'>new universe</a>!<br>"

