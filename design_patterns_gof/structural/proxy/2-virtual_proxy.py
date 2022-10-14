# Virtual Proxy

class Bitmap:
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Loading image from {filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")

class LazyBitmap:
    def __init__(self, filename: str):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image: Bitmap):
    print("About to draw image")
    image.draw()
    print("Done drawing image")

bmp = LazyBitmap("file.jpg")
draw_image(bmp)