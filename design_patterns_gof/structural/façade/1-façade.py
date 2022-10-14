# Façade

class Buffer:
    def __init__(self, width = 20, height = 20):
        self.width = width
        self.height = height
        self.buffer = [" "] * (width * height)

    def write(self, text: str):
        self.buffer += text

    def __getitem__(self, item: str):
        return self.buffer[item]

class ViewPort:
    def __init__(self, buffer: Buffer | None = None):
        if buffer is None:
            buffer = Buffer()
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index: int):
        return self.buffer[index + self.offset]

    def append(self, text: str):
        self.buffer.write(text)


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = ViewPort(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text: str):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index: int):
        return self.current_viewport.get_char_at(index)


c = Console()
c.write("hello")
ch = c.get_char_at(400)
print(ch)