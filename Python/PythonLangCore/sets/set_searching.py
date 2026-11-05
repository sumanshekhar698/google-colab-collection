import time

list_1million = list(range(1000000))  # Create a list with 1 million elements
set_1million = set(list_1million)  # Create a set with 1 million elements
target=199_999
# print(set_1million[0])  # This will raise an error because sets do not support indexing

# Search in list
time_start = time.time()
if target in list_1million:
    print(f"Found {target} in list")
time_end = time.time()
print(f"Time taken to search in list: {time_end - time_start} seconds")

# Search in set
time_start = time.time()
if target in set_1million:
    print(f"Found {target} in set")
time_end = time.time()
print(f"Time taken to search in set: {time_end - time_start} seconds")