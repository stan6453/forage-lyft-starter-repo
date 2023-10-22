from models.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from models.battery import SpindlerBattery, NubbinBattery
from models.tire import CarriganTire, OctoprimeTire
from .car import Car


class CarFactory():
    """Abstract factory responsible for constructing various car types"""

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tires_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tires_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tires_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tires_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tires_wear)
        return Car(engine, battery, tire)
