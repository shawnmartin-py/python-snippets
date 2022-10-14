from abc import ABC


class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, sub):
        return (
            hasattr(sub, "swipe") and callable(sub.swipe)
            and hasattr(sub, "sharpen") and callable(sub.sharpen)
        ) or NotImplemented

class Sword(metaclass=SwordMeta): ...

class SamuraiSword:
    def swipe(self): ...

    def sharpen(self): ...


# print(issubclass(SamuraiSword, Sword))

# --------------------------------------------------------------------------- #

class Sword(ABC):
    @classmethod
    def __subclasshook__(cls, sub):
        return (
            hasattr(sub, "swipe") and callable(sub.swipe)
            and hasattr(sub, "sharpen") and callable(sub.sharpen)
        )


# print(isinstance(SamuraiSword(), Sword))

# --------------------------------------------------------------------------- #

class Sword(ABC): ...

@Sword.register
class SamuraiSword:
    ...

print(isinstance(SamuraiSword(), Sword))

# --------------------------------------------------------------------------- #

  