from dataclasses import dataclass
from math import cos, sin

# Factory

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    class Factory:
        @staticmethod
        def polar_coordinates(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

#-----------------------------------------------------------------------------#

p = Point.Factory.polar_coordinates(1, 2)

print(p)
