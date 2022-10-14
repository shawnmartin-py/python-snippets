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


class Invariant:
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, cls):
        for name, attr in vars(cls).items():
            self._wrap_with_invariant_checking_proxy(
                attr,
                cls=cls,
                name=name,
                predicate=self.predicate,
            )
        return cls

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


def not_below_absolute_zero(temperature):
    return temperature._celsius >= 0


@Invariant(lambda self: self._heat < 40)
@Invariant(not_below_absolute_zero)
class Temperature:
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


t = Temperature(10, 30)

#t.heat = 50


