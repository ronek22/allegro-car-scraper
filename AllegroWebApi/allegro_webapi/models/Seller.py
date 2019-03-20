class Seller:
    def __init__(self, name, localization):
        self.name = name
        self.localization = localization
        self.link = 'https://allegro.pl/uzytkownik/' + name
        self.cars = list()

    def add_car(self, car):
        self.cars.append(car)

    def get_average(self):
        return {
            'srednia_cena': round(sum(car.price for car in self.cars) / len(self.cars),2),
            'sredni_wiek': round(sum(car.year for car in self.cars) / len(self.cars),2)
        }

    def get(self):
        return {
            'nazwa': self.name,
            'lokalizacja': self.localization,
            'url': self.link,
            'ilosc_samochodow': len(self.cars),
            **self.get_average()
        }

    def __repr__(self):
        return "{}\t{}\t{}".format(self.name, self.localization, self.get_average())

    def __eq__(self, other):
        return self.name == other.name

