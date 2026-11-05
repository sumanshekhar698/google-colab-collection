import time

words = ["Hey", "Hi"] * 20000
print(len(words))  # Output: 20000
# print(words)  # Output: ['Hey', 'Hi'] * 20000

# Classic way of concatenating strings using + operator
start = time.time()
s = ""
for w in words:
    s += w
end = time.time()
print(f"Time taken: {end - start} seconds")# Time taken: 0.07741570472717285 seconds


# Using join() method to concatenate strings
start = time.time()
s = "".join(words)
end = time.time()
print(f"Time taken: {end - start} seconds")# Time taken: 0.00022101402282714844 seconds