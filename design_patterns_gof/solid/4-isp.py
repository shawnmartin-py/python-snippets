from abc import ABC, abstractmethod

# Interface Segregation Principle

# Don't put too much into an interface; split into separate interfaces
# YAGNI - You Ain't Going to Need It

class Printer(ABC):
    @abstractmethod
    def print(self, document): ...

class Fax(ABC):
    @abstractmethod
    def fax(self, document): ...

class Scanner(ABC):
    @abstractmethod
    def scan(self, document): ...

class MultiFunctionDevice(Printer, Scanner): ...

class ConsolePrinter(Printer):
    def print(self, document):
        print(document)

class ConsoleScanner(Scanner):
        def scan(self, document: str):
            return "-" * 50 + "\n" + document + "\n" + "-" * 50 

class ConsoleMultiFunctionDevice(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner
        self.document = ""

    def print(self):
        self.printer.print(self.document)

    def scan(self, document: str):
        self.document = self.scanner.scan(document)

#-----------------------------------------------------------------------------#

m = ConsoleMultiFunctionDevice(ConsolePrinter(), ConsoleScanner())
m.print()
m.scan("some text")
m.print()