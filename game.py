import random

class Game:
  def __init__(self, id):
    self.p1Moved = False
    self.p2Moved = False
    self.ready = False
    self.id = id
    self.moves = [None,None]
    self.wins = [0,0]
    self.ties = 0
    self.word_bank = {"animal":["tiger", "cheetah", "elephant", "buffalo","butterfly","bird", "shark"], "art supplies": ["paintbrush", "canvas","sketchbook","graphite","acrylics", "pen"],
"movies":["BlackPanther", "Parasite", "RushHour", "TheGodfather", "Elf", "It", "Nope"]}
    self.word_bank_keys = ["animal","art supplies","movies"]
    self.theme = random.choice(self.word_bank_keys)
    self.answer =random.choice(self.word_bank[self.theme])
    self.p1_guess_left = 6
    self.p2_guess_left = 6
    self.play_game = True

#stores player's move
  def play(self, player, move):
    self.moves[player] = move

#returns player's move
  def player_move(self, player):
    return self.moves[player]

#allows for client script to ask initial prompt
  def connected(self):
    self.ready = True
    return self.ready

#should return True in order for addition guessing prompts and response to happen
  def bothMoved(self):
    return self.p1Moved and self.p2Moved

#determines if move for player is in answer, returns boolean for letter guess, & tuple for word guess
  def is_move_valid(self, player, move):#player = type(int) move = type(str)
    self.answer = self.answer.lower()
    if len(move) == 1:
      if move in self.answer:
        return True
      else:
        if player == 0:
          return False
        else:
          return False
    else:
      if move == self.answer.lower():
        return (True, "winner")
    return (False, "loser")


#checks of word guessed is the answer, returns boolean 
  def winner(self, verdict): #verdict is either tuple (bool,string) or string of letters guessed
    count = 0
    if isinstance(verdict,tuple):
      if verdict[0] == True:
        return True
      else:
        False
    for char in range(len(verdict)):
      if verdict[char] in self.answer:
         count += 1
         if count == len(self.answer):
          return True
    return False




      

    


  
