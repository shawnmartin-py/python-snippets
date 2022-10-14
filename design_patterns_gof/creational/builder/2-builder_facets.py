# Builder Facets

class Person:
    def __init__(self):
        self.street_address = None
        self.postcode = None
        self.city = None

        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}"
            f" Employed at {self.company_name} as a {self.position} earning"
            f" {self.annual_income}"
        )

class PersonBuilder:
    def __init__(self, person: Person | None = None):
        self.person = person or Person()

    @property
    def works(self) -> "PersonJobBuilder":
        return PersonJobBuilder(self.person)

    @property
    def lives(self) -> "PersonAddressBuilder":
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income: int):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self
    
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

#-----------------------------------------------------------------------------#

pb = PersonBuilder()
person = pb.works.at("PMY").as_a("developer").earning(60_000)
person.lives.at("Alvor").with_postcode("8500").in_city("Portimao")
print(person.build())
