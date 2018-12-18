# -*- coding: utf-8 -*-

import requests

class RequestsBackend(object):
    def __init__(self, client):
        self.client = client
        # self.session = requests.Session()

    def send_request(self, request):
        print(request)
        # response = self.session.request(
        #     request.method,
        #     request.url,
        #     data=request.body,
        #     headers=request.headers
        # )

        # return response
