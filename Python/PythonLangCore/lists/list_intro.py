items = ["a", "b"]


items.append("c")
print(items)  # Output: ['a', 'b', 'c']


items.append(["d", "e"])
print(items)  # Output: ['a', 'b', 'c']
items.append(["d", "e"])
print(items)  # Output: ['a', 'b', 'c']

items.extend(["d", "e"])
print(items)  # Output: ['a', 'b', 'c', ['d', 'e'], 'f', 'g']

items.extend(["d", "e"])
print(items)  # Output: ['a', 'b', 'c', ['d', 'e'], 'f', 'g']

items.insert(1, "x")
print(items)  # Output: ['a', 'x', 'b', 'c', ['d', 'e'], ['d', 'e'], 'd', 'e', 'd', 'e']


items.insert(6, "b")
print(items)  # Output: ['a', 'x', 'b', 'c', ['d', 'e'], ['d', 'e'], 'b', 'd', 'e', 'd', 'e']
print(items[4])  # Output: ['d', 'e']
print(items.count("d"))  # Output: 2
print(items.index("b"))  # Output: 2

items.remove("b")# will remove the first occurrence of "b" from the list
print(items)  # Output: ['a', 'x', 'c', ['d', 'e'], ['d', 'e'], 'b', 'd', 'e', 'd', 'e']
items.remove("b")
print(items)  # Output: ['a', 'x', 'c', ['d', 'e'], ['d', 'e'], 'b', 'd', 'e', 'd', 'e']


popped_item = items.pop()  # will remove the last item from the list
print(popped_item)  # Output: 'e'
print(items)  # Output: ['a', 'x', 'c', ['d', 'e'], ['d', 'e'], 'b', 'd', 'e', 'd', 'e']

popped_item_2 = items.pop(2)  # will remove the item at index 2
print(popped_item_2)  # Output: 'c'
print(items)  # Output: ['a', 'x', ['d', 'e'], ['d', 'e'], 'b', 'd', 'e', 'd', 'e']

items.reverse()  # will reverse the list in place
print(items)  # Output: ['e', 'd', 'e', 'b', ['d', 'e'], ['d', 'e'], 'x', 'a']

items.clear()  # will remove all items from the list
print(items)  # Output: []