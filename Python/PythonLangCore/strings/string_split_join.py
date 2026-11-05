s = "Classic Cars"

# Split fn
# By Default the delimiter is whitespace
# splits = s.split()
splits = s.split(" ")
print(splits)  # Output: ['Classic', 'Cars']
print(type(splits))  # Output: <class 'list'>

print("a-b-c".split("-"))  # Output: ['a', 'b', 'c']
print("a,b,ccc".split(","))  # Output: ['a', 'b', 'c']

# Join fn
print("-".join(["a", "b", "c"]))  # Output: a-b-c
print("-".join(splits))  # Output: Classic-Cars