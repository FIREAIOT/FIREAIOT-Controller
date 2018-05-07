import sys
import pysher
import logging

class Client:
    def __init__(self, callback):
        root = logging.getLogger()
        root.setLevel(logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        root.addHandler(ch)
        self.pusher = pysher.Pusher("", cluster="ap1", secret="")
        self.callback = callback

    def connect(self):
        self.pusher.connection.bind('pusher:connection_established', self.__connectionHandler)
        self.pusher.connect()

    def __connectionHandler(self):
        channel = self.pusher.subscribe('alarms')
        channel.bind('AlarmReceived', self.callback)