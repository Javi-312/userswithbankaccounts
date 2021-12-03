class BankAccount:
    #don't forget to add some default values to thesr parameters!
    def __init__(self, int_rate=0, balance=0):
        self.interest=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print("Insuffucient funds: Charginga $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:    
            self.balance = self.balance + self.balance * self.interest
        return self


class User:
    def __init__(self, username, email_address, rate, amount):
        self.name = username
        self.email = email_address
        self.account = BankAccount(rate, amount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s current account balance is ${self.account.display_account_info()}.")

    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.withdraw(amount)
        return self
    
    def monthly_interest(self):
        self.account.yield_interest()
        return self

Javi = User("Javier", "Javi@dojo.com", .002, 500)
Javi.display_user_balance()
Javi.make_deposit(500)
Javi.display_user_balance()