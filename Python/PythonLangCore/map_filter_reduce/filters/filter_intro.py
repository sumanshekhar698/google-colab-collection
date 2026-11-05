nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# LAZY
# EXHAUSTIBLE
even_filter = filter(lambda x:x%2 == 0, nums)
odd_filter = filter(lambda x:x%2 != 0, nums)

print(type(even_filter))
print(type(odd_filter))
 
even_numbers_list = list(even_filter)
odd_numbers_list = list(odd_filter)

print(even_numbers_list)
print(odd_numbers_list)

even_numbers_list = list(even_filter)
print(even_numbers_list)