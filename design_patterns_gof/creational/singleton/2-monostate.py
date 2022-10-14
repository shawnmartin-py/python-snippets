# Monostate

class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class CEO(Monostate):
    def __init__(self):
        self.name = "steve"


a = CEO()
b = CEO()


print(a.__dict__ is b.__dict__)