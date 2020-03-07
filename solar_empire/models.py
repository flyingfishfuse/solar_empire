import solar_empire
from solar_empire import database
class User(database.Model):
    login_id      = database.Column(database.Integer, primary_key=True)
    username      = database.Column(database.String(64), index=True, unique=True)
    email         = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128))
    ship_id       = database.Column(database.String(128))
    location      = database.Column(database.String(128))
    turns         = database.Column(database.Integer)
    turns_run     = database.Column(database.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserShip(database.Model):
	ship_id  = database.Column(database.String(128))
	location = database.Column(database.String(128))
	config   = database.Column(database.String(128))

class GameVars(database.Model):
    score_method = database.Column(database.Integer)
    ships_built  = database.Column(database.Integer)
