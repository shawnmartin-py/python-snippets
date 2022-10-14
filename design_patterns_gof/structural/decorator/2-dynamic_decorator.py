# Dynamic Decorator

class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    def __getattr__(self, item: str):
        return getattr(self.file, item)

    def __setattr__(self, key: str, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.file, value)

    def __delattr__(self, item: str):
        delattr(self.file, item)

    def __iter__(self):
        return iter(self.file)

    def __next__(self):
        return next(self.file)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.file.close()


with FileWithLogging(open("hello.txt", "w")) as file:
    file.writelines(["hello", "world"])
    file.write("testing")