import requests

class Server:
    def __init__(self, uuid):
        self.uuid = uuid

    def updateLocation(self, latitude, longitude):
        data = {
            "uuid"      : self.uuid,
            "latitude"  : latitude,
            "longitude" : longitude
        }
        print(requests.put("https://fireaiot.saleemhadad.me/api/v1/uav/location", data=data))
        print("UAV location updated")

    def updateAlarmStatus(self, alarmId, status):
        data = {
            "alarm_id" : alarmId,
            "status"   : status
        }
        requests.put("https://fireaiot.saleemhadad.me/api/v1/alarms", data=data)
        print("Alarm status updated")