nums = list(range(1, 11))

even_filter = filter(lambda x:x%2 == 0, nums)

mapped = map(lambda x : x*x, even_filter )

even_squares_list = list(mapped)
print(even_squares_list)