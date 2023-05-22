import datetime
import logging

import requests


class CoinList:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.coin_list = None
        self.coin_last_update = datetime.datetime(2023, 1, 1)

    def update(self):
        if (datetime.datetime.now() - self.coin_last_update) >= datetime.timedelta(hours=1):
            coin_request = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=false")
            coin_list_gc = coin_request.json()
            self.coin_list = coin_list_gc
            self.coin_last_update = datetime.datetime.now()
            logging.info("Reloaded coin list")


class ChartTemplate:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, template='plotly_dark'):
        self.template = template

    def set_template(self, template: str):
        self.template = template

    def get_template(self):
        return self.template
