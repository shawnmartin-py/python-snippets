import pandas as pd
import sqlalchemy as sql


class SqlSource:
    def __init__(self):
        self.query = "SELECT * FROM customer"
        self.engine = sql.create_engine()

    def get_data(self):
        return pd.read_sql(self.query, self.engine)


class Main:
    class _Source:
        def get_data(self) -> pd.DataFrame: ...

    def __init__(self, source: _Source):
        self.source = source

    def run(self):
        df = self.source.get_data()


if __name__ == "__main__":
    app = Main(SqlSource())
    app.run()