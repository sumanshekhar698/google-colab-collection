
# Return a function from a function (a closure)
def multiplier(n):
    def inner(val):
        return val * n
    return inner


    # def inner(val):
    #     return val * 2
doubler = multiplier(2)
    # def inner(val):
    #     return val * 3
tripler = multiplier(3)

print(doubler(100))
print(tripler(100))