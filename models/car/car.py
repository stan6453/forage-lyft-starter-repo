from . import IServiceable


class Car(IServiceable):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery

    def needs_service(self):
        """returns true if car needs servicing"""
        return self.__engine.needs_service() or self.__battery.needs_service()
