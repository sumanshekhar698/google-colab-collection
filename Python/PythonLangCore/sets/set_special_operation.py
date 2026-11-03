a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b, "union")                  # {1,2,3,4,5,6}
print(a & b, "intersection")           # {3,4}
print(a - b, "difference")             # {1,2}
print(b - a, "difference reversed")    # {5,6}
print(a ^ b, "symmetric difference")   # {1,2,5,6}

print(a.issubset({1,2,3,4,5}))         # True
print(a.isdisjoint({7,8}))             # True