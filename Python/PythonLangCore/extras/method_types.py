from datetime import date


class Order:
    TAX_RATE = 0.18
    _count = 0

    def __init__(self, order_id, lines, placed=None):
        self.order_id = order_id
        self.lines = lines
        self.placed = placed or date.today()

        Order._count += 1

    # INSTANCE METHOD: receives an object as self
    def total(self):
        amount = 0

        for quantity, price in self.lines:
            amount += quantity * price

        return amount

    def total_with_tax(self):
        return round(self.total() * (1 + self.TAX_RATE), 2)

    # CLASS METHOD: receives the class as cls
    @classmethod
    def empty(cls, order_id):
        return cls(order_id, [])

    @classmethod
    def from_csv_row(cls, row):
        values = row.split(",")
        order_id = values[0]
        lines = []

        for i in range(1, len(values), 2):
            quantity = int(values[i])
            price = float(values[i + 1])
            lines.append((quantity, price))

        return cls(order_id, lines)

    @classmethod
    def count(cls):
        return cls._count

    # STATIC METHOD: receives neither the object nor the class
    @staticmethod
    def is_valid_id(order_id):
        if not isinstance(order_id, str):
            return False

        return order_id.startswith("ORD-")

    def __repr__(self):
        return f"{type(self).__name__}({self.order_id!r}, {len(self.lines)} lines)"


order = Order("ORD-001", [(2, 100)])
print(order.total())  # 200
print(order.total_with_tax())  # 218
print(order)

print(Order.empty("ORD-002"))  #
# return Order(order_id, [])
print(Order.is_valid_id("ORD-001"))  # True)
print(Order.is_valid_id("0RD-001"))  # True)
# print(order._count)
print(Order.count())



order_3 =  Order.from_csv_row("ORD-002,3,50.0,1,80.0")
print(order_3)