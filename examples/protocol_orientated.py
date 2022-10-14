class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"{type(self).__name__}(*{self.coeffs})"

    def __add__(self, other: "Polynomial"):
        return type(self)(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    
    def __len__(self):
        return len(self.coeffs)

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)


print(p1 + p2)