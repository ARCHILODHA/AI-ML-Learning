# Day 28: Encapsulation in Python

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount("Archi", 5000)

account.deposit(2000)
account.withdraw(1000)

print("Account Holder:", account.owner)
print("Balance:", account.get_balance())
