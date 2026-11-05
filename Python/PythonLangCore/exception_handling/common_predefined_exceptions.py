examples = [
    ("ValueError",       lambda: int("abc")),
    ("TypeError",        lambda: "a" + 1),
    ("KeyError",         lambda: {"a": 1}["b"]),
    ("IndexError",       lambda: [1, 2, 3][99]),
    ("ZeroDivisionError",lambda: 1 / 0),
    ("AttributeError",   lambda: "abc".push("d")),
    ("NameError",        lambda: undefined_variable),
    ("FileNotFoundError",lambda: open("no_such_file.txt")),
]

for name, fn in examples:
    try:
        fn()
    except Exception as e:
        print(f"{name:<20} {type(e).__name__:<20} {e}")