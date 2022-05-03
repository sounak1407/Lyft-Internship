from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date, tire_status):
        self.last_service_date = last_service_date
        self.tire_statujs = tire_status

    @abstractmethod
    def needs_service(self):
        pass
