import math

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
        transaction_check(): Validates a transaction.
    """

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.history = [("deposit", balance)] if balance > 0 else []



    def transaction_check(self):
        calculated_balance = sum(amount for _, amount in self.history)
        return math.isclose(calculated_balance, self.balance)
        # return calculated_balance == self.balance

    def validate(self, amount):
        """Validates transaction amount."""
        # if not isinstance(amount, (int, float)):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        return True


    def deposit(self, amount):
        try:
            self.validate(amount)

            self.balance += amount
            self.history.append(("deposit", amount))

            print(f"Successfully deposited: {amount}")

        except (ValueError, TypeError) as e:
            print(f"Deposit failed: {e}")





    def withdraw(self, amount):
        try:
            self.validate(amount)

            if amount > self.balance:
                raise ValueError("Insufficient balance.")

            self.balance -= amount
            self.history.append(("withdraw", -amount))

            print(f"Successfully withdrawn: {amount}")

        except (ValueError, TypeError) as e:
            print(f"Withdrawal failed: {e}")

    # def withdraw_old(self, amount):
    #     self.validate(amount)

    #     if amount > self.balance:
    #         raise ValueError("Insufficient balance.")

    #     self.balance -= amount
    #     self.history.append(("withdraw", -amount))

    # def deposit_old(self, amount):
    #     self.validate(amount)

    #     self.balance += amount
    #     self.history.append(("deposit", amount))


# Create accounts
suman_acc = Account("Suman")

suman_acc.deposit(-500)
suman_acc.deposit(500.95)

# Calling instance method using class name
Account.deposit(suman_acc, 500)

suman_acc.withdraw(1000100)

ronnie_acc = Account("Ronnie", 1000)
ronnie_acc.withdraw(200)
ronnie_acc.deposit(100_000)


# Display account details
print(suman_acc.owner)
print(suman_acc.balance)
print(suman_acc.history)
print(f"tr check :: {suman_acc.transaction_check()}")

# print(ronnie_acc.owner)
# ronnie_acc.balance = 1000000000000000
print(ronnie_acc.balance)
print(ronnie_acc.history)
