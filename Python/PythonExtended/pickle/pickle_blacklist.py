from datetime import datetime
import pickle

open("hello.txt", "w").close()

def module_level_function(x):
    return x * 2


class SimpleClass:
    def __init__(self, v):
        self.v = v


cases = [
    ("int",                 42),
    ("list",                [1, 2, 3]),
    ("dict",                {"a": 1}),
    ("set",                 {1, 2}),
    ("datetime",            datetime.now()),
    ("custom instance",     SimpleClass(5)),
    ("module-level func",   module_level_function),
    ("built-in func",       len),
    ("lambda",              lambda x: x),
    ("closure",             (lambda: (lambda y: y))()),
    ("generator",           (i for i in range(3))),
    ("open file handle",    open("hello.txt")),
    ("thread lock",         __import__("threading").Lock()),
]

for name, value in cases:
    try:
        pickle.dumps(value)
        print(f"  OK      {name}")
    except Exception as e:
        print(f"  FAILS   {name:<22} {type(e).__name__}")

cases[-3][1].close()