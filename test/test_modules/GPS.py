from gps import gps, WATCH_ENABLE
from time import sleep
from dataclasses import dataclass

from modulepy.ModuleBase import ModuleBase, ModuleInformation, ModuleVersion


@dataclass
class GPSData:
    latitude: float
    longitude: float
    altitude: float
    speed: float
    course: float
    satellites: int
    timestamp: float


class GPS(ModuleBase):
    information = ModuleInformation("GPS", ModuleVersion(1, 0, 0))
    client: gps = None
    position = None
    gps_data: GPSData = GPSData(0, 0, 0, 0, 0, 0, 0)

    def on_start(self):
        print("Starting GPS")
        self.client = gps(mode=WATCH_ENABLE)

    def on_stop(self):
        print("Stopping GPS")
        self.client.close()

    def work(self):
        print("GPS working")
        self.client.next()
        self.gps_data.latitude = self.client.fix.latitude
        self.gps_data.longitude = self.client.fix.longitude
        self.gps_data.altitude = self.client.fix.altitude
        self.gps_data.speed = self.client.fix.speed
        self.gps_data.course = self.client.fix.track
        self.gps_data.satellites = self.client.satellites
        self.gps_data.timestamp = self.client.utc
        self.enqueue(self.gps_data)
        sleep(1)
