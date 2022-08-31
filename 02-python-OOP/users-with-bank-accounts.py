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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance = 0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(self.account.balance)

