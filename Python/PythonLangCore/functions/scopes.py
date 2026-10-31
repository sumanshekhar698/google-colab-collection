x = "global"

def show_scope():
    # global x
    print(x)# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value | PreMature Access
    x = "local to x"
    local_x = "local to x" # Good Habit
    # y = "y in local"
    print(x)
    # print(y)

show_scope()
print(x)
# print(y)