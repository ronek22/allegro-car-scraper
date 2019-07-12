import json
from allegro_webapi.utility import retryer
from configparser import ConfigParser
from multiprocessing.pool import ThreadPool
from pathlib import Path
import csv
from tqdm import tqdm

from allegro_webapi.allegro_web_api import AllegroWebApi
from allegro_webapi.models.Car import Car
from allegro_webapi.models.Seller import Seller
from allegro_webapi.utility import REST


class Scraper:
    def __init__(self):
        self.allegro = AllegroWebApi(self._config)
        self.offers = self._get_offers_from_json
        self.flat_offers = self._get_offers_flat
        self.sellers = []
        self.nicks = set()

    def run(self):
        for index, seller in tqdm(enumerate(self.offers), total=len(self.offers)):
            self.create_seller(seller[0])
            for offer in seller[1:]:
                self.add_car_to_seller(index, offer)

        self.write_to_csv()

    def run_flat(self):
        with ThreadPool(20) as pool:
            for _ in tqdm(pool.imap(self.flut_stuff, self.flat_offers), total=len(self.flat_offers)):
                pass

        self.write_to_csv()

    @retryer
    def flut_stuff(self, offer):
        car = Car(offer['OfferId'], offer['Price'], offer['Name'])
        try:
            content = self.allegro.get_item_info(car.offerId)
            nick, location, year = content['nick'], content['local'], content['year']

            car.update(content['year'])

            if nick in self.nicks:
                seller = next((s for s in self.sellers if s.name == nick), None)
                seller.add_car(car)
            else:
                seller = Seller(nick, location)
                seller.add_car(car)
                self.sellers.append(seller)
                self.nicks.add(nick)
        except Exception as e:
            print("Problematic", e)



    def create_seller(self, offer):
        car = Car(offer['OfferId'], offer['Price'], offer['Name'])
        content = self.allegro.get_item_info(car.offerId)
        car.update(content['year'])
        seller = Seller(content['nick'], content['local'])
        seller.add_car(car)
        self.sellers.append(seller)

    def add_car_to_seller(self, seller_id, offer):
        car = Car(offer['OfferId'], offer['Price'], offer['Name'])
        car.update(self.allegro.get_item_info(car.offerId)['year'])

        self.sellers[seller_id].add_car(car)

    @property
    def _config(self):
        config = ConfigParser()
        config.read('./config.ini')
        return config.get('allegro', 'api-key')

    @property
    def _get_offers_from_json(self):
        with open(REST + 'data.json', 'r') as data_file:
            data = json.load(data_file)
        return data

    @property
    def _get_offers_flat(self):
        with open(REST + 'data_without_grouping.json', 'r') as data_file:
            data = json.load(data_file)
        return data

    def write_to_csv(self):
        data = [s.get() for s in self.sellers]
        keys = data[0].keys()
        filepath = str(Path("output", "result.csv"))

        with open(filepath, "w", encoding='utf-8', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)




