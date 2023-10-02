class Account:
    counter_number = 0
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        Account.counter_number += 1
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self .balance = self.balance - amount
        return self.balance

a = Account('Tom')
b = Account('Jim')
print(a.counter_number)
print(b.counter_number)
