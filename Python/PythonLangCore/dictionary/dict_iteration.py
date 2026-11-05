# scores = {"Aditi": 88, "Rahul": 76, "Sneha": 92, 45: 85, "Rohit": 79}
scores = {"Aditi": 88, "Rahul": 76, "Sneha": 92, "Rohit": 79}

for key in scores:
    print(f"{key}: {scores[key]}")  # Output: Aditi: 88, Rahul: 76, Sneha: 92, 45: 85, Rohit: 79 (the keys and values of the dictionary)


print(scores.keys())  # Output: dict_keys(['Aditi', 'Rahul', 'Sneha', 45, 'Rohit']) (the keys of the dictionary)
print(type(scores.keys()))  # Output: <class 'dict_keys'> (the type of the keys view object)

print(scores.items())  # Output: dict_items([('Aditi', 88), ('Rahul', 76), ('Sneha', 92), (45, 85), ('Rohit', 79)]) (the key-value pairs of the dictionary)
print(type(scores.items()))  # Output: <class 'dict_items'> (the type of the items view object)

print(scores.values())  # Output: dict_values([88, 76, 92, 85, 79]) (the values of the dictionary)
print(type(scores.values()))  # Output: <class 'dict_values'> (the type of the values view object)

print("\nIterating over items:")

for key, value in scores.items():
    # scores["Aditya"] = 90  # Modifying the value of an existing key
    print(f"{key}: {value}")  # Output: Aditi: 88, Rahul: 76, Sneha: 92, 45: 85, Rohit: 79 (the keys and values of the dictionary)
