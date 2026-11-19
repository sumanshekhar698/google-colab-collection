values = [0, 1, -1, "", "a", [], [0], {}, {"a": 1}, None, 0.0]

for element in values:
    print(f"{repr(element)} is bool: {bool(element)}")