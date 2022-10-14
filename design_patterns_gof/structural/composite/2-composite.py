from collections.abc import Iterable

# Composite

class Connectable(Iterable):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)
        
class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return (
            f"{self.name}, {len(self.inputs)} inputs, {len(self.outputs)}"
            " outputs"
        )

    def __iter__(self):
        yield self

class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"

#-----------------------------------------------------------------------------#

n1 = Neuron("n1")
n2 = Neuron("n2")
l1 = NeuronLayer("l1", 3)
l2 = NeuronLayer("l2", 4)

# n1.connect_to(l1)
# l2.connect_to(n2)

print(n1)
print(n2)
print(l1)
print(l2)

