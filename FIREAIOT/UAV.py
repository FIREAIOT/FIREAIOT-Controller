import time
import argparse
from dronekit import connect, VehicleMode, LocationGlobalRelative

class UAV:
    def __init__(self, ip="tcp:127.0.0.1:5760"):
        self.vehicle = connect(ip, wait_ready=True)

    def armAndTakeoff(self, altitude):
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