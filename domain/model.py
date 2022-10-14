from datetime import date, timedelta
from dataclasses import dataclass


today = date.today()
tomorrow = date.today() + timedelta(days=1)
later = date.today() + timedelta(days=5)


class OutOfStock(Exception): ...


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(
        self, ref: str, sku: str, qty: int, eta: date | None
    ):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)
        
    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty

    def __gt__(self, other: "Batch"):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
    except StopIteration as exception:
        raise OutOfStock(f"Out of stock for sku {line.sku}") from exception
    batch.allocate(line)
    return batch.reference