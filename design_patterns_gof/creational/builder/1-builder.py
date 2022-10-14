# Builder

class HtmlElement:
    indent_size = 2

    def __init__(self, name = "", text = ""):
        self.name = name
        self.text = text
        self.elements = []

    def _str(self, indent: int) -> str:
        lines = []
        i = indent * self.indent_size * " "
        lines.append(f"{i}<{self.name}>")
        if self.text:
            i1 = (indent + 1) * self.indent_size * " "
            lines.append(f"{i1}{self.text}")
        for e in self.elements:
            lines.append(e._str(indent + 1))
        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self._str(0)

    # @staticmethod
    # def create(name: str):
    #     return HtmlBuilder(name)

# def html_element_create(name: str):
#     return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self._root = HtmlElement(root_name)

    def add_child(self, child_name, child_text) -> "HtmlBuilder":
        self._root.elements.append(
            HtmlElement(child_name, child_text),
        )
        return self

    def __str__(self) -> str:
        return str(self._root)

#-----------------------------------------------------------------------------#

builder = HtmlBuilder("body")
builder.add_child("h1", "title").add_child("h2", "subtitle")
print(builder)