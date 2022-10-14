from abc import ABC, abstractmethod
from enum import Enum

# Broker Chain

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENCE = 2

class Query:
    def __init__(
        self,
        creature_name: str,
        what_to_query: WhatToQuery,
        default_value: int
    ):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender: "Creature", query: Query):
        self.queries(sender, query)

class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: "Creature"):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender: "Creature", query: Query): ...

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.game.queries.remove(self.handle)

class DoubleAttackModifer(CreatureModifier):
    def handle(self, sender: "Creature", query: Query):
        if (
            sender.name == self.creature.name 
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2

class Creature:
    def __init__(self, game: Game, name: str, attack: int, defence: int):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defence = defence

    @property
    def attack(self):
        query = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defence(self):
        query = Query(self.name, WhatToQuery.DEFENCE, self.initial_defence)
        self.game.perform_query(self, query)
        return query.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defence})"


game = Game()
orc = Creature(game, "Orc King", 2, 2)
with DoubleAttackModifer(game, orc):
    print(orc)
print(orc)