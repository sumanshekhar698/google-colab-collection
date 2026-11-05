class BankAccount:
    
    # class variable
    bank_name = "Celestal Bank"
    interest_rate=0.08
    # the golden rule is not keep any mutable things in class variables


    def __init__(self, owner):
        self.owner=owner
        self.history=[]

    def deposit(self, amount):
        self.history.append((self.owner,amount))

suman_acc = BankAccount("Suman")
suman_acc.deposit(100)
suman_acc.deposit(200)
suman_acc.deposit(-500)

print(suman_acc.bank_name)
print(suman_acc.interest_rate)
print(suman_acc.history)

ronnie_acc = BankAccount("Ronnie")
ronnie_acc.deposit(1500)
ronnie_acc.deposit(-210)
print(ronnie_acc.history)

alisha_acc = BankAccount("Alisha")
alisha_acc.deposit(100)
alisha_acc.deposit(-10)
print(alisha_acc.history)


print(suman_acc.history is alisha_acc.history)




