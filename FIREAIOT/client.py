# -*- coding: utf-8 -*-

from .requests import RequestsBackend

class Client(object):
    def __init__(self, host=None):
        self.http = RequestsBackend(self)
        self.host = host