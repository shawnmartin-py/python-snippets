from abc import ABC, abstractmethod
from dataclasses import dataclass

# Method Chain

@dataclass
class Creature:
    name: str
    attack: int
    defence: int

class CreatureModifier:
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier: CreatureModifier = None

    def add_modifier(self, modifier: "CreatureModifier"):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print("Doubling Attack")
        self.creature.attack *= 2
        super().handle()


creature = Creature("Orc", 1, 1)
root = CreatureModifier(creature)
root.add_modifier(DoubleAttackModifier(creature))
root.handle()
print(creature)
