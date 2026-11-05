print("START")
def divide_safe(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e} {type(e)}")
        return None


print(divide_safe(8,2),end="\n\n")
print(divide_safe(0,0),end="\n\n")
print(divide_safe(10,2),end="\n\n")
print(divide_safe(10,0),end="\n\n")
print(divide_safe(10,5),end="\n\n")
print(divide_safe(10,5),end="\n\n")
    
print("END")