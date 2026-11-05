# A named function...
def square(x):
    return x * x

square_lambda = lambda x:x*x
print(square(8),square_lambda(8))
print(square(8),square_lambda(8))
print(square(8),square_lambda(8))

power_lambda = lambda a,b: a**b
print(power_lambda(5,4))


# With a default
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Suman"))
print(greet("Suman","Happy Diwali"))