age = 25
name = "Suman"

print(type(age))  # <class 'int'>
print(age)        # 25
print(id(age))    # Object's identity: a number

print(type(name))  # <class 'str'>
print(name)        # SUMAN
print(id(name))    # Object's identity: a number
print(name.upper())  # methods


def add(a, b):
    total = a + b
    return total


print(type(add))  # <class 'function'>
print(add)        # <function add at 0x...>
print(id(add))    # Object's identity: a number

print(id(print))    # Object's identity: a number

