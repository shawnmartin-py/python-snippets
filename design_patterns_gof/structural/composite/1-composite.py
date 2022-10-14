# Composite

class GraphicObject:
    def __init__(self, color: str | None = None):
        self.color = color
        self.children: list[GraphicObject] = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def _print(self, items: list[str], depth = 0):
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items)
        return "".join(items)

class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"

#-----------------------------------------------------------------------------#

drawing = GraphicObject()
drawing._name = "Drawing" 
drawing.children.append(Circle("Red"))
drawing.children.append(Circle("Yellow"))
group = GraphicObject()
group.children.append(Circle("Blue"))
group.children.append(Circle("Blue"))
drawing.children.append(group)
print(drawing)