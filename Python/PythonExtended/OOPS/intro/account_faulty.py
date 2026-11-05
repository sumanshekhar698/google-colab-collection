class BadAccount:
    history=[]
    # class variable


    def __init__(self, owner):
        self.owner=owner


    def deposit(self, amount):
        self.history.append((self.owner,amount))

suman_acc_bad = BadAccount("Suman")
suman_acc_bad.deposit(100)
suman_acc_bad.deposit(200)
suman_acc_bad.deposit(-500)
print(suman_acc_bad.history)

ronnie_acc_bad = BadAccount("Ronnie")
ronnie_acc_bad.deposit(1500)
ronnie_acc_bad.deposit(-210)
print(ronnie_acc_bad.history)

alisha_acc_bad = BadAccount("Alisha")
alisha_acc_bad.deposit(100)
alisha_acc_bad.deposit(-10)
print(alisha_acc_bad.history)



