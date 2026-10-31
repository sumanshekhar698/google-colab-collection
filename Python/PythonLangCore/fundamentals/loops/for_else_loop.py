numbers = [2, 4, 6, 8]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list.") # this else block will execute if the loop completes without hitting a break statement