# listen and silent are anagrams of each other
print(sorted("listen"))  # Output: ['e', 'i', 'l', 'n', 's', 't']
print(sorted("silent"))  # Output: ['e', 'i', 'l', 'n', 's', 't']


def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)# O(n) = 2 nlogn = nlogn
    # nlogn > n

# Test the function
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))  # Output: False