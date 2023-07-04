players = [
  {
  "name": "Kevin Durant",
  "age":34,
  "position": "small forward",
  "team": "Brooklyn Nets"
  },
  {
  "name": "Jason Tatum",
  "age":24,
  "position": "small forward",
  "team": "Boston Celtics"
  },
  {
  "name": "Kyrie Irving",
  "age":32,
  "position": "Point Guard",
  "team": "Brooklyn Nets"
  },
  {
  "name": "Damian Lillard",
  "age":33,
  "position": "Point Guard",
  "team": "Portland Trailblazers"
  },
  {
  "name": "Joel Embiid",
  "age":32,
  "position": "Power Foward",
  "team": "Philidelphia 76ers"
  },
  {
  "name": "DeMar DeRozan",
  "age": 32,
  "position": "Shooting Guard",
  "team": "Chicago Bulls"
  }
]

class Player:
  def __init__(self, player_info):
    self.name = player_info["name"]
    self.age = player_info["age"]
    self.position = player_info["position"]
    self.team = player_info["team"]

  def get_info(self):
    print(self.name)
    print(self.age)
    print(self.position)
    print(self.team)

  @classmethod
  def get_team(cls, team_list):
    new_list = []
    for player in team_list:
      new_list.append(Player(player))
    return new_list

new_team = Player.get_team(players)
for player in new_team:
  player.get_info()

# kevin = {
#   "name": "Kevin Durant",
#   "age":34,
#   "position": "small forward",
#   "team": "Brooklyn Nets"
# }
# jason = {
#   "name": "Jason Tatum",
#   "age":24,
#   "position": "small forward",
#   "team": "Boston Celtics"
# }
# kyrie = {
#   "name": "Kyrie Irving",
#   "age":32,
#   "position": "Point Guard",
#   "team": "Brooklyn Nets"
# }

# # Create your Player instances here!
# # player_jason = ???
# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)

# print(player_kevin.name)
# print(player_jason.name)
# print(player_kyrie.name)


# new_team = []

# for item in players:
#   new_team.append(Player(item))

# print(new_team[0].name)

# NINJA BONUS: Add a get_team(cls, team_list) @class method

# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
