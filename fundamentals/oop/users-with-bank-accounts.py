from bank_account import BankAccount


class User:
  def __init__(self, name, email):
      self.name = name
      self.email = email
      self.accounts = []

  def create_account(self, account_name):
    self.accounts.append(BankAccount( account_name, balance=0, int_rate=0.02))
    return self

  def make_deposit(self, amount, account_name):
    for account in self.accounts:
      if (account.account_name == account_name):
        account.deposit(amount)
    return self

  def make_withdrawal(self, amount, account_name):
    for account in self.accounts:
      if (account.account_name == account_name):
        account.withdraw(amount)
    return self

  def display_user_accounts(self):
    print("====================")
    print(self.name)
    for account in self.accounts:
      print("-----------------")
      print(account.account_name)
      print(account.balance)
      print(account.rate)
    return self

  def transfer_money(self, amount, other_user):
    self.accounts[0].balance -= amount
    other_user.accounts[0].balance += amount

user1 = User("Bob", "bob@gmail.com")
user1.create_account("Savings").create_account("Checking").make_deposit(200, "Savings").make_deposit(300, "Checking").make_withdrawal(150, "Checking")

user2 = User("John", "john@gmail.com")
user2.create_account("Savings").create_account("Checking").make_deposit(100, "Savings").make_deposit(500, "Checking").make_withdrawal(200, "Checking")

user1.transfer_money(30, user2)



user1.display_user_accounts()
user2.display_user_accounts()

