
def add_item_mutable(item, basket=[]):
    basket.append(item)
    print(f"Added {item} to basket. Current basket: {basket}")
    print(f"Basket ID: {id(basket)}")  # Print the memory address of the basket
    return basket

# MY Requirement: I want to modify the function so that it does not use a mutable default argument. Instead, it should create a NEW list each time the function is called without an explicit basket argument.
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    print(f"Added {item} to basket. Current basket: {basket}")
    print(f"Basket ID: {id(basket)}")  # Print the memory address of the basket
    return basket

# example of how the default mutable argument can lead to unexpected behavior
print(add_item_mutable("apple"))
print(add_item_mutable("banana"))
print(add_item_mutable("strawberry"))

print(add_item("apple"))
print(add_item("banana"))
print(add_item("strawberry"))

list_of_fruits = ["kiwi", "mango", "grape"]
add_item("orange", list_of_fruits)
print(list_of_fruits)  # Output: ['kiwi', 'mango', 'grape', 'orange']




# ============================= ==================================
print("\nDemonstrating the correct behavior with a new list each time:")
list_1 = [0]*3
print(id(list_1))  # Output: Memory address of list_1

print(list_1)  # Output: [0, 0, 0]
bad = [[0] * 3] * 3
for row in bad:
    print(id(row))

print(bad)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
bad[0][0] = -1
print(bad)  # Output: [[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]] (all rows are affected)


good = [[0] * 3 for suman in range(3)]
good[0][0] = 99
print(good)              # [[99,0,0], [0,0,0], [0,0,0]]     correct

for row in good:
    print(id(row))