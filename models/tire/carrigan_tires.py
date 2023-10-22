from .tire_interface import ITire


class CarriganTire(ITire):
    def __init__(self, tires_wear):
        self.__tires_wear = tires_wear

    def needs_service(self):
        tire_wear_threshold = 0.9
        for wear in self.__tires_wear:
            if wear >= tire_wear_threshold:
                return True
        return False