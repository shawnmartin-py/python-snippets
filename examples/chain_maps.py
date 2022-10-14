from collections import ChainMap, deque


net = ChainMap({"a": 10, "b": 15})
net.maps = deque(net.maps)

print(f"{net['a'] = }")

net.maps.appendleft({"a": 15})
print(f"{net['a'] = }")


net.maps.popleft()
print(f"{net['a'] = }")