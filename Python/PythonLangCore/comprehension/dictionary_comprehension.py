names = ["Aditi", "Sneha", "Rahul", "Vinayak"]
names_len = {name:len(name) for name in names}
print(names_len)



scores = {"Aditi": 88, "Rahul": 76, "Sneha": 92, "Aditya" : 76}
print({k: v for k, v in scores.items() if v >= 85})     # filter
print({k.upper(): v for k, v in scores.items()})        # transform keys
print({v: k for k, v in scores.items()})                # invert

# From two lists
print({k: v for k, v in zip(names, [88, 76, 92, 100])})
print({k for k, v in zip(names, [88, 76, 92, 100])})

print(type({k: v for k, v in zip(names, [88, 76, 92, 100])})) # dict
print(type({k for k, v in zip(names, [88, 76, 92, 100])})) # set