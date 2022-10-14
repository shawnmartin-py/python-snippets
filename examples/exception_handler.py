
from functools import partial, singledispatchmethod, update_wrapper


class CatchException:
    def __call__(self, obj):
        return self._wrap_with_exception_handler(obj)

    @singledispatchmethod
    def _wrap_with_exception_handler(self, func):
        def _exception_handler_decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
        return update_wrapper(_exception_handler_decorator, func)

    @_wrap_with_exception_handler.register
    def _(self, prop: property):
        _get = partial(prop.__get__)
        _get.__name__ = prop.fget.__name__
        return property(self._wrap_with_exception_handler(_get))




class Math:
    @CatchException()
    @staticmethod
    def divide(a: int, b: int) -> int:
        """divide docs"""
        return a / b

    @CatchException()
    @property
    def result(self) -> int:
        #5 / 0
        return 10




result = Math().divide.__doc__

print(result)