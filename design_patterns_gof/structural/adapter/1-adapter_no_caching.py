from dataclasses import dataclass

# Adapter (no-caching)

@dataclass
class Point:
    x: float
    y: float

def draw_point(_: Point):
    print(".", end="")

@dataclass
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

class LineToPointAdapter(list):
    count = 0

    def __init__(self, line: Line):
        super().__init__()
        self.count += 1
        print(
            f"{self.count}: Generating points for line [{line.start.x},"
            f"{line.start.y}]->[{line.end.x},{line.end.y}]", end=" "
        )
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif top - bottom == 0:
            for x in range(left, right):
                self.append(Point(x, top))
    
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