from pet import Pet

class Ninja(Pet):
# implement __init__( first_name , last_name , treats , pet_food , pet )
  def __init__(self, first_name , last_name , treats , pet_food , pet):
    self.first_name = first_name
    self.last_name = last_name
    self.treats = treats
    self.pet_food = pet_food
    self.pet = pet

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
  def walk(self):
    print("Ninja going for a walk.")
    super().play()
    return self
# feed() - feeds the ninja's pet invoking the pet eat() method
  def feed(self):
    print("Ninja feeding pet.")
    super().eat()
    return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
  def bathe(self):
    print("Ninja batheing pet.")
    super().noise()
    return self


ninja1 = Ninja("Bob", "Smith", "Bone treats", "Salmon", Pet("Max", "Weimaraner", "High Five"))

ninja1.walk().feed().bathe()
