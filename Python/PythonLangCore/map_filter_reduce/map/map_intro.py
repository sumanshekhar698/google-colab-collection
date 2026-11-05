nums = [1,2,3,4,5]

# LAZY
mapped = map(lambda x : x*x, nums )

# 2. Generator expression: lazily evaluates an expression for each item.
generated = (x * x for x in nums)

print(type(mapped))

# print(next(mapped))
# print(next(generated))

# print(next(mapped))
# print(next(generated))

# print(next(mapped))
# print(next(generated))

# print(next(mapped))
# print(next(generated))

# print(next(mapped))
# print(next(generated))

# print(next(mapped))#StopIteration
# print(next(generated))#StopIteration

list_of_maps = list(mapped)
print(list_of_maps)

list_of_generated=list(generated)
print(list_of_generated)

list_of_maps = list(mapped)
print(list_of_maps)

list_of_generated=list(generated)
print(list_of_generated)

# EAGER
list_of_squares=[x*x for x in nums]
print(list_of_squares)