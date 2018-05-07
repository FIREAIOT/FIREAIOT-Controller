#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import argparse
from FIREAIOT.Client import Client
from dronekit import connect, VehicleMode, LocationGlobalRelative


def callback(*args, **kwargs):
    print("processing Args:", args)
    print("processing Kwargs:", kwargs)

client = Client(callback=callback)
client.connect()

parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

if not connection_string:
    import dronekit_sitl

    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            break
        time.sleep(1)

arm_and_takeoff(10)

vehicle.airspeed = 3

point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
vehicle.simple_goto(point1)
time.sleep(30)

point2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
vehicle.simple_goto(point2, groundspeed=10)
time.sleep(30)

vehicle.mode = VehicleMode("RTL")
vehicle.close()

if sitl is not None:
    sitl.stop()