from . import IBattery
from datetime import timedelta


class NubbinBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        service_interval_in_days = 365 * 4
        return (self.__current_date - self.__last_service_date) >= timedelta(service_interval_in_days)
