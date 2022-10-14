from abc import ABC, abstractmethod

# Bridge

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius): ...

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle: {radius}")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle: {radius}")

class Shape:
    @abstractmethod
    def draw(self): ...

    @abstractmethod
    def resize(self, factor): ...

class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        self.renderer = renderer
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

c = Circle(VectorRenderer(), 10)
c.resize(2)
c.draw()

