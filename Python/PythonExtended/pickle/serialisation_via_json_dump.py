from datetime import datetime, date
from collections import Counter
import json

obj = {
    "when" : datetime(2026,9,1,14,30),
    "tags" : {"a", "b" , "c"},
    "counts" : Counter("Hello World"),
    "nested" : {"deep_tree": [1, {1,2,3}]}
}

print(obj)

obj = {"name": "Suman", "roll": 8}

print(json.dumps(obj))