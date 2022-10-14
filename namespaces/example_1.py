from types import SimpleNamespace


# Namespaces

d = dict()
d["name"] = "john"
print(d["name"])

x = 10
globals()["x"]
globals()["x"] = 11
print(x)

ns = SimpleNamespace(x=99, y=100)
print(ns)
print(ns.x)

