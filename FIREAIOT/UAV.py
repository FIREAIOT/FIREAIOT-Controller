import math
import time
import argparse
from dronekit import connect, VehicleMode, LocationGlobalRelative

class UAV:
    def __init__(self, ip="tcp:127.0.0.1:5760"):
        self.vehicle = connect(ip, wait_ready=True)
        self.hasBall = True

    def performFirefightingMession(self, latitdue, longitude):
        self.armAndTakeOff(40)
        self.goTo(latitude, longitude)
        self.releaseBall()
        self.returnToHome()

    def armAndTakeOff(self, altitude):
        while not self.vehicle.is_armable:
            time.sleep(1)

        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            time.sleep(1)

        self.vehicle.simple_takeoff(altitude)

        while True:
            currentAltitude = self.vehicle.location.global_relative_frame.alt
            if currentAltitude >= altitude * 0.95:
                break
            time.sleep(1)

    def getDistanceInMetres(self, location1, location2):
        dlat = location2.lat - location1.lat
        dlong = location2.lon - location1.lon
        return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


    def goTo(self, latitdue, longitude):
        point = LocationGlobalRelative(latitdue, longitude, 40)
        self.vehicle.simple_goto(point)

        while True:
            distance = self.getDistanceInMetres(self.vehicle.location.global_frame, point)
            print(distance)
            if distance < 20:
                break
            time.sleep(1)

    def returnToHome(self):
        self.vehicle.mode = VehicleMode("RTL")

    def land(self):
        self.vehicle.mode = VehicleMode("LAND")
    
    def releaseBall(self):
        # write to servo
        self.hasBall = False
