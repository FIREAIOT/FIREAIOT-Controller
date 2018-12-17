#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from config.env import *

from fireaiot import UAV
# from fireaiot import Client

print("Basic UAV's setup..")
uav = UAV()

# def callback(data):
# 	data    = json.loads(data)
# 	action  = data["action"]
# 	payload = data["payload"]
	
# 	if action == "isReady":
# 		print("isReady command received..")
# 	elif action == "goTo":
# 		target    = payload["target"]
# 		latitude  = target["latitude"]
# 		longitude = target["longitude"]
# 		print("goTo command received with target..", latitude, longitude)
# 		uav.armAndTakeOff(40)
# 		uav.goTo(float(latitude), float(longitude))
# 		uav.returnToHome()

# print("Crafting socket connection..")
# client = Client(
# 	appKey=env("PUSHER_APP_KEY"), 
# 	cluster=env("PUSHER_APP_CLUSTER"), 
# 	secret=env("PUSHER_APP_SECRET"), 
# 	callback=callback
# ).connect()

while True:
	time.sleep(0.1)