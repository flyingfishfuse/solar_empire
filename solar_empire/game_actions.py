import solar_empire
from solar_empire import *
from solar_empire.configuration_options import *
from solar_empire.generator_functions import *
from solar_empire.models import *
from solar_empire.common_include import *


def game_status():
    if request.method == 'POST' and Request.form.post('oven_timer'):
        make_systems()
        add_planets()
        add_starports()
        add_blackmarkets()
        place_resources()
    elif request.method == 'POST' and Request.form.post('pause_button'):
        hit_the_brakes
    elif request.method == 'POST' and Request.form.post('give_minerals'):
        resource_type = Request.form.post('resource_type')
        amount        = Request.form.post('amount')
        player        = Request.form.post('player')
        add_resources(player, resource_type, amount)
    return render_template('game_status.html')

def bilkos_blackmarket_shop():
    return render_template('bilkos.html')
