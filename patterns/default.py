import pandas as pd
import sqlalchemy as sql


class Main:
    def run(self):
        engine = sql.create_engine()
        df = pd.read_sql(
            "SELECT * FROM customer",
            con=engine
        )

if __name__ == "__main__":
    app = Main()
    app.run()