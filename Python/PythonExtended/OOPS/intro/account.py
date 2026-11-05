class Account:
    """
    Represents a bank account.

    Attributes:
        owner: Name of the account holder.
        balance: Current account balance.
        history: List of account transactions.

    Methods:
        deposit(): Adds money to the account.
        withdraw(): Withdraws money from the account.
    """

    # __new__() 1. Used to create objects
    # __init__  2. init is triggered to intialise the instance variables 
    def __init__(self,owner, balance=0.0):
        # instance attributes
        self.owner=owner
        self.balance=balance

        # self.history=[]
        # self.history.append(("deposit",balance))
        self.history = [("deposit", balance)]


    def deposit(self,amount):
        # TODO Add amount checks
        self.balance+=amount
        self.history.append(("deposit",amount))

    def withdraw(self,amount):
        # TODO Add amount checks
        self.balance-=amount
        self.history.append(("witdraw",-amount))

    # def tarnsaction_check(): TODO
    #     return True

suman_acc = Account("Suman")
suman_acc.deposit(500)
suman_acc.deposit(500)
Account.deposit(suman_acc,500)

suman_acc.withdraw(100)

ronnie_acc = Account("Ronnie",1000)
ronnie_acc.withdraw(200)
ronnie_acc.deposit(100_000)


# print(suman_acc.owner)
print(suman_acc.balance)
print(suman_acc.history)


print(ronnie_acc.owner)
print(ronnie_acc.balance)
print(ronnie_acc.history)