x , y = 5, 10
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False


print(x == 5 and y == 10)  # True
print(x == 5 or y == 5)   # True

# and and or are logical operators, not comparison operators. They are used to combine multiple boolean expressions.

# They are short-circuit operators, meaning that they only evaluate the second expression if necessary. 
# For example, in the expression x == 5 or y == 5, if x is equal to 5, then the second expression (y == 5) will not be evaluated because the first expression is already True.

print()
print(True and False) # False
print(True or False) # True
print(not True) # False

# Chained comparison — Python allows this, most languages don't
print(1 < x < 10) # True
print(1 < y < 10) # False