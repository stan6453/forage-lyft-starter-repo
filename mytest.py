from models.car.car_factory import CarFactory
from datetime import datetime

current_date = datetime.now()
last_service_date = datetime(2021, 11, 17)
current_mileage = 55000
last_service_mileage = 30000

car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

print(car.needs_service())


current_date = datetime.now()
last_service_date = datetime(2021, 10, 18)
current_mileage = 55000
last_service_mileage = 30000

car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

print(car.needs_service())