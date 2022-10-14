class Network:
    def __init__(self, *resistors):
        self.resistors = resistors

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            ...
        return cls()