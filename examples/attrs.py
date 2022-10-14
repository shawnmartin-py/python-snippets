#### attrib resolution order:
#
# cls __getattribute__ -> mro
# --
# cls data descriptor -> mro
# self __dict__
# cls (non-data descriptor, values) -> mro
# --
# cls __getattr__ -> mro


class Base:
    def __init__(self, **coords):
        _coords = {"_" + key: value for key, value in coords.items()}
        vars(self).update(_coords)

    def __getattr__(self, name):
        _name = "_" + name
        try:
            return vars(self)[_name]
        except KeyError:
            raise AttributeError()
     
    def __setattr__(self, name, value):
        raise AttributeError()

    def __delattr__(self, name):
        raise AttributeError()

    
class Sub(Base):
    COLOR_INDEXES = "red", "green", "blue"

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        vars(self)["color"] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = type(self).COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return vars(self)["color"][channel]

    def __setattr__(self, name, value):
        try:
            channel = type(self).COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            vars(self)["color"][channel] = value

# sub = Sub(2, 4, 6, x=45)

# sub.blue = 10

# print(sub.blue)


class LoggingProxy:
    def __init__(self, target):
        super().__setattr__("target", target)

    def __getattribute__(self, name):
        try:
            value = getattr(self._target, name)
        except AttributeError:
            raise AttributeError()
        return value

    def __setattr__(self, name, value):
        target = super().__getattribute__("target")
        try:
            setattr(target, name, value)
        except AttributeError:
            ...

    def __repr__(self):
        target = super().__getattribute__("target")
        


class A:
    def __setattr__(self, name, value):
        print("setattr")

    @property
    def name(self):
        ...

    @name.setter
    def name(self, value):
        print("prop setter")


a = A()



print(vars(a))

