import solar_empire
from flask_sqlalchemy import SQLAlchemy

class User(database.Model):
    login_id      = database.Column(database.Integer, primary_key=True)
    username      = database.Column(database.String(64), index=True, unique=True)
    email         = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128))
    ship_id       = database.Column(database.String(128))
    location      = database.Column(database.String(128))
    turns         = database.Column(database.Integer)
    turns_run     = database.Column(database.Integer)
    cash          = database.Column(database.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserShip(database.Model):
	ship_id          = database.Column(database.String(128))
	location         = database.Column(database.String(128))
	configuration    = database.Column(database.String(128))
    #quipment        = database.Column(database.String(128))

class GameVars(database.Model):
    score_method             = database.Column(database.Integer)
    ships_built              = database.Column(database.Integer)
    is_game_paused           = database.Column(database.Boolean)
    logged_in_players        = database.Column(database.Integer)
    logged_out_players       = database.Column(database.Integer)
    ships_destroyed          = database.Column(database.Integer)
    clans                    = database.Column(database.Integer)
    safe_turns_left          = database.Column(database.Integer)
    newbies_left             = database.Column(database.Integer)
    sudden_death             = database.Column(database.Boolean)
    sudden_death_turns_feft  = database.Column(database.Integer)
    are_we_political         = database.Column(database.Boolean)
