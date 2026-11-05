import copy

original = [1,2,3,4,5]
alias = original  # This creates an alias, not a copy
alias.append(6)
print("Original List:", original)  # Output: [1, 2, 3, 4, 5, 6]
print("same object:", original is alias)  # Output: True



# What are the ways to copy a list in Python?
# It will create Shallow copies of the list. If the list contains mutable objects, changes to those objects will be reflected in both the original and copied lists.
# Shallow Copy: A shallow copy creates a new list object, but the elements in the new list are references to the same objects as those in the original list. If the elements are mutable (like lists or dictionaries), changes to those elements will affect both the original and copied lists.

# ==> 1. Shallow Copy using the copy() method:
print()
print(original)  # Output: [1, 2, 3, 4, 5, 6]
copy_of_original = original.copy()
copy_of_original.append(7)
print("Original List:", original)  # Output: [1, 2, 3, 4, 5, 6]
print("Copy of Original List:", copy_of_original)  # Output: [1, 2, 3, 4, 5, 6, 7]
# print("Copy of Original List:", copy_of_original)  # Output: [1, 2, 3, 4, 5]
print("same object:", original is copy_of_original)  # Output: False

# ==> 2. Shallow Copy using the slicing technique:
print()
copy_of_original_2 = original[:]
print("Copy of Original List (slice):", copy_of_original_2)  # Output: [1, 2, 3, 4, 5, 6]
copy_of_original_2.append(8)
print("Original List:", original)  # Output: [1, 2, 3, 4, 5, 6]
print("Copy of Original List (slice):", copy_of_original_2)  # Output: [1, 2, 3, 4, 5, 6, 8]
print("same object (slice):", original is copy_of_original_2)  # Output: False

# ==> 3. Shallow Copy using the list() constructor:
print()
copy_of_original_3 = list(original)  # Using the list() constructor to create a copy
print("Copy of Original List (list() constructor):", copy_of_original_3)  # Output: [1, 2, 3, 4, 5, 6]
copy_of_original_3.append(9)
print("Original List:", original)  # Output: [1, 2, 3, 4, 5, 6]
print("Copy of Original List (list() constructor):", copy_of_original_3)  # Output: [1, 2, 3, 4, 5, 6, 9]
print("same object (list() constructor):", original is copy_of_original_3)  # Output: False



# Deep Copy: A deep copy creates a new list object and recursively copies all the objects found in the original. This means that if the original list contains mutable objects, the deep copy will contain copies of those objects, and changes to them will not affect the original list.
# ==> 4. Deep Copy using the copy module:

nested = [[1, 2], [3, 4]]
print("\nOriginal Nested List:", nested)  # Output: [[1, 2], [3, 4]]
print("Original Nested List ID:", id(nested))  # Output: Memory address of the original nested list 
shallow_copy = nested.copy()  # This creates a shallow copy of the nested list

print("Shallow Copy ID:", id(shallow_copy))  # Output: Memory address of the shallow copy
print("Shallow Copy:", shallow_copy)  # Output: [[1, 2], [3, 4]]
shallow_copy[0].append(5)  # Modifying the first sublist in the shallow copy
print("After modifying shallow copy:")
print("Original Nested List:", nested)  # Output: [[1, 2, 5], [3, 4]] (the original list is affected)


nested = [[1, 2], [3, 4]]
# Creating a deep copy using the copy module
deep_copy = copy.deepcopy(nested)# recursively copies everything
print("Deep Copy ID:", id(deep_copy))  # Output: Memory address of the deep copy
print("Deep Copy:", deep_copy)  # Output: [[1, 2], [3, 4]]

deep_copy[0].append(6)  # Modifying the first sublist in the deep copy
print("After modifying deep copy:")
print("Original Nested List:", nested)  # Output: [[1, 2, 5], [3, 4]] (the original list is not affected)
print("Deep Copy:", deep_copy)  # Output: [[1, 2, 5, 6], [3, 4]]