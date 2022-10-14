from random import random, randrange


# Chunking and Aliasing ----------------------------------------------------- #
"""
computer gives us words that do things.
make new words to make computers easier to use
"""
# random choice, choices

5000 + int(random() * 200) * 5

result = randrange(5000, 6000, 5)

# print(result)

# Solve a related but simpler problem --------------------------------------- #
# Incremental development --------------------------------------------------- #

tree = {
    "one": [
        "abc",
        "def",
        "ghi",
        {"four": 4, "five": 5},
    ],
    "two": [
        "jkl",
        "mno",
        "BLUE",
        {"six": 6, "seven": 7},
    ],
    "three": [
        "qrs",
        "BLUE",
        "BLUE",
        {"eight": "BLUE", "nine": 9},
    ],
}
from functools import singledispatch

@singledispatch
def path_to(node, target):
    if node == target:
        return f" -> {target!r}"

@path_to.register
def _(node: list, target):
    for i, subnode in enumerate(node):
        if (path := path_to(subnode, target)):
            return f"[{i}]" + path

@path_to.register
def _(node: dict, target):
    for key, subnode in node.items():
        if (path := path_to(subnode, target)):
            return f"[{key!r}]" + path

#print(path_to(tree, 7))

# Build classes independently and let inheritance discover itself ----------- #

# Repeat tasks manually until patterns emerge, then move to a function ------ #
# Continue to generalize as needed ------------------------------------------ #

# Consider object oriented programming as a graph traversal problem --------- #

# Separate ETL from analysis. Separate analysis from presentation ----------- #
# Verify type, verify size, view subset of data, and test a subset ---------- #
# Humans should never gaze upon unsorted data ------------------------------- #
# Sets and dict groupings are primary tools for data analysis --------------- #


print(list(str(3423894732)))



