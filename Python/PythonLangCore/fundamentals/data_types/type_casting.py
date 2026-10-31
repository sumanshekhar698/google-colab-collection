print(43)
print(type(43))

print("44")
print(type("44"))

print(int("45"))
print(type(int("45")))

print(float("46"))
print(type(float("46")))

print(str(47))
print(type(str(47)))

print(3.99)
print(type(3.99))
print(int(3.99)) # It will truncate the decimal part and return 3
print(type(int(3.99)))

print(round(3.99)) # It will round to the nearest integer and return 4

# print(int("3.14")) # This will raise a ValueError because "3.14" is not a valid integer string. You can first convert it to a float and then to an int if you want to get the integer part.
print(float("3.14"))
print(int(float("3.14")))
print(bool(0), bool(1), bool(""), bool("a"), bool([]), bool([0]))