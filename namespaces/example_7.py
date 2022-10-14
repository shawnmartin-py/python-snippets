class Dict:

    def __init__(self):
        self.n = 8
        self.karr = [[] for _ in range(self.n)]
        self.varr = [[] for _ in range(self.n)]

    def __setitem__(self, key, value):
        i = hash(key) % self.n
        self.karr[i] += [key]
        self.varr[i] += [value]

    def __getitem__(self, key):
        i = hash(key) % self.n
        try:
            j = self.karr[i].index(key)
        except ValueError:
            raise KeyError(key)
        return self.varr[i][j]


if __name__ == "__main__":

    d1 = Dict()
    d1["name"] = "john"
    d1["age"] = 24

    print(d1["name"])

    ns2 = Dict()