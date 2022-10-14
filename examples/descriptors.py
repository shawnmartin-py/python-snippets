
# cached_property, lru_cache

class Planet:
    class Positive:
        def __get__(self, instance, _):
            return instance.__dict__["_" + self.name]

        def __set_name__(self, _, name):
            self.name = name

        def __set__(self, instance, value):
            if value <= 0:
                raise ValueError(
                    f"'{self.name}' of '{type(instance).__name__}' can only be "
                    "a positive value"
                )
            instance.__dict__["_" + self.name] = value

        def __delete__(self, _):
            raise AttributeError()

    def __init__(
        self, name, radius, mass, orbital_period, surface_temp
    ):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.orbital_period = orbital_period
        self.surface_temp = surface_temp
    
    @property   
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError()
        self._name = value

    radius = Positive()
    mass = Positive()
    orbital_period = Positive()
    surface_temp = Positive()


pluto = Planet("pluto", 1, 2, 3, 4)
mars = Planet("mars", -1, 6, 7, 8)


print(pluto.mass)
print(pluto.radius)
print(mars.mass)
print(mars.radius)
print(pluto.__dict__)