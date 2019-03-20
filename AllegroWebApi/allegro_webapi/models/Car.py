class Car:
    def __init__(self, offer_id, price, name, year=None):
        self.offerId = offer_id
        self.price = price
        self.name = name
        self.year = year

    def update(self, year):
        self.year = year

    def get_link(self):
        return "https://allegro.pl/ogloszenie/" + self.offerId
