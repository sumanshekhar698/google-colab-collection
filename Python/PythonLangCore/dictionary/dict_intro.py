customer = {
    "customerNumber": 103,
    "customerName": "Atelier graphique",
    "country": "France",
    "creditLimit": 21000.00,
    "balance": 103,
}

# The keys should be unique, so if you try to add a key that already exists, it will overwrite the existing value.
# The keys should be immutable (hashable) types, such as strings, numbers, or tuples. Lists and dictionaries cannot be used as keys because they are mutable.


print(customer)  # Output: {'customerNumber': 103, 'customerName': 'Atelier graphique', 'country': 'France', 'creditLimit': 21000.0, 'balance': 103}
print(customer["customerName"])  # Output: Atelier graphique (accessing a value using its key)
print(len(customer))  # Output: 5 (the number of key-value pairs in the dictionary)


empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'> (this is an empty dictionary)

d1 = dict(a=1, b=2)
d2 = dict([("a", 1), ("b", 2)])