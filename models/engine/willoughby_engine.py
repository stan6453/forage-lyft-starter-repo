from . import IEngine


class WilloughbyEngine(IEngine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        service_mileage_threshold = 60000
        return self.__current_mileage - self.__last_service_mileage > service_mileage_threshold
