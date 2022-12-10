# import socket
from Network import Network

result_verdict = False

def main():
  run = True
  n = Network()
  player = int(n.getP())
  print("Player: ", player)
  global result_verdict
  while run:
    try:
      game = n.send("get")
      # print(game)
    except:
      run = False
      print("fail 1")
      print("Game not found")
      break
    #Generates initial prompt to clients
    if game.connected():
      if player == 0:
        if not game.p1Moved:
          print(f"The theme is: {game.theme}. Your word is {len(game.answer)} letters long")
          move = input("Guess a letter or word: ").lower()
          game.play(player,move)
          n.send(move)
      else:
        if not game.p2Moved:
          print(f"The theme is: {game.theme}. Your word is {len(game.answer)} letters long")
          move = input("Guess a letter or word: ").lower()
          game.play(player,move)
          n.send(move) #sends letter or word guessed to the server
      game.p1Moved = True
      game.p2Moved = True
      guess = ''   
    
    while game.play_game: 
      if game.bothMoved(): #checks if p1Moved & p2Moved are true
        try:
          #game = n.send("reset")
          pass
        except:
          run = False
          print("fail 2")
          print("Game not Found")
          break
        #compares move from player 1 against if-else statements to check is their guess was valid
        if player == 0:
          if game.p1Moved:
            if isinstance(game.is_move_valid(player,move), bool): #is_move_valid can return a tuple or bool. tuple indicates word guessed, bool indicates letter guessed
              if (len(guess) < len(game.answer)-1) and game.p1_guess_left > 1:
                if game.is_move_valid(player,move):
                  if move in guess:
                    print(f"You guessed '{move}' already! Guess again.")
                    move = input("Guess a letter or word: ").lower()
                  else:
                    print(f"Good guess! Letter: {move} found. \nRemaining lives: {game.p1_guess_left}")
                    count = game.answer.count(move) #count = amount of times letter occurs in answer
                  for num in range(count): #increases guess to prevent user from having to input the same letter
                    guess += move
                  move = input("Guess a letter or word: ").lower()
                else:
                  game.p1_guess_left -= 1
                  print(f"Letter: '{move}' not found. \nRemaining lives: {game.p1_guess_left}")
                  move = input("Guess a letter or word: ").lower()
              else:
                  result_verdict = game.winner(guess) #type(result_verdict, bool)
                  game.play_game = False
            else:
              result_verdict = game.winner(move)
              game.play_game = False
        else:
          #same instructions as player 1
          if game.p2Moved:
            if isinstance(game.is_move_valid(player,move),bool): 
              if (len(guess) < len(game.answer)-1) and game.p2_guess_left > 1:
                if game.is_move_valid(player,move):
                  if move in guess:
                    print(f"You guessed '{move}' already. Guess again.")
                    move = input("Guess a letter or word: ").lower()
                  else:
                    print(f"Good guess! Letter: {move} found. \nRemaining lives: {game.p2_guess_left}")
                    count = game.answer.count(move)
                  for num in range(count):
                    guess += move
                  move = input("Guess a letter or word: ").lower()
                else:
                  game.p2_guess_left -= 1
                  print(f"Letter: '{move}' not found. \nRemaining lives: {game.p2_guess_left}")
                  move = input("Guess a letter or word: ").lower()
              else:
                result_verdict = game.winner(guess)
                game.play_game = False
            else:
              result_verdict = game.winner(move)
              game.play_game = False
    game.play_game = False
    if (result_verdict == True and player == 1) or (result_verdict == True and player == 0):
      print(f"You won! The word was {game.answer}")
    else:
      print(f"You lost! The word was {game.answer}")
    break

main()
      
    
        
      
      
      
  

