
class Store(database.Model):
    __tablename__              = "base store class"
    store_id                   = database.Column(database.Integer, primary_key=True)

class Bilkos(Store):
    pass

class BlackMarket(Store):
    blackmarket_id            = database.Column(database.Integer)
    name                       = database.Column(database.String(128))
    location                   = database.Column(database.Integer)
