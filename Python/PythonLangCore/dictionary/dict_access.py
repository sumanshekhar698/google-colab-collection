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
# print(customer["name"])  # KeyError: 'name'

print(customer.get("customerName"))  # Output: Atelier graphique (accessing a value using its key)
print(customer.get("name"))  # Output: None (accessing a non-existent key)
print(customer.get("name", "Key not found"))  # Output: Key not found (accessing a non-existent key with a default value)
