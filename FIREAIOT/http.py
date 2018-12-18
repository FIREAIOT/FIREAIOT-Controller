# -*- coding: utf-8 -*-

import six
import copy
import json

GET, POST, PUT, DELETE = "GET", "POST", "PUT", "DELETE"

class RequestMethod(object):
    def __init__(self, client, f):
        self.client = client
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.client.http.send_request(self.make_request(*args, **kwargs))

    def make_request(self, *args, **kwargs):
        return self.f(self.client, *args, **kwargs)

def request_method(f):
    @property
    def wrapped(self):
        return RequestMethod(self, f)

    return wrapped

class Request(object):
    def __init__(self, client, method, path, params=None):
        if params is None:
            params = {}

        self.method = method
        self.path = path
        self.client = client
        self.params = copy.copy(params)

        if method == POST:
            self.body = six.text_type(json.dumps(params)).encode('utf8')
            self.query_params = {}

        elif method == GET:
            self.body = bytes()
            self.query_params = params

    @property
    def url(self):
        return "%s%s" % (self.client.host, self.path)
    
    @property
    def headers(self):
        headers = {
            "Content-Type": "application/json"
        }

        return headers
