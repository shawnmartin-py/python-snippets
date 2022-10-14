from abc import ABC, abstractmethod
from enum import Enum

# Dependency Inversion Principle

# High-level modules should not depend upon low-level ones; use abstractions

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class AbstractRelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name): ...

class Relationships(AbstractRelationshipBrowser):  # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):  # solution
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:  # high-level
    # def __init__(self, relationships: Relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}.")
    def __init__(self, browser: AbstractRelationshipBrowser):
        name = "John"
        for p in browser.find_all_children_of(name):
            print(f"{name} has a child called {p}.")
            
#-----------------------------------------------------------------------------#

parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
Research(relationships)
