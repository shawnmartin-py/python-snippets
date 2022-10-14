class Dict:

    def setup(self):
        self.n = 8
        self.karr = [[] for _ in range(self.n)]
        self.varr = [[] for _ in range(self.n)]

    def store(self, key, value):
        i = hash(key) % self.n
        self.karr[i] += [key]
        self.varr[i] += [value]

    def lookup(self, key):
        i = hash(key) % self.n
        try:
            j = self.karr[i].index(key)
        except ValueError:
            raise KeyError(key)
        return self.varr[i][j]


if __name__ == "__main__":

    d1 = Dict()
    d1.setup()
    d1.store("name", "john")
    d1.store("age", 24)

    print(d1.lookup("name"))

    ns2 = Dict()