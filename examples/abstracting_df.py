from dataclasses import dataclass
from typing import NamedTuple

from pandas import DataFrame


class Resistor(NamedTuple):
    number: str
    manufacturer: str
    resistance: int


# @dataclass
# class Resistor:
#     number: str
#     manufacturer: str
#     resistance: int


class Product:
    def __init__(self, *components: Resistor):
        self.components = DataFrame(
            [[r.manufacturer, r.resistance] for r in components],
            index=[r.number for r in components],
            columns=["manufacturer", "resistance"],
        )

    def __getitem__(self, number: str) -> Resistor:
        r = self.components.loc[number]
        return Resistor(number, r.manufacturer, r.resistance)


p = Product(
    Resistor("10-423-1234", "honhai", 1),
    Resistor("10-423-1249", "samsung", 5),
    Resistor("10-423-1230", "honhai", 10),
)


print(f"{p.components.resistance.mean() = }")
print(f"{p['10-423-1234'] = }")