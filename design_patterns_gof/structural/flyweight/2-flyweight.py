# Flyweight

class FormattedText:
    class TextRange:
        def __init__(self, start: int, end: int, capitalize = False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position: int):
            return self.start <= position <= self.end

    def __init__(self, text: str):
        self.text = text
        self.formatting: list[FormattedText.TextRange] = []

    def get_range(self, start: int, end: int):
        range = self.TextRange(start, end)
        self.formatting += [range]
        return range

    def __str__(self):
        return "".join(
            char.upper() if t_range.covers(i) and t_range.capitalize else char
            for i, char in enumerate(self.text)
            for t_range in self.formatting
        )


text = "This is a brave new world"
ft = FormattedText(text)
ft.get_range(10, 15).capitalize = True
print(ft)
