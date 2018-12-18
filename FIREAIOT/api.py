# -*- coding: utf-8 -*-

from .client import Client
from .http import GET, POST, Request, request_method

class API(Client):
    def __init__(self, host=None):
        super(API, self).__init__(host=host)

    @request_method
    def update_location(self, latitude=None, longitude=None):
        params = {
            'latitude': latitude,
            'longitude': longitude
        }

        return Request(self, POST, "/locations", params)
