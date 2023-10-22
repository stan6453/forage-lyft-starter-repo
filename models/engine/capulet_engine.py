from .engine_interface import IEngine


class CapuletEngine(IEngine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        service_mileage_threshold = 30000
        return self.__current_mileage - self.__last_service_mileage > service_mileage_threshold
