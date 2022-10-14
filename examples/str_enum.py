from enum import Enum, EnumMeta
from functools import singledispatchmethod


class StrEnumMeta(EnumMeta):
    @singledispatchmethod
    def __getitem__(self, key):
        return super().__getitem__(key)

    @__getitem__.register
    def _(self, index: int):
        return list(self)[index]


class StrEnum(str, Enum, metaclass=StrEnumMeta):
    def __str__(self) -> str:
        return str.__str__(self)
    

class BRAIN(StrEnum):
    SMALL = "small"
    MEDIUM = "medium"
    GALAXY = "galaxy"

assert str(BRAIN.SMALL) == "small"
assert BRAIN.SMALL == 1

