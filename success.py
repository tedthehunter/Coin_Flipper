import sys
import math
import random

class player:
  def __init__(self, name, coins, id_num):
    self.name = name
    self.coins = coins
    self.id_num = id_num
    self.disqualified = False
    self.is_heads = False

  def status(self):
    if self.coins > 1:
      print(str(self.name) + ': ' + str(self.coins) + ' coins')
    elif self.coins == 1:
      print(str(self.name) + ': ' + str(self.coins) + ' coin')
    else:
      print(str(self.name) + ': 0 coins')

  def flip(self):
    print(str(self.name) + ' flips a coin!')
    if random.randint(0,1) == 0:
      self.is_heads = False
      return self.is_heads
    else:
      self.is_heads = True
      return self.is_heads

  def dq_check(self):
    if self.coins > 0:
      print(str(self.name) + ' has ' + str(self.coins) + ' coins left!')
    else:
      self.disqualified = True
      print(str(self.name) + ' has ' + str(self.coins) + ' coins left!')
      print(str(self.name) + ' has been disqualified!')

class game:
  def __init__(self, player_a, player_b):
    self.player_a = player_a
    self.player_b = player_b

  def play(self):
    player_a_result = self.player_a.flip()
    player_b_result = self.player_b.flip()
    if player_a_result == player_b_result:
      print('It\'s a tie!  Let\'s try again!')
      self.play()
    elif player_a_result and not player_b_result:
      print(str(self.player_a.name) + ' wins a coin from ' + str(self.player_b.name) + '!')
      self.player_a.coins += 1
      self.player_a.dq_check()
      self.player_b.coins -= 1
      self.player_b.dq_check()
      print('\n')
    elif player_b_result and not player_a_result:
      print(str(self.player_b.name) + ' wins a coin from ' + str(self.player_a.name) + '!')
      self.player_b.coins += 1
      self.player_b.dq_check()
      self.player_a.coins -= 1
      self.player_a.dq_check()
      print('\n')

class round:
  def __init__(self, player_list):
    self.player_list = player_list
    self.game_list = []

  def pair_up(self):
    for player in self.player_list:
      if len(self.player_list) >= 2:
        self.game_list.append(game(self.player_list.pop(0), self.player_list.pop(-1)))
      else:
        pass

  def dq_check(self):
    for game in self.game_list:
      if game.player_a.disqualified == True:
        self.player_list.append(game.player_b)
      elif game.player_b.disqualified == True:
        self.player_list.append(game.player_a)
      else:
        self.player_list.append(game.player_a)
        self.player_list.append(game.player_b)
   
  def execute_round(self):
    self.pair_up()
    for game in self.game_list:
      game.play()
    self.dq_check()
    return self.player_list

#Attempt to make a func that initializes a number of players
def roster(number_of_players):
  player_list = []
  for i in range(1, number_of_players + 1):
    player_list.append(player('Player ' +str(i), 1, i))
  return player_list

def setup_coins(player_list, number_of_coins):
  for player in player_list:
    player.coins = number_of_coins

def status_message(player_list):
  print('\nRoster:')
  for player in player_list:
    player.status()
  print('\n')

# def tournament(number_of_players, number_of_coins):
#   print('Welcome to the coin flipping tournament!')
#   print('\nRoster:')
#   player_list = roster(number_of_players)
#   setup_coins(player_list, number_of_coins)
#   status_message(player_list)
#   print('\n')
#   round_position = 1
#   round_start()
#   print(round_position)

class tournament:
  def __init__(self, number_of_players, number_of_coins):
    self.number_of_players = number_of_players
    self.number_of_coins = number_of_coins
    self.round_position = 0
    self.player_list = roster(number_of_players)
    setup_coins(self.player_list, number_of_coins)
  
  def start_tournament(self):
    print('Welcome to the coin flipping tournament!')
    self.next_round()

  def round_start(self):
    self.round_position += 1
    current_round = round(self.player_list)
    print('Round ' + str(self.round_position) + ' begin!')
    status_message(self.player_list)
    self.player_list = current_round.execute_round()

  def next_round(self):
    while len(self.player_list) > 1:
      self.round_start()
    print('The tournament is complete!')
    print(str(self.player_list[0].name) + ' is the winner!')

    



test = tournament(300, 1)
test.start_tournament()
