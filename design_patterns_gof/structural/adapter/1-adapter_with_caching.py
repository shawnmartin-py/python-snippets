from dataclasses import dataclass

# Adapter (with caching)

@dataclass(frozen=True)
class Point:
    x: float
    y: float

def draw_point(_: Point):
    print(".", end="")

@dataclass(frozen=True)
class Line:
    start: Point
    end: Point

class Rectangle(list):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))

class LineToPointAdapter:
    cache = {}

    def __init__(self, line: Line):
        self.h = hash(line)
        if self.h not in self.cache:
            self._init(line)

    def _init(self, line: Line):
        print(
            f"Generating points for line [{line.start.x},"
            f"{line.start.y}]->[{line.end.x},{line.end.y}]", end=" "
        )
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif top - bottom == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])
    
def draw(rcs):
    print("\n\n--- Drawing\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
            print("\n")

#-----------------------------------------------------------------------------#

rcs = [
    Rectangle(1, 1, 10, 10),
    Rectangle(3, 3, 6, 6),
]
draw(rcs)
draw(rcs)