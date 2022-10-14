# Command

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
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

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

account = BankAccount()
cmd = BankAccountCommand(account, BankAccountCommand.Action.DEPOSIT, 100)

print(account)
