from dataclasses import dataclass

# Protection Proxy

@dataclass
class Car:
    driver: "Driver"

    def drive(self):
        print(f"{self.driver.name} is driving")

@dataclass
class Driver:
    name: str
    age: int

class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young")

driver = Driver("John", 20)
car = CarProxy(driver)
car.drive()