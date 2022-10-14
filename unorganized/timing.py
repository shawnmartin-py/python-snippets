from contextlib import contextmanager
from functools import wraps
from time import perf_counter


def timer():
    start = perf_counter()
    try:
        yield
    finally:
        print(f"{(perf_counter() - start) * 1e3:.2f}ms")


def measure(iterations: int):
    return (
        lambda fn: wraps(fn)(
            lambda: contextmanager(timer)()(
                lambda: [fn() for _ in range(iterations)]
            )()
        )
    )
    # iterations = int(iterations)
    # def decorator(fn):
        # @wraps(fn)
        # def inner():
        #     with timer():
        #         [fn() for _ in range(iterations)]
        # return inner
    # return decorator

@measure(int(10e6))
def add():
    return 1 + 1

# with timer():
#     add():q


add()


# prints >>> 519.86ms