from .battery_interface import IBattery


class SpindlerBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        service_threshold_in_years = 3
        next_service_date = self.__last_service_date.replace(
            self.__last_service_date.year + service_threshold_in_years
        )
        return self.__current_date >= next_service_date
