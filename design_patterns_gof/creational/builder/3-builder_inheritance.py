# Builder Inheritance
from abc import ABC

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return (
            f"{self.name} born on {self.date_of_birth} works as"
            f" {self.position}"
        )

class PersonBuilderMixin(ABC):
    person = Person

class NameBuilderMixin(PersonBuilderMixin):
    def called(self, name):
        self.person.name = name
        return self

class JobBuilderMixin(PersonBuilderMixin):
    def works_as_a(self, position):
        self.person.position = position
        return self

class BirthDateBuilderMixin(PersonBuilderMixin):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

class PersonInfoBuilderMixin(
    NameBuilderMixin,
    BirthDateBuilderMixin,
    JobBuilderMixin,
): ...

class PersonBuilder(PersonInfoBuilderMixin):
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

pb = PersonBuilder().called("John").works_as_a("CTO").born("1990").build()
print(pb)