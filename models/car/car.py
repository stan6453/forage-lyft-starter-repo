from . import IServiceable
from models.tire.tire_interface import ITire


class Car(IServiceable):
    def __init__(self, engine, battery, tire: ITire):
        self.__engine = engine
        self.__battery = battery
        self.__tire = tire

    def needs_service(self):
        """returns true if car needs servicing"""
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tire.needs_service()
