fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for fruit in fruits:
#     print(fruit)


# for i in range(len(fruits)):
#     print(f"Index: {i}, Fruit: {fruits[i]}" )

# Pythonic way to enumerate through a list
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")


# Pythonic way to enumerate through a list
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")