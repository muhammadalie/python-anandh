class bankaccount(object):
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class minimumbalanceaccount(bankaccount):
    minimum_balance=500
    def __init__(self, minimum_balance):
        bankaccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)

a=bankaccount()
print a.deposit(999)
b=minimumbalanceaccount(a)
b.withdraw(600)
