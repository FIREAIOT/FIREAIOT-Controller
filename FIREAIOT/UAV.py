import time
import argparse
from dronekit import connect, VehicleMode, LocationGlobalRelative

class UAV:
    def __init__(self, ip="tcp:127.0.0.1:5760"):
        self.vehicle = connect(ip, wait_ready=True)

    def armAndTakeOff(self, altitude):
        while not self.vehicle.is_armable:
            time.sleep(1)

        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            time.sleep(1)

        self.vehicle.simple_takeoff(altitude)

        while True:
            if self.vehicle.location.global_relative_frame.alt >= altitude * 0.95:
                break
            time.sleep(1)

    def getDistanceInMetres(location1, location2):
        dlat = location2.lat - location1.lat
        dlong = location2.lon - location1.lon
        return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


    def goTo(latitdue, longitude):        
        vehicle.airspeed = 3

        point = LocationGlobalRelative(latitdue, longitude, 40)
        vehicle.simple_goto(point)

        while True:
            if self.getDistanceInMetres(vehicle.location.global_frame, point) > 10:
                break
            time.sleep(1)



