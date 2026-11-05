try:
    res=10/0
except:
    pass


try:
    result = 10 / 0
except Exception as e:
    print(e)
    result = None

print(result)


# GOOD: catch what you expect, and say something
x = "0"
try:
    result = 10 / x
except ZeroDivisionError as e:
    print(f"Expected failure, using default. ({e})")
    result = 0
except Exception as e:
    print(f"Unknown failure. ({e})")
    result = 0



print(result)
print("END")