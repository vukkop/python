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

  def enroll(self):
    if(self.is_rewards_member):
      print("Already a member")
    else:
      self.is_rewards_member = True
      self.gold_card_points = 200

  def spend_points(self, amount):
    if(self.gold_card_points - amount >= 0 ):
      self.gold_card_points = self.gold_card_points - amount
    else:
      print("You have insufficient points balance to make this transaction")


first_user = User("Vuk", "Koprivica", "examle@gmail.com", 34)
second_user = User("Bob", "Bobers", "examle.bob@gmail.com", 25)
third_user = User("Amy", "Smith", "examle.smith@gmail.com", 41)


first_user.enroll()
first_user.spend_points(50)
first_user.display_info()
first_user.enroll()
print("-------------------------")
second_user.enroll()
second_user.spend_points(80)
second_user.display_info()
print("-------------------------")
third_user.display_info()
third_user.spend_points(40)
