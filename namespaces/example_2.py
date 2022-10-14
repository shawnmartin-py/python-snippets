n = 8
karr = [[] for _ in range(n)]
varr = [[] for _ in range(n)]

print(karr)
print(varr)

key, value = "john", "john"
i = hash(key) % n

print(i)

karr[i] += [key]
varr[i] += [value]

print(karr)
print(varr)