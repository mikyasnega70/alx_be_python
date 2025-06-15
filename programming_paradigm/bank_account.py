
class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0
    
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"your current balance is {self.account_balance}")



