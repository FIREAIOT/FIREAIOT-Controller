#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from config.env import *
from FIREAIOT.UAV import UAV
from FIREAIOT.Client import Client

def callback(data):
	data = json.loads(data)
	print(
		data["latitude"], 
		data["longitude"]
	)

# uav = UAV()
client = Client(
	appKey=env("PUSHER_APP_KEY"), 
	cluster=env("PUSHER_APP_CLUSTER"), 
	secret=env("PUSHER_APP_SECRET"), 
	callback=callback
).connect()

while True:
    time.sleep(1)