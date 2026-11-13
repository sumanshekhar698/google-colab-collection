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

with open("data_obj.pkl","wb") as f:
    pickle.dump(obj,f)

