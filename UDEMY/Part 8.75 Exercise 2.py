class Account():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
    def deposit(self, add_money):
        self.balance += add_money
        return self.balance
    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            return self.balance
        else :
            print ("The account can't be overdrawn")

acct1 = Account('XTruong', 1000000)
acct1.deposit(1000000)

print(acct1.balance)

acct1.withdraw(500000)
print(acct1.balance)

acct1.withdraw(2500000)
print(acct1.balance)
