def total_sum(*numbers):
    """Function to calculate the sum of any number of arguments."""
    print(type(numbers))
    return sum(numbers)

sum1 = total_sum(5,4,5,15,1,5,1,54)
print(sum1)


def min_max(*numbers):
    """Function to find the minimum and maximum of any number of arguments."""
    print(type(numbers))
    return min(numbers), max(numbers)

res = min_max(5, 4, 5, 15, 1, 5, 1, 54)
print(res)  # Output: (1, 54)
print(type(res))  # Output: <class 'tuple'> (the result is a tuple containing the min and max values)
min_val, max_val = res
print(f"Minimum: {min_val}, Maximum: {max_val}")


# Unpacking of Structures
person = ("Alice", 30, "Engineer")
print(person)  # Output: ("Alice", 30, "Engineer")
name, age, profession, = person  # Unpacking the tuple into variables
# name, age, profession, gender = person  # ValueError: not enough values to unpack (expected 4, got 3)

print(name)  # Output: Alice
print(age)  # Output: 30
print(profession)  # Output: Engineer


nums = (1,2,3,4,5)
first, *rest = nums  # Unpacking with the * operator to capture remaining elements
print(first)  # Output: 1
print(rest)  # Output: [2, 3, 4, 5]`
print(type(rest))  # Output: <class 'list'> (rest is a list)
print()

first, *middle, last = nums  # Unpacking with the * operator to capture middle elements
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5
print(type(middle))  # Output: <class 'list'> (middle is a list)
print(type(last))  # Output: <class 'int'> (last is an integer)

