try:
    import sys
except ImportError:
    sys = None

assert sys is not None, 'sys must be installed to use something'

from typing import Literal

name = Literal["adsfas", "sdfasdf"]

