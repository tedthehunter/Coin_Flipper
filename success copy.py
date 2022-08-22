
import random

class player:
  def __init__(self, name, coins):
    self.name = name
    self.coins = coins
    
  def __repr__(self):
    return f'{self.name} Object'
    
  def status(self):
    if self.coins > 1:
      print(str(self.name) + ': ' + str(self.coins) + ' coins')
    elif self.coins == 1:
      print(str(self.name) + ': ' + str(self.coins) + ' coin')
    else:
      print(str(self.name) + ': 0 coins')
  
  def dq_check(self):
    if self.coins > 0:
      print(str(self.name) + ' has ' + str(self.coins) + ' coins left!')
      return False
    else:
      print(str(self.name) + ' has ' + str(self.coins) + ' coins left!')
      print(str(self.name) + ' has been disqualified!')
      return True


## TRY TO SET A DEFAULT VALUE FOR PLAYER_B IN SUCH A WAY THAT A SINGLE PLAYER WILL AUTOMATICALLY GET A BYE
class game:
  def __init__(self, player_a, player_b=None):
    self.player_a = player_a
    self.player_b = player_b
    
  def __repr__(self):
    return f'Game Object between {self.player_a.name} and {self.player_b.name}'

  def play(self):
    if not self.player_b == None:
      winner = random.choice([self.player_a, self.player_b])
      if winner == self.player_a:
        print(str(self.player_a.name) + ' wins a coin from ' + str(self.player_b.name) + '!')
        self.player_a.coins += 1
        self.player_b.coins -= 1
        if self.player_b.dq_check():
          print('\n')
          return self.player_a
        else:
          print('\n')
          return self.player_a, self.player_b
      else:
        print(str(self.player_b.name) + ' wins a coin from ' + str(self.player_a.name) + '!')
        self.player_b.coins += 1
        self.player_a.coins -= 1
        self.player_a.dq_check()
        print('\n')
    else:
      print(f'{self.player_a.name} gets a bye round.')
      return self.player_a



# this function initializes a number of players and names them
def roster(number_of_players):
  player_list = []
  for i in range(1, number_of_players + 1):
    player_list.append(player(f'Player {str(i)}', 1))
  return player_list

# this function sets the number of coins of all players in a list to the same number
def setup_coins(player_list, number_of_coins):
  for player in player_list:
    player.coins = number_of_coins
    

## WORKING ON TOURNAMENT CLASS -- BROKEN
class tournament:
  def __init__(self, number_of_players, number_of_coins):
    self.number_of_players = number_of_players
    self.number_of_coins = number_of_coins
    self.round_position = 1
    self.player_list = roster(number_of_players)
    setup_coins(self.player_list, number_of_coins)
    
  def __repr__(self):
    return f'Tournament Object between {self.number_of_players} players with {self.number_of_coins} coins'
  
  def status_message(self):
    print('\nRemaining Players:')
    for player in self.player_list:
      player.status()
    print('\n')
  
  def start_tournament(self):
    print('Welcome to the coin flipping tournament!')
    print(f'This tournament includes {self.number_of_players} players with {self.number_of_coins} coins.\n')

  def execute_round(self):
    print(f'Round {str(self.round_position)} begin!')
    self.status_message()
    new_list = []
    while len(self.player_list) > 0:
      new_list.append((game(self.player_list.pop(random.randint(0, len(self.player_list)))), self.player_list.pop(random.randint(0, len(self.player_list)))).play())
    self.player_list = new_list
    self.round_position += 1
    
  def execute_tournament(self):
    self.start_tournament()
    i = 0
    while i < 10:
      self.execute_round()
      i += 1
    # self.announce_winner()
    



# PLAYER CLASS TESTS SUCCESSFUL ***
# test =  player('RJ', 5)
# print(test)
# print(test.name)
# print(test.coins)
# test.status()
# print(test.dq_check())

## GAME CLASS TESTS SUCCESSFUL ***
# rj = player('RJ', 2)
# derrick = player('Derrick', 2)
# test = game(rj, derrick)
# print(test)
# print(test.player_a)
# print(test.player_b)
# test.player_a.status()
# test.player_b.status()
# test.play()
# test.player_a.status()
# test.player_b.status()

test = tournament(4, 2)
print(test)
print(test.player_list)
test.execute_tournament()
