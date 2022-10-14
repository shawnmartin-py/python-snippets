# Can be used on base class, then all subclasses include behaviour
class Meta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return super().__prepare__(mcs, name, bases)

    def __new__(mcs, name, bases, ns):
        return super().__new__(mcs, name, bases, ns)

    def __init__(cls, name, bases, ns):
        super().__init__(name, bases, ns)

    def __call__(cls, *args, **kwargs):
        if len(args) > 1:
            raise TypeError(
                f"Constructor for class {cls.__name__} does not accept more "
                "than one positional argument"
            )
        return super().__call__(*args, **kwargs)


# Needs decorating on every class
def decorator(cls):
    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            raise TypeError(
                f"Constructor for class {cls.__name__} does not accept more "
                "than one positional argument"
            )
        cls.__init__(*args, **kwargs)
    cls.__init__ = __init__
    return cls

class A(metaclass=Meta): ...

class A: ...


@decorator
class B(A):
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = B("John", 22)

# print(a.name)
# print(a.age)

