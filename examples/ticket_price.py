# $180 + $0.04 attendee

# 120 = 5$
# 15 = $0.10


# 5$ = 120 people, $600 ticket sales, $184,80 show cost, profit = $415,20
# $2.90 = 435 people, $1261,50 ticket sales, $197,40 show cost, profit = $1064,10

from functools import total_ordering


class Dollar(float):
    def __str__(self):
        return f"${self:.2f}"

    def to_cents(self) -> float:
        return self * 100

    @classmethod
    def from_cents(cls, cents: int):
        return Dollar(round(cents / 100, 2))


@total_ordering
class Session:
    FIXED_SHOW_PRICE = 180
    COST_PER_HEAD = .04
    BASE_TICKET_PRICE = 5
    BASE_ATTENDANCE = 120
    AVG_ATTENDANCE_CHANGE_PER_DOLLAR = 150

    def __init__(self, price: float):
        self.price = Dollar(price)
    
    @property
    def _attendees(self) -> int:
        return self.BASE_ATTENDANCE + round(
            (self.BASE_TICKET_PRICE - self.price)
            * self.AVG_ATTENDANCE_CHANGE_PER_DOLLAR
        )

    @property
    def _cost(self) -> float:
        return self.FIXED_SHOW_PRICE + round(
            self._attendees * self.COST_PER_HEAD,
            2,
        )

    @property
    def _income(self) -> float:
        return self._attendees * self.price

    @property
    def profit(self) -> Dollar:
        return Dollar(self._income - self._cost)

    def __eq__(self, other) -> bool:
        if isinstance(other, Session):
            return self.profit == other.profit
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Session):
            return self.profit < other.profit
        return NotImplemented

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.price!r})"


class SessionFactory:
    def __init__(self, max_price_dollars: float):
        max_price_cents = max_price_dollars * 100
        self.sessions = [
            Session(p) for p in
            (Dollar.from_cents(p + 10) for p in range(0, max_price_cents, 10))
        ]

    def _top_sessions(self, n: int):
        yield from sorted(self.sessions, reverse=True)[:n]

    def info_by_profit(self, n: int = 5):
        output = "-" * 16 + "\n"
        output += f"{'PRICE'} {'PROFIT':>10}\n" 
        output += "~" * 16 + "\n"
        return output + "\n".join(
            f"{session.price!s:>5} {session.profit!s:>10}"
            for session in self._top_sessions(n)
        )


sessions = SessionFactory(10)
print(sessions.info_by_profit())

