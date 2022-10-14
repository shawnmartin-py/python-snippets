
from collections import Counter
from functools import reduce
import re


# Tools---------------------------------------------------------------------- #
class Var:
    ...

class Const:
    ...

class FuncCall:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, _, name):
        self.name = name

    def __get__(self, *_):
        return self.func()

class RegexEqual(str):
    def __eq__(self, pattern):
        return re.fullmatch(pattern, self)
# --------------------------------------------------------------------------- #

# match RegexEqual("hello"):
#     case "h.*o":
#         print("matches with regex")


def func(*_):
    return 20

class A:
    x = FuncCall(func)

# match 20:
#     case A.x:
#         print("matched 20")


tree = {
    "one": [
        "abc",
        "def",
        "ghi",
        {"fou": 4, "five": 5},
    ],
}

Var.four = "four"
match tree:
    case {
        "one": [
            "abc",
            "def",
            "ghi",
            _,
        ]
    }: print("matched")




def path_to(target, node):
    Var.target = target
    match node:
        case Var.target:
            return f" --> {target!r}"
        case list():
            for i, subnode in enumerate(node):
                if (path := path_to(target, subnode)):
                    return f"[{i}]" + path
        case dict():
            for key, subnode in node.items():
                if (path := path_to(target, subnode)):
                    return f"[{key!r}]" + path
