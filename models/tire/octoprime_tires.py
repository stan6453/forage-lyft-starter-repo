from .tire_interface import ITire


class OctoprimeTire(ITire):
    def __init__(self, tires_wear):
        self.__tires_wear = tires_wear

    def needs_service(self):
        tires_wear_sum_threshold = 3
        tires_wear_sum = 0
        for wear in self.__tires_wear:
            tires_wear_sum += wear
        return True if tires_wear_sum >= tires_wear_sum_threshold else False
        

