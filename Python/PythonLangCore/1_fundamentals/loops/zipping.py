# zip() iterates two or more sequences in parallel
names  = ["Aditi", "Rahul", "Sneha","Ankit"]
scores = [88, 76, 92, 100, 20]


# ZIPPING the two lists together |  drops the extra elements if the lists are of unequal length and shortest list is prioritized
for name, score in zip(names, scores):
    print(f"{name}: {score}")



pairs = [("a", 1), ("b", 2), ("c", 3)] #LIST OF TUPLES
#UNZIPPING The list of tuples into two separate iterables using the * operator
letters, numbers = zip(*pairs)

print(letters)  # ('a', 'b', 'c')
print(type(numbers))  # <class 'tuple'>
print(numbers)  # (1, 2, 3)
print(type(letters))  # <class 'tuple'>
