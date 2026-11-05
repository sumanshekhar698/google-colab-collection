scores = {"Aditi": 88, "Rahul": 76, "Sneha": 92, "Aditya": 88, "Arpit": 76}

print(sorted(scores.items()))  # Output: [('Aditya', 88), ('Aditi', 88), ('Rahul', 76), ('Sneha', 92)] (the key-value pairs of the dictionary sorted by keys)
print(sorted(scores.items(), reverse=True))  # Output: [('Sneha', 92), ('Rahul', 76), ('Aditi', 88), ('Aditya', 88)] (the key-value pairs of the dictionary sorted by keys in descending order)

# Aggregate functions on dictionary values
print(max(scores, key=scores.get))      # Sneha
print(min(scores, key=scores.get))      # Rahul

# Sum and Average
print(sum(scores.values()),
      round(sum(scores.values()) / len(scores), 1))


# Inverting the dictionary (swapping keys and values) | If values are not unique, the last key-value pair will overwrite the previous ones.
print({v: k for k, v in scores.items()})
