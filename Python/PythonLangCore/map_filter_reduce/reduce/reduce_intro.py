from functools import reduce

nums = [1, 2, 3, 4, 5]

# print(sum(nums))

#  EAGER
# reduce reduces to one value
sum_reduce_obj = reduce(lambda a,b: a+b, nums)
# a=1  b=2 ->3
# a=3 b=3 ->6
# a=6 b=4 -> 10
# a=10 b=5 -> 15

print(sum_reduce_obj)
print(type(sum_reduce_obj))



# 2. Multiply all numbers.
print(reduce(lambda a, b: a * b, nums))  # 120
# 1 * 2 → 2
# 2 * 3 → 6
# 6 * 4 → 24
# 24 * 5 → 120
# This equals 5! because nums contains the integers 1 through 5.

# 3. Keep whichever value is larger.
print(reduce(lambda a, b: a if a > b else b, nums))  # 5
# Compare 1 and 2 → keep 2
# Compare 2 and 3 → keep 3
# Compare 3 and 4 → keep 4
# Compare 4 and 5 → keep 5

# 4. Start the accumulator at 100.
print(reduce(lambda a, b: a + b, nums, 100))  # 115
# 100 + 1 → 101
# 101 + 2 → 103
# 103 + 3 → 106
# 106 + 4 → 110
# 110 + 5 → 115

# 5. Builtins express these common operations more clearly.
print(sum(nums), max(nums))  # 15 5

# Unlike map(), which returns a lazy iterator, reduce() processes the iterable
# immediately and returns the final accumulated value.


