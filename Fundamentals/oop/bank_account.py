class BankAccount:

    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f'Balance: {self.balance}')
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance * (self.int_rate + 1)
        return self
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(account)


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []


    # other methods
    def create_account(self, amount):
        self.accounts.append(BankAccount(int_rate=0.02, balance=amount))
    
    def make_deposit(self, amount, account):
        # your code here
        self.accounts[account].deposit(amount)

    def make_withdrawal(self, amount, account):
        # your code here
        self.accounts[account].withdraw(amount)

    def display_user_balance(self, account):
        # your code here
        self.accounts[account].display_account_info()

    def transfer_money(self, amount, other_user):
        self.accounts[0].balance -= amount
        other_user.accounts[0].balance += amount



me = User("Matt", "matt@test.com")
molly = User("Molly", "molly@test.com")

me.create_account(10)
me.create_account(2)

molly.create_account(50)

print(me.accounts[0].balance)
print(molly.accounts[0].balance)

me.make_deposit(10, 0)
me.make_deposit(50, 0)
me.transfer_money(12.50, molly)

print(me.accounts[0].balance)
print(molly.accounts[0].balance)
