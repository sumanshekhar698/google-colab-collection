from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay():
        pass

    @abstractmethod
    def refund():
        pass

    @abstractmethod
    def scan_qr():
        pass


# class CreditCard(Payment):
#     def pay(self, amount):
#         return f"Paid ₹{amount} using Credit Card"

#     def refund(self, amount):
#         return f"Refunded ₹{amount}"

#     def scan_qr(self):
#         raise NotImplementedError("Credit cards don't scan QR codes")


# class Cash(Payment):

#     def pay(self, amount):
#         return f"Paid ₹{amount} using Cash"

#     def refund(self, amount):
#         raise NotImplementedError("Cash payment doesn't support automatic refunds")

#     def scan_qr(self):
#         raise NotImplementedError("Cash doesn't scan QR codes")


class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass


class Refundable(ABC):

    @abstractmethod
    def refund(self):
        pass


class QRPayable(ABC):
    @abstractmethod
    def scan_qr(self):
        pass


class CreditCard(Payable, Refundable):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

    def refund(self, amount):
        return f"Refunded ₹{amount} to Credit Card"


class UPI(Payable, Refundable, QRPayable):

    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"

    def refund(self, amount):
        return f"Refunded ₹{amount} to UPI"

    def scan_qr(self):
        return "UPI QR Code scanned"


# Cash supports only payment
class Cash(Payable):

    def pay(self, amount):
        return f"Paid ₹{amount} using Cash"

cc = CreditCard()
print(cc.pay(100))
print(cc.refund(100))

upi = UPI()
print(upi.scan_qr())
print(upi.pay(88))
print(upi.refund(88))