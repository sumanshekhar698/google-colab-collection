class SafeAccount:

    def __init__(self, owner, balance=0.0):
        self.owner =owner
        self._bank_code = "CLEAR123" # internl use only (protected)
        self.__balance=balance # (private) variable name mangling(_SafeAccount__balance)
        self.history=[]


    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.history.append(("deposit",amount))
    
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Withdraw Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        self.history.append(("withdraw",-amount))

    # getters
    def get_balance(self):
        return self.__balance


suman_acc = SafeAccount("Suman",1000)
suman_acc.deposit(1050)
# print(suman_acc._bank_code)
print(suman_acc.__balance)

# print(suman_acc._SafeAccount__balance)
print(suman_acc.get_balance())