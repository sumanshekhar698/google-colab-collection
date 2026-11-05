point = (3, 4)
print(point)  # Output: (3, 4)
print(type(point))  # Output: <class 'tuple'>
print(point[0])  # Output: 3
print(point[1])  # Output: 4
print(len(point))  # Output: 2
print(point[0:2])  # Output: (3, 4)

point_alias = point  # This creates an alias, not a copy

# point[0] = 5  # This will raise a TypeError because tuples are immutable
# point.copy()  # This will raise an AttributeError because tuples do not have a copy method

point_dup = point + (5, 6)  # This creates a new tuple by concatenating the original tuple with another tuple 
print(point_dup)  # Output: (3, 4, 5, 6)

not_a_tuple = (5)
print(type(not_a_tuple))  # Output: <class 'int'> (not a tuple)
single_element_tuple_correct = (5,)
print(type(single_element_tuple_correct))  # Output: <class 'tuple'> (correct way to create a single-element tuple)