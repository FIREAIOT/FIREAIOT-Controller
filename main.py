#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from config.env import *
from FIREAIOT.UAV import UAV
from FIREAIOT.Client import Client

def callback(data):
	data    = json.loads(data)
	action  = data["action"]
	payload = data["payload"]

	if action == "isReady":
		print("isReady command received..")
	elif action == "goTo":
		print("goTo command received with nodes..")
		print(payload["nodes"])
		

# print("Basic UAV's setup..")
# uav = UAV()

print("Crafting socket connection..")
client = Client(
	appKey=env("PUSHER_APP_KEY"), 
	cluster=env("PUSHER_APP_CLUSTER"), 
	secret=env("PUSHER_APP_SECRET"), 
	callback=callback
).connect()

while True:
	time.sleep(0.01)