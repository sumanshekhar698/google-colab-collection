from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    # ABSTRACT METHODS
    @abstractmethod
    def pay(self,amount):
        """this should be implmented by the child class"""

    @abstractmethod    
    def refund(self, amount):
        """this should be implmented by the child class"""

    # CONCRETE METHOD
    def pay_with_receipt(self, amount):
        res = self.pay(amount)
        return f"{res}  [receipt #DONE]"
    


class CreditCard(PaymentMethod):
    def pay(self,amount):
        return f"charged {amount:,.2f} via CC"

    def refund(self, amount):
        return f"refund processed to CC of amount {amount}"


class UPI(PaymentMethod):
    def pay(self,amount):
        return f"charged {amount:,.2f} via UPI"
    
    def refund(self, amount):
        return f"refund processed to UPI of amount {amount}"

class Incomplete(PaymentMethod):
    def pay(self,amount):
        return f"PAID {amount:,.2f}"
    # !!!!!!!!!
    


cc = CreditCard()
print(cc.pay(10000))
print(cc.refund(10000))
print(cc.pay_with_receipt(10000))

print()
upi = UPI()
print(upi.pay(10000))
print(upi.refund(10000))
print(upi.pay_with_receipt(10000))

print()
# incmplete = Incomplete()
# print(incmplete.pay(500))
# print(incmplete.refund(500))