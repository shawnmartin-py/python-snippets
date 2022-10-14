from abc import ABC, abstractmethod
from ast import And
from enum import Enum

# Open-Closed Principle

# Classes should be open for extension but closed for modification

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"({self.name}, {self.color}, {self.size})"
    
class ProductFilter:
    def filter_by_color(self, products: list[Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products: list[Product], size: Size):
        for p in products:
            if p.size == size:
                yield p

# --------------------------------------------------------------------------- #

# Specification

class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item): ...

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec): ...

class ColorSpec(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpec(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *specs: Specification):
        self.specs = specs
        
    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)

class Filter(Filter):
    def filter(self, items: list[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item

#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
    products = [apple, tree, house]

    # pf = ProductFilter()
    # print(*pf.filter_by_color(products, Color.GREEN))
    green_spec, large_spec = ColorSpec(Color.GREEN), SizeSpec(Size.LARGE)
    pf = Filter()
    print(*pf.filter(products, green_spec & large_spec))

