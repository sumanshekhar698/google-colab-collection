s = {32,43,3,3,3,343,5,43,53,5,5,35,3,35,3,5,3,5,3,5,3,5,3,5,3,5}
#  the elements in the set should be immutable (hashable) and unique. Duplicates will be removed automatically.

print(s)  # Output: {32, 3, 5, 35, 43, 53, 343} (duplicates are removed and order is not guaranteed)
print(type(s))  # Output: <class 'set'>
print(len(s))  # Output: 6 (the number of unique elements in the set)

list_with_duplicates = [32,43,3,3,3,343,5,43,53,333,1005,5,35,3,35,3,5,3,5,3,5,3,5,3,5,3,5]
unique_set = set(list_with_duplicates)  # Convert the list to a set to remove duplicates
print(unique_set)  # Output: {32, 3, 5, 35, 43, 53, 343} (duplicates are removed)


empty_set = {}
print(type(empty_set))  # Output: <class 'dict'> (this is an empty dictionary, not a set)

empty_set_correct = set()  # Correct way to create an empty set
print(type(empty_set_correct))  # Output: <class 'set'> (this is an

empty_set_correct.add(10)  # Adding an element to the set
empty_set_correct.update(s)  # Adding elements from another set
empty_set_correct.update([1, 2, 3])  # Adding elements from a list

# empty_set_correct.remove(322)  # Removing an element from the set (will raise KeyError if the element does not exist)
empty_set_correct.discard(3)  # Removing an element from the set (if it exists)

print(empty_set_correct)  # Output: {10} (the set now contains one element)
print(10 in empty_set_correct)  # Output: True (checking if 10 is in the set)


s1 = {(1, 2, 2, 3), 4,(1, 2, 2, 3), 6, 4,(1, 2, 2), 5} #{(1, 2, 2), 4, 5, 6, (1, 2, 2, 3)}
# s1 = {(1, 2, 2, 3), 4,(1, 2, 2, 3), 6, 4,(1, 2, 2), 5, {32,43}} #TypeError: unhashable type: 'set'
print(s1)  # Output: {(1, 2, 3), 4, 5} (the set contains a tuple and two integers)