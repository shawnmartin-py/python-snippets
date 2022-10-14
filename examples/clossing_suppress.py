from contextlib import closing, suppress


class Object:
    name = "john"

    def close(self):
        print("closing")


with closing(Object()) as object:
    print(object.name)


with suppress(FileNotFoundError):
    with open("non_existing_file.txt") as file:
        print(file.read())


try:
    with open("non_existing_file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")