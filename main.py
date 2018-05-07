#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from FIREAIOT.UAV import UAV
from FIREAIOT.Client import Client

def callback(*args, **kwargs):
    print("processing Args:", args)
    print("processing Kwargs:", kwargs)

uav = UAV()
client = Client(appKey="", cluster="", secret="", callback=callback)
client.connect()

while True:
    print("no")
    time.sleep(1)