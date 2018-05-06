import sys
import time
import pysher
import logging

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

def  callback(*args, **kwargs):
    print("processing Args:", args)
    print("processing Kwargs:", kwargs)

def connect_handler(data):
    channel = pusher.subscribe('alarms')
    channel.bind('AlarmReceived', callback)

pusher = pysher.Pusher("", cluster="ap1", secret="")

pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

while True:
    time.sleep(1)