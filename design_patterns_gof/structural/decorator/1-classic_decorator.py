from abc import ABC, abstractmethod

# Classic Decorator

class Shape(ABC):
    def __str__(self):
        return ""

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"Circle"

class ColoredShape(Shape):
    def __init__(self, shape: Shape, color: str):
        self.color = color
        self.shape = shape
    
    def __str__(self):
        return f"{self.shape} is {self.color}"

c = Circle(2)
print(c)
red_c = ColoredShape(c, "red")
print(red_c)