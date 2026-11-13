from dataclasses import dataclass, field, replace, asdict, FrozenInstanceError


@dataclass( slots=True, frozen=True, kw_only=True, order=True)
class Product:
    code: str
    name: str
    price: float = 0.0
    tags: tuple = ()
    notes: str = field(default="", compare=False, repr=False)

    def __post_init__(self):#dunder
        if self.price < 0:
            raise ValueError("Price cannot be negative")

desk = Product(code="P1", name="Desk", price=1000.5, tags=("office",))
lamp = Product(code="L1", name="Desk", price=1000.5, tags=("office","home"))
table = Product(code="P1", name="Table", price=1100.5, tags=("office",))
# desk = Product("P1","Desk", 1000.5,("office",))


try:
    desk.price = 100 # FrozenInstanceError | frozen=True
except FrozenInstanceError as f:
    print(f)

print(desk)
print(f"Desk- ID {id(desk)} HASH {hash(desk)}")

discounted_desk = replace(desk,price = 900)# shallow copy
print(discounted_desk)
print(f"discounted_desk- ID {id(discounted_desk)} HASH {hash(discounted_desk)}")
print(desk)


# print(hash(desk)) # frozen=True



# desk.color = "Pink" #  slots=True
# print(desk)

print(desk)
list_of_essentials = [desk, lamp, table]
print(sorted(list_of_essentials))

desk_dict = asdict(desk)
print(type(desk_dict))
print(desk_dict)
