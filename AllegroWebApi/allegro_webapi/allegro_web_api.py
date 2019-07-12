from zeep import Client
import json
from allegro_webapi.utility import REST


class AllegroWebApi:
    WSDL = 'https://webapi.allegro.pl/service.php?wsdl'

    def __init__(self, api_key, country=1, wsdl=WSDL):
        self.api_key = api_key
        self.country = country
        self.wsdl = wsdl
        self.client = Client(wsdl=wsdl)
        self.sessionHandle = self.login

    @property
    def login(self):
        with open(REST + 'secret.json', 'r') as secret_file:
            secret = json.load(secret_file)
        access_token = secret['access_token']
        return self.client.service.doLoginWithAccessToken(access_token, self.country, self.api_key)['sessionHandlePart']

    def get_item_info(self, item_id):
        response = self.client.service.doShowItemInfoExt(
            sessionHandle=self.sessionHandle,
            itemId=item_id,
            getAttribs=1,
        )
        return self._handle_info_response(response)

    def _handle_info_response(self, response):
        attrib = response['itemAttribList']['item']
        # attrib_list =
        # [(x['attribName'], x['attribValues']['item'][0]) for x in attrib if x['attribName'] == 'Rok produkcji']

        nick = response['itemListInfoExt']['itSellerLogin']
        local = response['itemListInfoExt']['itLocation'].capitalize()
        description = response['itemListInfoExt']['itDescription']
        stand_description = response['itemListInfoExt']['itStandardizedDescription']
        year = next((x['attribValues']['item'][0] for x in attrib if x['attribName'] == 'Rok produkcji' ), None)

        return {
            "nick": nick,
            "local": local,
            "year": int(year)
        }
