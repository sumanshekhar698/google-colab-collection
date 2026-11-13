
class ProductManual:
    
    def __init__(self, code, name, price, tags=None):
        self.code, self.name, self.price = code, name, price
        self.tags = tags if tags is not None else []

    def __repr__(self):
        return (f"ProductManual(code={self.code!r}, name={self.name!r} price={self.price!r}, tags={self.tags!r})")

    def __eq__(self, other):
        if not isinstance(other, ProductManual):
            return NotImplemented
        return (self.code, self.name, self.price, self.tags) == (other.code, other.name, other.price, other.tags)

    # __hash__() = None 

    def __hash__(self):
        return hash((self.code, self.name, self.price, tuple(self.tags)))
    # The factors in a __hash__ (instance attributes)should not change in the object lifecycle


p1 = ProductManual("P1", "Desk", 1200.0)
p1_1 = ProductManual("P1", "Desk", 1200.0)
p2 = ProductManual("P2", "Desk", 1200.0)

print(p1 == p1_1)
print(p1 == p2)

set_of_products = {p1, p1_1, p2}

print(hash(p1))
print(hash(p1_1))
print(hash(p2))


p2.name = "P1" # My ProductManual object is mutable

print(set_of_products)
print(hash(p1))
print(hash(p1_1))
print(hash(p2))

for p in set_of_products:
    print(p)