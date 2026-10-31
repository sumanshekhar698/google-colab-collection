
print("e" in "Hello, World!") # True
print("a" in "Hello, World!") # False


print("Hello" not in "Hello, World!") # False
print(10 in [3,56,78]) # False

list_a = [1, 2, 3]
list_b = [1, 2, 3]


# 'is' vs '=='
print(list_a is list_b)  # False, because they are different objects in memory
print(list_a == list_b)  # True, because they have the same content

list_c = list_a
print(list_c is list_a)  # True, because they are the same object in memory



# Integer caching in Python
d = 257
e = 257

print(d is e)



x = 255
y = 255
z = 255
print(x is y)
print(x is z)

print(id(x))
print(id(y))
print(id(z))

print(x is None)  # False, because x is an integer, not None
print(None is None)  # True, because None is a singleton object