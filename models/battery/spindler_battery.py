from . import IBattery
from datetime import timedelta


class SpindlerBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        next_service_date = self.__last_service_date.replace(
            self.__last_service_date.year+2
        )
        return self.__current_date >= next_service_date
