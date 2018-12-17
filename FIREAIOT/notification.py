import sys
import pysher
import logging

class Notification:
    def __init__(self, appKey, cluster, secret, callback, logging=False):
        if logging:
            root = logging.getLogger()
            root.setLevel(logging.INFO)
            ch = logging.StreamHandler(sys.stdout)
            root.addHandler(ch)

        self.pusher = pysher.Pusher(appKey, cluster=cluster, secret=secret)
        self.callback = callback

    def connect(self):
        self.pusher.connection.bind('pusher:connection_established', self.__connectionHandler)
        self.pusher.connect()
        return self

    def __connectionHandler(self, data):
        channel = self.pusher.subscribe('UAVs')
        channel.bind('App\\Events\\ActionRequired', self.callback)