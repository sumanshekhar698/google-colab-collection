print("START")
def divide_safe(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e} {type(e)}")
        return None
    except TypeError as e:
        print(f"TypeError caught: {e} {type(e)}")
        return None


print(divide_safe(8,2),end="\n\n")
print(divide_safe(0,0),end="\n\n")
print(divide_safe("0",0),end="\n\n")
# print(divide_safe([],None),end="\n\n")
# print(divide_safe(0),end="\n\n")


# try:
#     print(divide_safe(0),end="\n\n")
# except TypeError as e:
#     print(f"TypeError caught: {e} {type(e)}")


    
print("END")