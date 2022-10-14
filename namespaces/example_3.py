def setup():
    global n, karr, varr
    n = 8
    karr = [[] for _ in range(n)]
    varr = [[] for _ in range(n)]

def store(key, value):
    i = hash(key) % n
    karr[i] += [key]
    varr[i] += [value]

def lookup(key):
    i = hash(key) % n
    try:
        j = karr[i].index(key)
    except ValueError:
        raise KeyError(key)
    return varr[i][j]


if __name__ == "__main__":

    setup()
    store("name", "john")
    store("age", 24)

    print(lookup("name"))