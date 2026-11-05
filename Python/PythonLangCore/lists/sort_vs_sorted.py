nums = [12,23,23,23,2,32,3,13,1,1,1,1,1,1,-1221]



sorted_nums = sorted(nums)  # Returns a new sorted list
print(sorted_nums)  # Output: [-1221, 1, 1, 1, 1, 1, 1, 2, 3, 12, 13, 23, 23, 23, 32]
print(nums)  # Output: [12, 23, 23, 23, 2, 32, 3, 13, 1, 1, 1, 1, 1, 1, -1221]


nums.sort()  # Sorts the list in place
# Every method is a function BUT not every function is a method. A method is a function that is associated with an object and can be called on that object. In Python, methods are defined within classes and are called on instances of those classes. Functions, on the other hand, are standalone blocks of code that can be called independently.
print(nums)  # Output: [-1221, 1, 1, 1, 1, 1, 1, 2, 3, 12, 13, 23, 23, 23, 32]