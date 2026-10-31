# type() tells you what something is
print(type(42))
print(type(3.14))
print(type("hello"))


print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"a": 1}))
print(type({1, 2, 3}))



print(isinstance(42, int))  # True
print(isinstance(3.14, float))  # True
print(isinstance("hello", str))  # True

print(isinstance("Hi", (int, float)))  # False