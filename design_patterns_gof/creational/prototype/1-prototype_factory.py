from copy import deepcopy
from dataclasses import dataclass

# Prototype

@dataclass
class Address:
    street_address: str
    city: str
    country: str

@dataclass
class Employee:
    name: str
    address: Address

class EmployeeFactory:
    _main_office_employee = Employee("", Address("123", "London", "UK"))
    _aux_office_employee = Employee("", Address("125", "London", "UK"))

    @staticmethod
    def _new_employee(proto: Employee, name: str) -> Employee:
        result = deepcopy(proto)
        result.name = name
        return result

    @classmethod
    def main_office_employee(cls, name: str):
        return cls._new_employee(cls._main_office_employee, name)

#-----------------------------------------------------------------------------#

employee = EmployeeFactory.main_office_employee("John")
print(employee)