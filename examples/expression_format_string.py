class StringEx(str):
    def __getattribute__(self, name):
        try:
            return getattr(super(), name)()
        except:
            raise AttributeError(f"{self!r} object has no attribute {name!r}")

    def __repr__(self):
        return repr(type(self).__name__)



text = "this is some text {.title}"



print(text.format(StringEx("in upper")))




#print("string".upper())

