import json

data = {
    "orderNumber": 10100,
    "customer": "Online Diecast Creations Co.",
    "lines": [
        {"product": "S18_1749", "qty": 30},
        {"product": "S18_2248", "qty": 50},
    ],
}

# writing
with open("order.json", "w") as f:
    # json.dump(data,f)
    json.dump(data,f, indent=2)


# reading
with open("order.json", "r") as f:
    # json.dump(data,f)
    # i/p => file ref
    loaded = json.load(f)


print(type(loaded))
print(loaded)
print(loaded["customer"])

# o/p => string
s = json.dumps(data)
print(type(s))
print(s)

# i/p => string JSON data
print(json.loads(s)["orderNumber"])