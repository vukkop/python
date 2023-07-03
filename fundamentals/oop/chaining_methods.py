class User:

  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0

  def display_info(self):
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print(self.age)
    print(self.is_rewards_member)
    print(self.gold_card_points)
    return self

  def enroll(self):
    if(self.is_rewards_member == True):
      print("Already a member")
      return self
    else:
      self.is_rewards_member = True
      self.gold_card_points = 200
      return self

  def spend_points(self, amount):
    if(self.gold_card_points - amount >= 0 ):
      self.gold_card_points = self.gold_card_points - amount
      return self
    else:
      print("You have insufficient points balance to make this transaction")
      return self


first_user = User("Vuk", "Koprivica", "examle@gmail.com", 34)
second_user = User("Bob", "Bobers", "examle.bob@gmail.com", 25)
third_user = User("Amy", "Smith", "examle.smith@gmail.com", 41)


first_user.display_info().enroll().spend_points(50).enroll().display_info()
print("-------------------------")
second_user.enroll().spend_points(80).display_info()
print("-------------------------")
third_user.display_info().spend_points(40)
