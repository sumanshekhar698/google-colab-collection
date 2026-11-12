from datetime import date

class Order:
    TAX_RATE = 0.18
    _count = 0

    def __init__(self, order_id, lines, placed=None):
        self.order_id = order_id
        self.lines = lines
        self.placed = placed or date.today()
        Order._count += 1


    # INSTANCE method
    # [(qty,price),()]
    def total(self):
        amount = 0

        for quantity,price in self.lines:
            amount += quantity*price

        return amount

    def total_with_tax(self):
        return round((1 + self.TAX_RATE) * self.total(), 2)

    @classmethod
    def count(cls):
        return cls._count # Order._count

    @staticmethod
    def is_valid_order_id(order_id):# ORD
        if not isinstance(order_id, str):
            return False
        return order_id.startswith("ORD-")


# def is_valid_order_id(order_id):# ORD
#     if not isinstance(order_id, str):
#         return False
#     return order_id.startswith("ORD-")

ord_1 = Order("ORD-001", [(2,100),(5,20)])
ord_2 = Order("ORD-002", [(2,115),(5,523)])
print(ord_1.total())
print(ord_1.total_with_tax())

print(ord_1.count())
print(Order.count())
print(Order.is_valid_order_id("0RD-2"))
