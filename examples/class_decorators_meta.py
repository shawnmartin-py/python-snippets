from abc import ABC, abstractmethod
from functools import wraps, singledispatchmethod
from collections.abc import Callable


# Metaclasses, Abstract Base Class, SingledispatchMethod
# Class decorator Class, Descriptors, 


class PropertyDataDescriptor(ABC):
    @abstractmethod
    def __get__(self, instance, owner):
        raise NotImplementedError

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def __isabstractmethod__(self):
        raise NotImplementedError

PropertyDataDescriptor.register(property)


class InvariantMeta(type):
    def __new__(mcs, name, bases, ns, **_):
        return super().__new__(mcs, name, bases, ns)

    def __init__(cls, name, bases, ns, predicates: list | None = None):
        if predicates:
            for name, attr in vars(cls).items():
                for predicate in predicates:
                    cls._wrap_with_invariant_checking_proxy(
                        attr,
                        cls=cls,
                        name=name,
                        predicate=predicate,
                    )
        super().__init__(name, bases, ns)

    @singledispatchmethod
    def _wrap_with_invariant_checking_proxy(*_, **__): ...

    @_wrap_with_invariant_checking_proxy.register
    def _(self, method: Callable, *, cls, name: str, predicate):
        @wraps(method)
        def invariant_checking_method_decorator(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError()
            return result
        setattr(cls, name, invariant_checking_method_decorator)

    @_wrap_with_invariant_checking_proxy.register
    def _(self, prop: PropertyDataDescriptor, cls, *, name: str, predicate):
        setattr(cls, name, InvariantCheckingPropertyProxy(prop, predicate))


class InvariantCheckingPropertyProxy(PropertyDataDescriptor):
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def __get__(self, instance, owner):
        if instance is None:
            return self._referent
        result = self._referent.__get__(instance, owner)
        if not self._predicate(instance):
            raise RuntimeError()
        return result

    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        if not self._predicate(instance):
            raise RuntimeError()
        return result

    def __isabstractmethod__(self):
        return self._referent.__isabstractmethod__


class InvariantTemperature(metaclass=InvariantMeta): ...

def not_below_absolute_zero(temperature):
    return temperature._celsius >= 0


class Temperature(InvariantTemperature, predicates=[not_below_absolute_zero]):
    def __init__(self, celsius, heat):
        self._celsius = celsius
        self.heat = heat

    def get_celsius(self):
        return self._celsius

    @property
    def heat(self):
        return self._heat

    @heat.setter
    def heat(self, value):
        self._heat = value


t = Temperature(0, 30)

#t.heat = 50


