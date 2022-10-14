from collections import abc
from contextlib import suppress
import os


class ListBasedSet(abc.Set):
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)


class FileDict(abc.MutableMapping):
    def __init__(self, dirname, pairs=(), **kwargs):
        self.dirname = dirname
        with suppress(FileExistsError):
            os.mkdir(dirname)
        self.update(pairs, **kwargs)

    def __getitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            with open(fullname) as f:
                return f.read()
        except FileNotFoundError:
            raise KeyError(key) from None
        
    def __setitem__(self, key, value):
        fullname = os.path.join(self.dirname, key)
        with open(fullname, "w") as f:
            f.write(value)

    def __delitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            os.remove(fullname)
        except FileNotFoundError:
            raise KeyError(key) from None

    def __len__(self):
        return len(os.listdir(self.dirname))

    def __iter__(self):
        return iter(os.listdir(self.dirname))

    def __repr__(self):
        return f"{type(self).__name__}{tuple(self.items())}"


d = FileDict("files")

d["pages"] = FileDict("pages")