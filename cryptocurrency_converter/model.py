import requests
from cryptocurrency_converter import API_KEY, URL_SPECIFIC_RATE
from cryptocurrency_converter.errors import APIError 

class Model:
    def __init__(self, currency_from = "", currency_to = ""):
        self.currency_from = currency_from
        self.currency_to = currency_to

        self.rate = 0.0

    def get_rate(self):
        self.get_request = requests.get(URL_SPECIFIC_RATE.format(
            self.currency_from,
            self.currency_to,
            API_KEY
        ))

        if self.get_request.status_code != 200:
            raise APIError(self.get_request.json()["error"])
            

        self.rate = round(self.get_request.json()["rate"], 2)
