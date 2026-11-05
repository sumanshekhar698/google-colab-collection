from collections import Counter


def first_unique_char_using_counter(s: str) -> int:
    char_count = Counter(s)
    print(char_count)

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1

first_unique_char_using_counter("leetcode")



def first_unique_char(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1


print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))  # -1