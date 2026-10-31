
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))  # Output: 15


def total_sum(*numbers):
    """Function to calculate the sum of any number of arguments."""
    print(type(numbers))
    return sum(numbers)

sum1 = total_sum(5,4,5,15,1,5,1,54)
print(sum1)



def total_sum2(num, *numbers):
    """Function to calculate the sum of any number of arguments."""
    print(type(numbers))
    return sum(numbers)

sum = total_sum2(5,5,5)
print(sum)