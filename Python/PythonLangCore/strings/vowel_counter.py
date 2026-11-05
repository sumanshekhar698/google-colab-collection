
def count_vowels(input_string):
    """
    Counts the number of vowels in the given input string.

    Parameters:
    input_string (str): The string in which to count vowels.

    Returns:
    int: The count of vowels in the input string.
    """
    vowels = "aeiou"
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1

    return count

print(count_vowels("Hello World"))  # Output: 3