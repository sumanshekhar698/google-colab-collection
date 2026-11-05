# Modifying
customer = {"name": "Atelier graphique"}

customer["name"] = "John Doe"  # Modifying an existing key-value pair
customer["age"] = 30  # Adding a new key-value pair
print(customer)  # Output: {'name': 'John Doe', 'age': 30} (the dictionary now has two key-value pairs)

customer.update({"country": "USA", "balance": 1000, "age": 35})  # Adding multiple key-value pairs
print(customer)  # Output: {'name': 'John Doe', 'age': 35, 'country': 'USA', 'balance': 1000} (the dictionary now has four key-value pairs, and the value of "age" has been updated to 35)

balance = customer.pop("balance")  # Removing a key-value pair
print(balance)  # Output: 1000 (the value of the removed key)
print(customer)  # Output: {'name': 'John Doe', 'age': 35, 'country': 'USA'} (the dictionary now has three key-value pairs)


# print(customer.pop("balance"))  # Output: KeyError: 'balance' (trying to remove a non-existent key will raise a KeyError)
print(customer.pop("balance", "Key not found"))  # Output: Key not found (trying to remove a non-existent key with a default value)

print(customer.popitem())  # Output: ('country', 'USA') (removes and returns the last inserted key-value pair)
print(customer)  # Output: {'name': 'John Doe', 'age': 35

del customer["age"]  # Removing a key-value pair using the del statement
# del customer["ages"]  # KeyError: 'ages'
print(customer)  # Output: {'name': 'John Doe'} (the dictionary now has

customer.setdefault("name", "Jane Smith")  # Adding a new key-value pair if the key does not exist
print(customer)  # Output: {'name': 'John Doe', 'age': 30}

customer.clear()  # Removing all key-value pairs from the dictionary
print(customer)  # Output: {} (the dictionary is now empty)