def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']


a=make_account()
b=make_account()
print deposit(a,2500)
print withdraw(a,200)
