import os
from flask.config import Config
import random

#software stuff
VERSION            = 'Generic SE 2.9.1 - MODIFIED:Python Language Conversion -  Version : 0.01'
basedir = os.path.abspath(os.path.dirname(__file__))
things_this_app_needs = ['flask' , "flask-sqlalchemy"]

#server stuff
SERVER_NAME        = "Solar Empire: 2020 - Python Edition"
SERVER_ADDRESS     = ('localhost', 4443)
HTTP_HOST          = "gamebiscuits"
SERVER_HOST        = "fightbiscuits"
DOMAIN             = "firewall-gateway.net"
GAME_DIR           = "/solar_empire/"
URL_FULL           = "https://" + HTTP_HOST + SERVER_HOST + DOMAIN + GAME_DIR
URL_SHORT          = "asdf"
SEND_AUTH_MAIL     = True
SESSION_TIME_LIMIT = 3600
#user stuff
ADMIN_NAME = "Emperor of Sol"
ADMIN_PASSWORD = "password"
ADMIN_EMAIL = "game_admin" + "@" + HTTP_HOST + SERVER_HOST + DOMAIN
ADMIN_USER_ID = 1
OWNER_ID = 1

#DB STUFF 
DATABASE_HOST      = "localhost"
DATABASE           = "solar_empire-python"
DATABASE_USER      = "moop"
DATABASE_PASSWORD  = "password"
USER_TABLE_NAME = "User"
DANGER_STRING= "you should NEVER see this string. Something errored HARD . TACOCAT"

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE + '.' + HTTP_HOST + '.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


#GameVars.sv_turns = 30
QUARK_DAMAGE = random.randint(400,1000)
SAFE_TURNS   = 60
MAX_USER_TURNS = 30

#border on all sides around the image (stops numbers going off the edge) (pixels).
map_border = 25

num_size = 1
#font size for system numbers (on map).

bg_color = [0,0,0] 
#background colour of map

link_color = [90,90,90] 
#colour of links between systems

num_color = [0,255,255]
#Most system numbers

num_color2 = [255,255,255]
#Current system number

num_color3 = [255,0,0]
#Sol color

star_color = [255,255,255]

worm_one_way_color = [230,230,64] 
#yellow

worm_two_way_color = [0,230,0] 
#green

label_color = [0, 255, 0]

localmapwidth = 200
 #width of 'local area' map.

localmapheight = 200
#height of 'local area' map.

minlinks = 2; #miniumum number of links a system may have.

maxlinks = 6; #maximum number of links a system may have.

print_bg_color = [255,255,255] #background colour of printable map.

print_link_color = [200,200,200] #link colour for printable map

print_num_color = [0,0,0]#Most system numbers for printably map

print_star_color = [0,0,0] #star colour for printable map

print_label_color = [0, 0, 0]
"Are you sure you want to build a new universe?<p>This may take some time.";

