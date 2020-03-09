import solar_empire
from solar_empire.configuration_options import *
from solar_empire.generator_functions import *
from solar_empire.models import *


def game_status():
    if Request.form.get('oven_timer'):
        make_systems()
        add_planets()
        add_starports()
        add_blackmarkets()
        place_resources()

    return render_template('game_status.html')

def bilkos_blackmarket_shop():
    return render_template('bilkos.html')
