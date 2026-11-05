print("START")
def divide_unsafe(a,b):
    return a/b

# print(divide_unsafe(8,0))

# Exception Handling by YOU
try:
    print(divide_unsafe(8,2))
    print(divide_unsafe(8,0))
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e} {type(e)}")
    
print("END")

# 9/0