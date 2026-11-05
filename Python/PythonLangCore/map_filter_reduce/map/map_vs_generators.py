nums = [1, 2, 3, 4, 5]

# nums_str = ['1', '2', '3', '4', '5']

# LAZY
mapped_str = map(str,nums)
generated_str = (str(num) for num in nums)


print(list(mapped_str))
print(list(generated_str))

even_squares = (x * x for x in nums if x % 2 == 0)



# map + filter nested — hard to read
list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))

# comprehension — obvious
[x * 2 for x in nums if x % 2 == 0]