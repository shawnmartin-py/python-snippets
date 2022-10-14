import random
import string

# Flyweight

class User: # 1,700,000
    def __init__(self, name):
        self.name = name

class User2:
    strings = []
    __slots__ = "firstname", "lastname"

    def _get_or_add(self, s) -> int:
        if s in self.strings:
            return self.strings.index(s)
        else:
            self.strings.append(s)
            return len(self.strings) - 1

    def __init__(self, name):
        self.firstname, self.lastname = [
            self._get_or_add(x)
            for x in name.split(" ")
        ]
    
    def __str__(self):
        return self.strings[self.firstname] + " " + self.strings[self.lastname]

def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


users = []
first_names = [random_string() for _ in range(100)]
last_names = [random_string() for _ in range(100)]

for first in first_names:
    for last in last_names:
        users.append(User2(f"{first} {last}"))

print(users[0])