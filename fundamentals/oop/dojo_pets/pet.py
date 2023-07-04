class Pet:
# implement __init__( name , type , tricks ):
  def __init__(self, name , type , tricks):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.energy = 50
    self.health = 50

# implement the following methods:
# sleep() - increases the pets energy by 25
  def sleep(self):
    print("Pet sleeping ZZZZzzzzz")
    self.pet.energy += 25
    return self
# eat() - increases the pet's energy by 5 & health by 10
  def eat(self):
    print("Pet eating")
    self.pet.energy += 5
    self.pet.health += 10
    return self
# play() - increases the pet's health by 5
  def play(self):
    print("Pet playing")
    self.pet.health += 5
    return self
# noise() - prints out the pet's sound
  def noise(self):
    print("Aw AW Aw")
    return self
