from engine.sternman_engine import SternmanEngine
from battery.splinder_battery import SplinderBattery

class Palindrome(SternmanEngine,SplinderBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
