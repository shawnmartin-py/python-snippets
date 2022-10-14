import pandas as pd
import sqlalchemy as sql


class Customer:
    @classmethod
    def from_tuple(cls, tuple: tuple[str, str]) -> "Customer": ...

class CustomerSource:
    def get_customers(self):
        return [
            Customer.from_tuple(value)
            for value in pd.read_sql(...).itertuples()
        ]

class Main:
    class _Source:
        def get_customers(self) -> Customer: ...

    def __init__(self, source: _Source):
        self.source = source

    def run(self):
        customers = self.source.get_customers()


if __name__ == "__main__":
    app = Main(CustomerSource())
    app.run()