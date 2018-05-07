#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from config.env import *
from FIREAIOT.UAV import UAV
from FIREAIOT.Client import Client

def callback(*args, **kwargs):
    print("processing Args:", args)
    print("processing Kwargs:", kwargs)

uav = UAV()
client = Client(
	appKey=env("PUSHER_APP_KEY"), 
	cluster=env("PUSHER_APP_CLUSTER"), 
	secret=env("PUSHER_APP_SECRET"), 
	callback=callback
).connect()

while True:
    print("running..")
    time.sleep(1)