def setup(ns):
    ns["n"] = 8
    ns["karr"] = [[] for _ in range(ns["n"])]
    ns["varr"] = [[] for _ in range(ns["n"])]

def store(ns, key, value):
    i = hash(key) % ns["n"]
    ns["karr"][i] += [key]
    ns["varr"][i] += [value]

def lookup(ns, key):
    i = hash(key) % ns["n"]
    try:
        j = ns["karr"][i].index(key)
    except ValueError:
        raise KeyError(key)
    return ns["varr"][i][j]


if __name__ == "__main__":

    ns1 = {}
    setup(ns1)
    store(ns1, "name", "john")
    store(ns1, "age", 24)

    print(lookup(ns1, "name"))

    ns2 = globals()