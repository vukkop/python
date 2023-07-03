class BankAccount:
  all_accounts = []

  def __init__(self, name, balance = 0, int_rate = 0.01):
    self.account_name = name
    self.balance = balance
    self.rate = int_rate
    BankAccount.all_accounts.append(self)

  @classmethod
  def print_bankAccount_info(cls):
    print("-----------------")
    for account in cls.all_accounts:
      print(f"Account name: ${account.account_name}")
      print(f"Balance: ${account.balance}")
      print(f"Rate: {account.rate*100}%")
    return cls

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if(self.balance - amount >= 0):
      self.balance -= amount
      return self
    else:
      print( "Insufficient funds: Charging a $5 fee")
      self.balance - 5
      return self

  def display_account_info(self):
    print(f"Balance: ${self.balance}")
    return self

  def yield_interest(self):
    if (self.balance > 0):
      self.balance = self.balance + self.balance * self.rate
      return self

# account1 = BankAccount(1000, 0.05)
# account2 = BankAccount(2000, 0.1)

# account1.deposit(100).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()
# account2.deposit(150).deposit(320).withdraw(100).withdraw(200).withdraw(160).withdraw(430).yield_interest().display_account_info()


# BankAccount.print_bankAccount_info()
