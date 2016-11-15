class BankAccount():
    def withdraw(self):
        pass
    def deposit(self):
        pass
class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500

    def withdraw(self, amount):
        if self.balance -amount < 500:
            return "Cannot withdraw beyond the minimum account balance"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
        return self.balance
    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit ammount"
        else:
            self.balance += amount
        return self.balance

class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if amount < 0 :
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount < 0:
            return "Invalid wuthdaw amount"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"