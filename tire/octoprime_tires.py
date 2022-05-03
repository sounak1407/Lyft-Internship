from abc import ABC
from car import Car


class OctoprimeTires(Car, ABC):
    def __init__(self, tire_status):
        super().__init__(last_service_date)
        self.tire_status = tire_status

    def tires_should_be_serviced(self):
        return sum(tire_status) >= 3