from .battery_interface import IBattery


class NubbinBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        next_service_date = self.__last_service_date.replace(
            self.__last_service_date.year+4
        )
        return self.__current_date >= next_service_date
