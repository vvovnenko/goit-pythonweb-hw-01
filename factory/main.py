from abc import abstractmethod, ABC
import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    def create_car(self, make: str, model: str):
        return Car(make, f"{model} ({self.get_country_code()} Spec)")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, f"{model} ({self.get_country_code()} Spec)")

    @abstractmethod
    def get_country_code(self) -> str:
        pass


class USVehicleFactory(VehicleFactory):
    def get_country_code(self) -> str:
        return "US"


class EUVehicleFactory(VehicleFactory):
    def get_country_code(self) -> str:
        return "EU"


if __name__ == "__main__":
    eu_vehicle_factory = EUVehicleFactory()
    eu_car = eu_vehicle_factory.create_car("Toyota", "Corolla")
    eu_motorcycle = eu_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    eu_car.start_engine()
    eu_motorcycle.start_engine()

    us_vehicle_factory = USVehicleFactory()
    us_car = us_vehicle_factory.create_car("Toyota", "Corolla")
    us_motorcycle = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()
