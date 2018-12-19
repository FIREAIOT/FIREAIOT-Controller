#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from config.env import *

from fireaiot import UAV, WebSocket, API
from dronekit import connect, VehicleMode 

print("UAV's setup..")
uav = UAV() # ip="/dev/cu.usbmodem1411"
uav.armAndTakeOff(10)

api = API(host=env("BASE_URL"))

def callback(data):
	data    = json.loads(data)
	action  = data["action"]
	payload = data["payload"]
	
	if action == "mession.new":
		target = payload["target"]
		uav.performFirefightingMession(
			float(target["latitude"]), 
			float(target["longitude"])
		)

print("Crafting socket connection..")
WebSocket(
	appKey=env("PUSHER_APP_KEY"), 
	cluster=env("PUSHER_APP_CLUSTER"), 
	secret=env("PUSHER_APP_SECRET"), 
	callback=callback
).connect()

while True:
	time.sleep(0.1)
