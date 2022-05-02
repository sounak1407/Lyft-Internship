from engine.capulet_engine import CapuletEngine
from battery.splinder_battery import SplinderBattery

class Calliope(CapuletEngine,SplinderBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
