# Composite Command

from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: float = 0):
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposit: {amount}, Balance: {self.balance}")

    def withdraw(self, amount: float):
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew: {amount}, Balance: {self.balance}")
            return True
        return False

    def __str__(self) -> str:
        return f"Balance: {self.balance}"

class Command(ABC):
    def __init__(self):
        self.success = False

    @abstractmethod
    def invoke(self): ...

    @abstractmethod
    def undo(self): ...

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(
        self,
        account: BankAccount,
        action: "BankAccountCommand.Action",
        amount: float
    ):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)
        self.success = False

class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: list[Command] | None = None):
        if items is None:
            items: list[Command] = []
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()

class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(
        self, from_account: BankAccount,
        to_account: BankAccount,
        amount: float
    ):
        super().__init__(
            [
                BankAccountCommand(
                    from_account,
                    BankAccountCommand.Action.WITHDRAW,
                    amount,
                ),
                BankAccountCommand(
                    to_account,
                    BankAccountCommand.Action.DEPOSIT,
                    amount,
                ),
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


account = BankAccount(120)
account2 = BankAccount(120)
transfer = MoneyTransferCommand(account, account2, 10)

transfer.invoke()
print(account, account2)
