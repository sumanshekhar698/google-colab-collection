a = 1
b = 2
c = 3


# Multiple assignment
a , b , c = 10, 20, 30

print(a, b, c)  # 10 20 30


x = 8
y = 9

#Dynamic swapping of two numbers without using a temporary variable
x , y = y, x
print(x, y)  # 9 8

# Chain assignment
a = b = c = 100
print(a, b, c)  # 100 100 100