import solar_empire
from solar_empire import database
from solar_empire.inc.configuration_options import *

class ForumPost(database.Model):
    __tablename__              = "base forum post class"
    user_id                    = database.Column(database.String(128), primary_key=True)
    time                       = database.Column(database.String(128))
    content                    = database.Column(database.String(528))

class PublicPost(ForumPost):
    pass

class ClanPost(ForumPost):
    __tablename__              = "Clan Forum Fosts"
    clan_post_id               = database.Column(database.Integer)
    clan                       = database.Column(database.String(128))