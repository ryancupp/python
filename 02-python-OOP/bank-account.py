class BankAccount:
    beginning_balance = 0
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance=  balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        print("Deposit:", amount)
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        print("Withdraw:", amount)
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate} Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self

account1= BankAccount(0.02, 200)

account2 = BankAccount(0.03, 800)

account1.deposit(76).deposit(89).deposit(634).withdraw(139).yield_interest().display_account_info()

account2.deposit(320).deposit(55).withdraw(48).withdraw(19).withdraw(155).withdraw(73).yield_interest().display_account_info()

