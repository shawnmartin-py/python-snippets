from abc import ABC, abstractmethod
from enum import Enum

# Abstract Factory

class HotDrink(ABC):
    @abstractmethod
    def consume(self): ...

class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, container: str) -> HotDrink: ...

class Tea(HotDrink):
    def consume(self):
        print("drinking tea")

class Coffee(HotDrink):
    def consume(self):
        print("drinking coffee")

class TeaFactory(HotDrinkFactory):
    def prepare(self, container: str):
        print(f"making a {container} of tea")
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, container: str):
        print(f"making a {container} of coffee")
        return Coffee()

class HotDrinkMachine:
    class Drink(Enum):
        TEA = 1
        COFFEE = 2

    factories: dict[Drink, type[HotDrinkFactory]] = {}
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            self.factories.update(
                {
                    d: globals()[d.name.capitalize() + "Factory"]
                    for d in self.Drink
                }
            )

    def make_drink(self, drink: Drink) -> HotDrink:
        return self.factories[drink]().prepare("cup")

#-----------------------------------------------------------------------------#

machine = HotDrinkMachine()
drink = machine.make_drink(machine.Drink.TEA)
drink.consume()