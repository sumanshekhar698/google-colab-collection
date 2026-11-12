import json

class JsonMixin:
    """Adds to_json() functioanilty to any sub class"""

    def to_json(self):
        return json.dumps(vars(self), default=str)


class ComparableMixin:
    """Adds comparison, provided the class defines _sort_key()."""
    def _sort_key(self):
        raise NotImplementedError("subclass must define _sort_key")


    def __lt__(self, other):
        return self._sort_key() < other._sort_key()





    # p1 == p2
    def __eq__(self, other):
        return self._sort_key() == other._sort_key()

    def __hash__(self):
        return hash(self._sort_key())

    # __hash__ = None


# 1. its a good habit to Override __eq__ when adding __hash__ and vice versa
# 2. If two objects are equal == they should have same hash value BUT vice versa not exactly true
# 3. The hash should not change, if the deciding factors dont change
# 4. both fn __eq__ and __hash__ are utilized in set and dictionaries


class Product(JsonMixin, ComparableMixin):
    def __init__(self, code, name, price):
        self.code=code
        self.name=name
        self.price=price

    def _sort_key(self):
        return (self.price, self.code)

    def __repr__(self): # DEV friendly
        return f"Product:{self.name!r} Code:{self.code!r} Price:{self.price}"
    
    def __str__(self): # Human-readable output.
        return f"{self.name} ({self.code}) - ₹{self.price:.2f}"


items = [Product("C1", "Loung Chair", 500.0),
         Product("C2", "Office Chair", 300.0),
         Product("C3", "Work Chair", 300.0),
         Product("C3", "Premium Work Chair", 300.0),
         Product("L1", "Desk Lamp", 110.0),
         Product("W1", "Work Table", 600.0),
         ]

print(items[1] < items[2])
print(items[0])

print(sorted(items))
print(vars(items[0]))
print(items[0].to_json())

print(items[2] ==  items[3])


items_set = {Product("C1", "Loung Chair", 500.0),
         Product("C2", "Office Chair", 300.0),
         Product("C3", "Work Chair", 300.0),
         Product("C3", "Premium Work Chair", 300.0),
         Product("L1", "Desk Lamp", 110.0),
         Product("W1", "Work Table", 600.0),
         }

print(len(items_set))
print(items_set)


print(str(items[0]))#__str__
print(repr(items[0]))#__repr__
print(items[0])# __str__
print([items[0]])#__repr__   print a list of objects | items[0].__repr__()