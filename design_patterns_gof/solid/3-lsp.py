# Liskov Substitution Principle

# You should be able to substitute a base type for a subtype

class Rectangle:
    def __init__(self, width: int, height: int):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size: int):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value
    

def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f"Expected an area of {expected}, got {rc.area}")

#-----------------------------------------------------------------------------#

rc = Square(5)
use_it(rc)
