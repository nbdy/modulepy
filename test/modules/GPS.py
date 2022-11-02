from typing import Optional

from gps import gps, WATCH_ENABLE

from modulepy import log
from modulepy.Base import Base, Information, Version


class GPS(Base):
    information = Information("GPS", Version(1, 0, 0))
    client: Optional[gps] = None

    def on_start(self):
        log.debug("Creating GPS client")
        try:
            self.client = gps(mode=WATCH_ENABLE)
            log.debug("Created client")
            self.data.set("error", None)
        except ConnectionRefusedError:
            self.data.set("error", "ConnectionRefusedError")
            log.error("Could not create client")
            pass

    def on_stop(self):
        log.debug("Closing GPS client")
        if self.client:
            self.client.close()

    def work(self):
        if self.client:
            self.client.next()
            self.data.set("latitude", self.client.fix.latitude)
            self.data.set("longitude", self.client.fix.longitude)
            self.data.set("altitude", self.client.fix.altitude)
            self.data.set("speed", self.client.fix.speed)
            self.data.set("track", self.client.fix.track)
            self.data.set("satellites", self.client.satellites)
            self.data.set("timestamp", self.client.utc)
