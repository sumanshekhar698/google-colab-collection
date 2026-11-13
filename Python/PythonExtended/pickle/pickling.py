from datetime import datetime, date
from collections import Counter, defaultdict, deque
import pickle

obj = {
    "when" : datetime(2026,9,1,14,30),
    "tags" : {"a", "b" , "c"},
    "counts" : Counter("Hello World"),
    "queue" : deque([52, 4, 55]),
    "nested" : {"deep_tree": [1, {1,2,3}]},
    "none": None
}

print(f" ID Obj {id(obj)} | Type {type(obj)}")

print(obj)
blob = pickle.dumps(obj)
print(type(blob))
print(f"{len(blob)} bytes ")


obj_2 = pickle.loads(blob)
print(obj_2)
print(f" ID Obj {id(obj_2)} | Type {type(obj_2)}")

print(obj  == obj_2)
print(obj  is obj_2)
