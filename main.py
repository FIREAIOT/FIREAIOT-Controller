#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from config.env import *

from fireaiot import UAV, Notification

print("UAV's setup..")
uav = UAV()

def callback(data):
	data    = json.loads(data)
	action  = data["action"]
	payload = data["payload"]
	
	if action == "mession.new":
		target    = payload["target"]
		latitude  = target["latitude"]
		longitude = target["longitude"]
		uav.performFirefightingMession(float(latitude), float(longitude))

print("Crafting socket connection and sub to ..")
Notification(
	appKey=env("PUSHER_APP_KEY"), 
	cluster=env("PUSHER_APP_CLUSTER"), 
	secret=env("PUSHER_APP_SECRET"), 
	callback=callback
).connect()

while True:
	time.sleep(0.1)