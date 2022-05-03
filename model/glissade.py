from engine.willoughby_engine import WilloughbyEngine
from battery.splinder_battery import SplinderBattery


class Glissade(WilloughbyEngine, SplinderBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
