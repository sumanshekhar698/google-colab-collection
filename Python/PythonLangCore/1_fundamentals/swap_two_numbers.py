x = 8
y = 9
print("type of x:", type(x))  # <class 'int'>
print("Before swapping: x =", x, "y =", y)

# Swapping the values (Classic way using a temporary variable)
temp = x
x = y
y = temp

print("After swapping: x =", x, "y =", y)



# (Pythonically, we can swap two numbers without using a temporary variable. Here are a few ways to do it.)
x, y = y, x
print("After swapping (using tuple unpacking): x =", x, "y =", y)