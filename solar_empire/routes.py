import solar_empire
from solar_empire.configuration_options import *

solar_empire_server.route('/',             methods=['GET', 'POST'])
solar_empire_server.route('/login',        methods=['GET', 'POST'])
solar_empire_server.route('/user',         methods=['GET', 'POST'])
solar_empire_server.route('/diary',        methods=['GET', 'POST'])
solar_empire_server.route('/location',     methods=['GET', 'POST'])
solar_empire_server.route('/news',         methods=['GET', 'POST'])
solar_empire_server.route('/politics',     methods=['GET', 'POST'])
solar_empire_server.route('/message',      methods=['GET', 'POST'])
solar_empire_server.route('/mpage',        methods=['GET', 'POST'])
solar_empire_server.route('/clan',         methods=['GET', 'POST'])
solar_empire_server.route('/forum',        methods=['GET', 'POST'])
solar_empire_server.route('/player_stat',  methods=['GET', 'POST'])
solar_empire_server.route('/help',         methods=['GET', 'POST'])
solar_empire_server.route('/options',      methods=['GET', 'POST'])
solar_empire_server.route('/developer',    methods=['GET', 'POST'])
solar_empire_server.route('/game_info',    methods=['GET', 'POST'])
solar_empire_server.route('/clan_forum',   methods=['GET', 'POST'])
solar_empire_server.route('/game_status',  methods=['GET', 'POST'])
solar_empire_server.route('/logout',       methods=['GET', 'POST'])
solar_empire_server.route('/logout',       methods=['GET', 'POST'])
solar_empire_server.route('/logout',       methods=['GET', 'POST'])

def index():
    return render_template('index.html')

def login_form():
    return render_template('login.html')

def game_page():
    return render_template('game_page.html')
